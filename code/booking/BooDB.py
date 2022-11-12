import boto3
import grpc
import time

from boto3.dynamodb.conditions import Attr
from decimal import *

from proto import Managment_pb2
from proto import Managment_pb2_grpc

from proto import Discovery_pb2
from proto import Discovery_pb2_grpc

from BooUtils import *


# ADDR_PORT = 'management:50052'
# -------------------------------------------------- DISCOVERY ----------------------------------------------
ADDR_PORT = ''
# -------------------------------------------------- DISCOVERY ----------------------------------------------

DYNAMODB = 'dynamodb'
REGIONE = 'us-east-1'
TABELLA_VOLO = 'Volo'
TABELLA_POSTI_OCCUPATI = 'PostiOccupati'


# L'assunzione fatta sui possibili posti disponibili dell'aereo.
postiTotali = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5',
'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'A10', 'B10', 'C10', 'D10', 'E10', 'F10',
'A11', 'B11', 'C11', 'D11', 'E11', 'F11', 'A12', 'B12', 'C12', 'D12', 'E12', 'F12', 'A13', 'B13', 'C13', 'D13', 'E13', 'F13', 'A14', 'B14', 'C14', 'D14', 'E14', 'F14', 'A15', 'B15', 'C15', 'D15', 'E15', 'F15',
'A16', 'B16', 'C16', 'D16', 'E16', 'F16', 'A17', 'B17', 'C17', 'D17', 'E17', 'F17', 'A18', 'B18', 'C18', 'D18', 'E18', 'F18', 'A19', 'B19', 'C19', 'D19', 'E19', 'F19', 'A20', 'B20', 'C20', 'D20', 'E20', 'F20',
"A21", "B21", "C21", "D21", "E21", "F21", "A22", "B22", "C22", "D22", "E22", "F22", "A23", "B23", "C23", "D23", "E23", "F23", "A24", "B24", "C24", "D24", "E24", "F24", "A25", "B25", "C25", "D25", "E25", "F25",
"A26", "B26", "C26", "D26", "E26", "F26"]



class Flight:
    def __init__(self, idKey, compagnia_aerea, arrivo, partenza, orario, data, prezzo, postiDisponibili):
        # Identificativo del volo
        self.idKey = idKey
        # Compagnia aerea
        self.compagnia_aerea = compagnia_aerea
        # Aeroporto di arrivo
        self.arrivo = arrivo
        # Aeroporto di partenza
        self.partenza = partenza
        # Orario del volo
        self.orario = orario
        # Data del volo
        self.data = data
        # Prezzo del volo per singolo posto
        self.prezzo = prezzo
        # Identificativi dei posti disponibili
        self.postiDisponibili = postiDisponibili



#this function returns true if there is no item with the specified id (i.e. the specified primary key); it returns false otherwise
def isNewId(flightId):
    dynamodb = boto3.resource(DYNAMODB, REGIONE)
    table = dynamodb.Table(TABELLA_VOLO)

    #read from 'Volo' table in DynamoDB
    response = table.get_item(
        Key = {
            'Id': flightId,
        }
    )

    if 'Item' in response:
        return False
    else:
        return True



def storeFlight(flightId, date, departureAirport, arrivalAirport, departureTime, arrivalTime, airline, price, seats):
    dynamodb = boto3.resource(DYNAMODB, REGIONE)
    tableVolo = dynamodb.Table(TABELLA_VOLO)
    tablePosti = dynamodb.Table(TABELLA_POSTI_OCCUPATI)
    
    #store an item in 'Volo' table in DynamoDB
    tableVolo.put_item(
        Item = {
            'Id': flightId,
            'Data': date,
            'Aeroporto partenza': departureAirport,
            'Aeroporto arrivo': arrivalAirport,
            'Orario partenza': departureTime,
            'Orario arrivo': arrivalTime,
            'Compagnia aerea': airline,
            'Prezzo base': Decimal(price),
            'Posti liberi': seats
        }
    )

    #store an item in 'PostiOccupati' table in DynamoDB
    tablePosti.put_item(
        Item = {
            'IdVolo': flightId
        }
    )



def storeUpdatedFlight(flightId, newPrice):
    dynamodb = boto3.resource(DYNAMODB, REGIONE)
    table = dynamodb.Table(TABELLA_VOLO)

    #read from 'Volo' table in DynamoDB
    response = table.get_item(
	    Key = {
	        'Id': flightId,
	    }
    )

    #retrieve all the information about selected flight
    item = response['Item']
    date = item['Data']
    departureAirport = item['Aeroporto partenza']
    arrivalAirport = item['Aeroporto arrivo']
    departureTime = item['Orario partenza']
    arrivalTime = item['Orario arrivo']
    airline = item['Compagnia aerea']
    seats = item['Posti liberi']

    #update selected flight by adding a new instance with same id in DynamoDB database
    table.put_item(
	    Item = {
                'Id': flightId,
                'Data': date,
                'Aeroporto partenza': departureAirport,
                'Aeroporto arrivo': arrivalAirport,
                'Orario partenza': departureTime,
                'Orario arrivo': arrivalTime,
                'Compagnia aerea': airline,
                'Prezzo base': Decimal(newPrice),
                'Posti liberi': seats
	    }
    )



# ----------------------------------------------------- DISCOVERY --------------------------------------------
def discovery_management_micro(all_discovery_servers, logger):
    global ADDR_PORT
    ok = False
    while(True):
        """
        Itero sui discovery servers noti al microservizio
        per ottenere la porta ricercata.
        """
        for discovery in all_discovery_servers:
            try:
                # Provo a connettermi al Discovery server.
                channel = grpc.insecure_channel(discovery)
                stub = Discovery_pb2_grpc.DiscoveryServiceStub(channel)
                # Recupero la porta su cui è in ascolto il servizio di Management.
                res = stub.get(Discovery_pb2.GetRequest(serviceName="booking" , serviceNameTarget="management"))
            except:
                # Si è verificato un problema nella connessione con il discovery server
                logger.info('[ GET DISCOVERY MANAGEMENT] Problema connessione con il discovery server ' + discovery + '.')
                time.sleep(2)
                continue
            if (res.port == '-1'):
                logger.info('[ GET DISCOVERY MANAGEMENT] porta ancora non registrata dal discovery server ' + discovery + ' riprovare...')
                time.sleep(2)
                continue
            # Non ho avuto problemi di connsessione e la porta restituita è valida.
            ok = True
            logger.info('[ GET DISCOVERY MANAGEMENT] porta del servizio di management recuperata: ' + res.port + '.')
            ADDR_PORT = res.serviceName + ':' + res.port
            break
        if(ok):
            break
        logger.info('[ GET DISCOVERY MANAGEMENT ] Richiesta di GET avvenuta con insuccesso presso tutti i discovery servers...')
        time.sleep(5)
# ----------------------------------------------------- DISCOVERY --------------------------------------------




def retrieveAvailableSeats(idVolo, postiDisponibili):

    dynamodb = boto3.resource(DYNAMODB, REGIONE)
    table = dynamodb.Table(TABELLA_POSTI_OCCUPATI)

    """
    Ottengo le informazioni relative ai posti disponibili
    solamente per il volo richiesto. Poiché l'identificativo
    rappresenta la chiave primaria, allora ottengo una sola
    riga al più.
    """
    response = table.scan(FilterExpression=Attr('IdVolo').eq(idVolo))   

    """
    Il valore di items è una array che ha esattamente un elemento
    poiché l'identificativo del volo è la chiave primaria.
    """
    items = response['Items']

    """
    In questo scenario, si sta richiedendo di accedere ai posti disponibili
    per un volo che ha un identificativo che non è contenuto all'interno del
    database.
    """
    if(len(items)==0):
        return []
    
    #Estraggo il dizionario relativo alla riga
    row = items[0]
    keys = row.keys()

    """
    Tolgo dalla lista 'postiTotali' tutti i posti che non
    sono attualmente disponibili. Per fare ciò osservo che
    le chiavi del dizionario rappresenta i posti che sono
    attulmente occupati. Tuttavia, tra le chiavi abbiamo
    anche l'identificativo del volo. Di conseguenza, nel
    momento in cui il dizionario contiene solamente la chiave
    dell'identificativo del volo allora non ci sono posti che
    risultano essere occupati. L'iterazione relativa all'ID del
    volo la saltiamo poiché non rappresenta un posto.
    """
    for key in keys:
        if(row[key]==idVolo):
            # Non considero la chiave relativa all'identificativo del volo poiché non è un posto disponibile
            continue
        try:
            postiDisponibili.remove(key)
        except:
            print("[ECCEZIONE]: " + key)
    #Restituisco tutti e soli i posti attualmente disponibili
    return postiDisponibili




"""
Interroga il database Dynamodb per ottenere tutti
i voli disponibili per la data GG/MM/AAAA con la partenza e
l'arrivo che corrispondono ai dati passati in input.
"""
def retrieveFlights(giorno, mese, anno, partenza, arrivo, all_discovery_servers, logger):
    dynamodb = boto3.resource(DYNAMODB, REGIONE)
    table = dynamodb.Table(TABELLA_VOLO)

    response = table.scan(FilterExpression=Attr('Aeroporto partenza').eq(partenza) & Attr('Aeroporto arrivo').eq(arrivo) & Attr('Data').eq(getTwoDigitsString(str(giorno))+'-'+getTwoDigitsString(str(mese))+'-'+str(anno)))
    
    """
    La variabile items è una lista di dizionari fatta nel seguente modo:
    [{}, {}, ..., {}]
    """
    items = response['Items']
    
    idKey = ''
    compagnia_aerea = ''
    arrivo = ''
    partenza = ''
    data = ''
    orario = ''
    flights = []
    append = True
    
    #itero sui dizionari.
    for item in items:
        # Itero su tutte le coppie (key, value) del dizionario fissato.
        for key, value in item.items():
            if(key=='Id'):
                # Identificativo del volo
                idKey = value
            if(key=='Compagnia aerea'):
                # Compagnia aerea che offre il volo
                compagnia_aerea = value  
            if(key=='Aeroporto arrivo'):
                # Aeroporto di arrivo del volo
                arrivo = value
            if(key=='Aeroporto partenza'):
                # Aeroporto di partenza del volo
                partenza = value
            if(key=='Data'):
                # Data del volo
                data = value
            if(key=='Orario arrivo'):
                # Orario di arrivo del volo
                orario = value

            """
            Controllo se tutti le informazioni relative al volo
            su cui sto iterando sono state acquisite.
            """
            if(idKey!= '' and compagnia_aerea!='' and append and arrivo!='' and partenza!='' and data!='' and orario!=''):
                append = False
                flights.append(Flight(idKey, compagnia_aerea, arrivo, partenza, orario, data, -1, None))

        """
        Ripristino il valore delle variabili per
        poter iterare sul volo successivo.
        """
        idKey = ''
        compagnia_aerea = ''
        arrivo = ''
        partenza = ''
        data = ''
        orario = ''
        append = True

# -------------------------------- DISCOVERY -------------------------------------------------------------------
    if (ADDR_PORT == ''):
        # Recupero la porta su cui è in ascolto il microservizio di Management.
        discovery_management_micro(all_discovery_servers,logger)
# -------------------------------- DISCOVERY -------------------------------------------------------------------

    # La porta del microservizio di Management è stata recuperata con successo.
    channel = grpc.insecure_channel(ADDR_PORT)
    stub = Managment_pb2_grpc.FlightsInfoStub(channel)
    
    """
    Itero sui voli che sono stati recuperati per
    ottenere il prezzo base e i posti attulamente disponibili.
    """
    for flight in flights:
        response = stub.GetPriceFlight(Managment_pb2.PriceRequest(idVolo=flight.idKey))
        flight.prezzo = response.price
        copiaPostiTotali = postiTotali.copy()
        postiDisponibili = retrieveAvailableSeats(flight.idKey, copiaPostiTotali)
        flight.postiDisponibili = postiDisponibili

    return flights


"""
Restituisce tutti gli aeroporti di partenza che figurano nella tabella Volo.
"""
def retrieveDepartures():
    dynamodb = boto3.resource(DYNAMODB, REGIONE)
    table = dynamodb.Table(TABELLA_VOLO)

    departures = []     #la lista degli aeroporti di partenza da restituire al chiamante

    response = table.scan()

    """
    La variabile items è una lista di dizionari fatta nel seguente modo:
    [{}, {}, ..., {}]
    """
    items = response['Items']

    #itero sui dizionari.
    for item in items:
        #itero su tutte le coppie (key, value) del dizionario fissato.
        for key, value in item.items():
            #aggiungo l'aeroporto di partenza alla lista solo se non vi è già presente
            if(key=='Aeroporto partenza' and value not in departures):        
                departures.append(value)

    return departures


"""
Restituisce tutti gli aeroporti di arrivo che figurano nella tabella Volo.
"""
def retrieveArrivals():
    dynamodb = boto3.resource(DYNAMODB, REGIONE)
    table = dynamodb.Table(TABELLA_VOLO)

    arrivals = []     #la lista degli aeroporti di partenza da restituire al chiamante

    response = table.scan()

    """
    La variabile items è una lista di dizionari fatta nel seguente modo:
    [{}, {}, ..., {}]
    """
    items = response['Items']

    #itero sui dizionari.
    for item in items:
        #itero su tutte le coppie (key, value) del dizionario fissato.
        for key, value in item.items():
            #aggiungo l'aeroporto di arrivo alla lista solo se non vi è già presente
            if(key=='Aeroporto arrivo' and value not in arrivals):        
                arrivals.append(value)

    return arrivals
