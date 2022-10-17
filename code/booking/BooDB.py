import boto3
import grpc
from boto3.dynamodb.conditions import Attr
from decimal import *
from proto import Managment_pb2
from proto import Managment_pb2_grpc

ADDR_PORT = 'localhost:50052'   #server_IP_addr:port_num

#this function returns true if there is no item with the specified id (i.e. the specified primary key); it returns false otherwise
def isNewId(flightId):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Volo')

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
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Volo')
    
    #store an item in 'Utente' table in DynamoDB
    table.put_item(
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

def storeUpdatedFlight(flightId, newPrice):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Volo')

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

class Flight:
    def __init__(self, idKey, compagnia_aerea, arrivo, partenza, orario, data, prezzo):
        self.idKey = idKey
        self.compagnia_aerea = compagnia_aerea
        self.arrivo = arrivo
        self.partenza = partenza
        self.orario = orario
        self.data = data
        self.prezzo = prezzo




def retrieveAvailableSeats(idVolo, postiTotali):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('PostiOccupati')

    """
    Ottengo le informazioni relative ai posti disponibili
    solamente per il volo richiesto. Poiché l'identificativo
    rappresenta la chiave primaria, allora ottengo una sola
    riga al più.
    """
    response = table.scan(FilterExpression=Attr('IdVolo').eq(idVolo))   
    print(response)

    """
    Il valore di items è una array che ha esattamente un elemento
    poiché l'identificativo del volo è la chiave primaria.
    """
    items = response['Items']

    print(items)

    """
    In questo scenario, si sta richiedendo di accedere ai posti disponibili
    per un volo che ha un identificativo che non è contenuto all'interno del
    database.
    """
    if(len(items)==0):
        return []
    
    #Estraggo il dizionario relativo alla riga
    row = items[0]
    print(row)
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
            continue
        try:
            postiTotali.remove(key)
        except:
            print("[ECCEZIONE]: " + key)
        


    #Restituisco tutti e soli i posti attualmente disponibili
    return postiTotali



def retrieveFlights(giorno, mese, anno, partenza, arrivo, persone):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Volo')

    response = table.scan(FilterExpression=Attr('Aeroporto partenza').eq(partenza) & Attr('Aeroporto arrivo').eq(arrivo) & Attr('Data').eq(str(giorno)+'-'+str(mese)+'-'+str(anno)))
    
    items = response['Items']
    
    idKey = ''
    compagnia_aerea = ''
    arrivo = ''
    partenza = ''
    data = ''
    orario = ''
    flights = []
    append = True
    
    #itero sui dizionari
    for item in items:
        for key, value in item.items():
            if(key=='Id'):
                idKey = value
            if(key=='Compagnia aerea'):
                compagnia_aerea = value  
            if(key=='Aeroporto arrivo'):
                arrivo = value
            if(key=='Aeroporto partenza'):
                partenza = value
            if(key=='Data'):
                data = value
            if(key=='Orario arrivo'):
                orario = value
            if(idKey!= '' and compagnia_aerea!='' and append and arrivo!='' and partenza!='' and data!='' and orario!=''):
                append = False
                flights.append(Flight(idKey, compagnia_aerea, arrivo, partenza, orario, data, -1))

        idKey = ''
        compagnia_aerea = ''
        arrivo = ''
        partenza = ''
        data = ''
        orario = ''
        append = True

    print(flights)
    
    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    #create client stub
    stub = Managment_pb2_grpc.FlightsInfoStub(channel)
    
    for flight in flights:
        #print("CICLOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        response = stub.GetPriceFlight(Managment_pb2.PriceRequest(idVolo=flight.idKey))
        print(response.price)
        flight.prezzo = response.price

    #forse qua bisogna implementare la SAGA per ottenere i posti ancora disponibili per il volo
    return flights