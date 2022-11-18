from BooDB import *

"""
Questa funzione controlla la tabella Volo periodicamente. Per ciascun controllo (e per ciascun volo) si hanno i seguenti casi:
1) Il volo è di oggi. In tal caso si elimina il volo dalle tabelle Volo e PostiOccupati, si raccolgono in un messaggio le relative informazioni a partire
    da StoricoVolo, si elimina il volo anche da StoricoVolo e si invia il messaggio al microservizio Suggestions tramite chiamata gRPC.
2) Il volo è di una data futura. In tal caso si fa un controllo anche nella tabella StoricoVolo e:
    2.1) Se in StoricoVolo si hanno già informazioni per quel volo relative alla giornata di oggi (in particolar modo il prezzo), allora non si fa nulla.
    2.2) Altrimenti si aggiungono le informazioni per quel volo relative alla giornata di oggi all'interno di StoricoVolo.
"""
def checkFlights(logger):
    logger.info('Thread associato al coordinamento con Suggestions creato con successo.')

    while(True):
        #flightsDict è un dizionario che, a ogni volo (i.e. idVolo), associa lo stato di quel volo (True se è di oggi, False altrimenti)
        flightsDict = getFlightsStatus()
