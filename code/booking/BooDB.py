import boto3
from boto3.dynamodb.conditions import Attr
from decimal import *

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
    response = table.getItem(
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
    def __init__(self, idKey, compagnia_aerea, arrivo, partenza, orario, data):
        self.idKey = idKey
        self.compagnia_aerea = compagnia_aerea
        self.arrivo = arrivo
        self.partenza = partenza
        self.orario = orario
        self.data = data


def retrieveFlights(giorno, mese, anno, partenza, arrivo, persone):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Volo')

    response = table.scan(FilterExpression=Attr('Aeroporto partenza').eq(partenza) & Attr('Data').eq(str(giorno)+'-'+str(mese)+'-'+str(anno)))
    
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
                flights.append(Flight(idKey, compagnia_aerea, arrivo, partenza, orario, data))

        idKey = ''
        compagnia_aerea = ''
        arrivo = ''
        partenza = ''
        data = ''
        orario = ''
        append = True

    print(flights)
    
    return flights