import grpc
import time

from proto import Suggestions_pb2
from proto import Suggestions_pb2_grpc
from proto import Discovery_pb2
from proto import Discovery_pb2_grpc

from BooDB import *


ADDR_PORT = ''



def discovery_suggestions_micro(all_discovery_servers, logger):
    global ADDR_PORT
    ok = False
    while(True):
        """
        Itero sui discovery servers noti al microservizio
        per ottenere la porta ricercata.
        """
        for discovery_server in all_discovery_servers:
            try:
                # Provo a connettermi al server.
                channel = grpc.insecure_channel(discovery_server)
                stub = Discovery_pb2_grpc.DiscoveryServiceStub(channel)
                # Ottengo la porta su cui è in ascolto il microservizio di Booking
                res = stub.get(Discovery_pb2.GetRequest(serviceName="booking" , serviceNameTarget="code_suggestions_1"))
            except:
                # Si è verificato un problema nella connessione con il discovery server
                logger.info('[GET DISCOVERY SUGGESTIONS] Problema connessione con il discovery server ' + discovery_server + '.')
                time.sleep(2)
                continue
            if (res.port == '-1'):
                logger.info('[GET DISCOVERY SUGGESTIONS] porta ancora non conosciuta dal discovery server ' + discovery_server + ' riprovare.')
                time.sleep(2)
                continue
            ok = True
            logger.info('[GET DISCOVERY SUGGESTIONS] porta del servizio di booking recuperata: ' + res.port + '.')
            ADDR_PORT = res.serviceName + ':' + res.port
            break
        if(ok):
            break
        logger.info('[GET DISCOVERY SUGGESTIONS] Richiesta di GET avvenuta con insuccesso presso tutti i discovery servers.')
        time.sleep(5)


"""
Questa funzione controlla la tabella Volo periodicamente. Per ciascun controllo (e per ciascun volo) si hanno i seguenti casi:
1) Il volo è di oggi (o del passato). In tal caso si elimina il volo dalle tabelle Volo e PostiOccupati, si raccolgono in un messaggio le relative informazioni
    a partire da StoricoVolo, si elimina il volo anche da StoricoVolo e si invia il messaggio al microservizio Suggestions tramite chiamata gRPC.
2) Il volo è di una data futura. In tal caso si fa un controllo anche nella tabella StoricoVolo e:
    2.1) Se in StoricoVolo si hanno già informazioni per quel volo relative alla giornata di oggi (in particolar modo il prezzo), allora non si fa nulla.
    2.2) Altrimenti si aggiungono le informazioni per quel volo relative alla giornata di oggi all'interno di StoricoVolo.
"""
def checkFlights(logger, all_discovery_servers):
    logger.info('Thread associato al coordinamento con Suggestions creato con successo.')

    while(True):
        #flightsDict è un dizionario che, a ogni volo (i.e. idVolo), associa lo stato di quel volo (True se è di oggi / del passato, False altrimenti)
        flightsDict = getFlightsStatus()
        logger.info('[COORDINAMENTO CON SUGGESTIONS] Classificazioni voli del passato vs del futuro completata.')

        #questa non è altro che un'iterazione sui voli
        for key, value in flightsDict.items():

            if value==True:                     #caso in cui il volo è di oggi o del passato
                logger.info('[COORDINAMENTO CON SUGGESTIONS] Il volo ' + key + ' è di oggi (o del passato).')
                deleteFromVolo(key)             #eliminazione del volo dalla tabella Volo
                logger.info('[COORDINAMENTO CON SUGGESTIONS] Eliminato il volo ' + key + ' dalla tabella Volo.')
                deleteFromPostiOccupati(key)    #eliminazione del volo dalla tabella PostiOccupati
                logger.info('[COORDINAMENTO CON SUGGESTIONS] Eliminato il volo ' + key + ' dalla tabella PostiOccupati.')
                msg = getFlightHistory(key)     #generazione del messaggio contenente lo storico del prezzo del volo da inviare a Sugggestions tramite gRPC
                logger.info('[COORDINAMENTO CON SUGGESTIONS] Generato il messaggio da inviare a Suggestions relativo al volo ' + key + '.')
                
                #è necessario ottenere tutte le date in cui era possibile prenotare il volo per rimuovere correttamente il volo dalla tabella StoricoVolo
                bookingDates = getBookingDates(key)
                
                """
                Non è detto che il volo si trovi effettivamente anche nella tabella StoricoVolo.
                Il blocco try-except serve ad evitare che un'eccezione dovuta a questo blocchi il coordinamento tra Booking e Suggestions.
                La variabile rpc, a tal proposito, indica se deve essere effettuata la chiamata gRPC al microservizio Suggestions.
                """
                rpc = True
                try:
                    deleteFromStoricoVolo(key, bookingDates)      #eliminazione del volo dalla tabella StoricoVolo
                    logger.info('[COORDINAMENTO CON SUGGESTIONS] Eliminato il volo ' + key + ' dalla tabella StoricoVolo.')
                except:
                    logger.info("[COORDINAMENTO CON SUGGESTIONS] Il volo " +  key + " già non era presente di suo all'interno della tabella StoricoVolo.")
                    rpc = False

                if rpc == True:
                    # -------------------------------- DISCOVERY -------------------------------------------------------------------
                    if (ADDR_PORT == ''):
                        discovery_suggestions_micro(all_discovery_servers, logger)
                    # -------------------------------- DISCOVERY -------------------------------------------------------------------

                    while(True):
                        try:
                            """ Comunicazione gRPC (lato client) con Suggestions """               
                            #open gRPC channel
                            channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num    
                            #create client stub
                            stub = Suggestions_pb2_grpc.SuggestionsServiceStub(channel)
                            #non possiamo invocare una return perché il ciclo while deve essere infinito
                            stub.StoreOldFlight(Suggestions_pb2.OldFlight(oldFlightsMsg=msg))
                            logger.info('[COORDINAMENTO CON SUGGESTIONS] Inviato il messaggio a Suggestions mediante chiamata gRPC.')
                            break
                        except:
                            #se entriamo qui, vuol dire che il microservizio Suggestions non è ancora sveglio
                            logger.info('[COORDINAMENTO CON SUGGESTIONS] Ancora non è possibile inviare il messaggio a Suggestions mediante chiamata gRPC.')
                            time.sleep(5)
                            continue

            else:           #caso in cui il volo è del futuro
                logger.info('[COORDINAMENTO CON SUGGESTIONS] Il volo ' + key + ' è del futuro.')
                isInStorico = isTodayInStorico(key)         #check su se il prezzo di oggi del volo 'key' è stato registrato in StoricoVolo o meno

                #se isInStorico==True, non è necessario fare nulla; altrimenti si procede a memorizzare le nuove informazioni in StoricoVolo
                if isInStorico==False:
                    logger.info('[COORDINAMENTO CON SUGGESTIONS] È ancora necessario registrare il prezzo di oggi del volo ' + key + ' in StoricoVolo.')
                    flight = retrieveFlightInfo(key)        #ottenimento di DataVolo, AeroportoPartenza, AeroportoArrivo, CompagniaAerea e PrezzoBase del volo
                    storeInStoricoVolo(flight)              #aggiunta delle informazioni incapsulate in flight nella tabella StoricoVolo
                    logger.info('[COORDINAMENTO CON SUGGESTIONS] Il prezzo di oggi del volo ' + key + ' è stato registrato in StoricoVolo.')

                else:
                    logger.info('[COORDINAMENTO CON SUGGESTIONS] È stato già registrato il prezzo di oggi del volo ' + key + ' in StoricoVolo.')

        #terminate le iterazioni sui voli all'interno del ciclo for, si mette il thread in pausa per 6 ore (=21600 secondi), così da non sovraccaricare la CPU
        time.sleep(21600)
