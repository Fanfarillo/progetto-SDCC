from BooDB import *

"""
Questa funzione controlla la tabella Volo periodicamente. Per ciascun controllo (e per ciascun volo) si hanno i seguenti casi:
1) Il volo è di oggi (o del passato). In tal caso si elimina il volo dalle tabelle Volo e PostiOccupati, si raccolgono in un messaggio le relative informazioni
    a partire da StoricoVolo, si elimina il volo anche da StoricoVolo e si invia il messaggio al microservizio Suggestions tramite chiamata gRPC.
2) Il volo è di una data futura. In tal caso si fa un controllo anche nella tabella StoricoVolo e:
    2.1) Se in StoricoVolo si hanno già informazioni per quel volo relative alla giornata di oggi (in particolar modo il prezzo), allora non si fa nulla.
    2.2) Altrimenti si aggiungono le informazioni per quel volo relative alla giornata di oggi all'interno di StoricoVolo.
"""
def checkFlights(logger):
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
                deleteFromStoricoVolo(key)      #eliminazione del volo dalla tabella StoricoVolo
                logger.info('[COORDINAMENTO CON SUGGESTIONS] Eliminato il volo ' + key + ' dalla tabella StoricoVolo.')
                #TODO: comunicazione gRPC (lato client) con Suggestions
