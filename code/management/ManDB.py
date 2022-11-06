import boto3

from boto3.dynamodb.conditions import Attr
from decimal import *



DYNAMODB = 'dynamodb'
REGIONE = 'us-east-1'



def getAllSeatsFlight(compagnia):
    dynamodb = boto3.resource(DYNAMODB, REGIONE)
    table = dynamodb.Table('PrezzoPosti')

    response = table.scan(FilterExpression=Attr('Compagnia').eq(compagnia))
    # Prezzo dei posti nella fila 1
    primo = response['Items'][0]['1']
    # Prezzo dei posti nelle file 2-5
    secondo = response['Items'][0]['2-5']
    # Prezzo dei posti nelle file 6-15
    terzo = response['Items'][0]['6-15']
    # Prezzo dei posti nelle file 16-17
    quarto = response['Items'][0]['16-17']
    # Prezzo dei posti nelle file 18-26
    quinto = response['Items'][0]['18-26']

    prezzi = []
    prezzi.append(primo)
    prezzi.append(secondo)
    prezzi.append(terzo)
    prezzi.append(quarto)
    prezzi.append(quinto)

    return prezzi



def getAlladditionalServicesFlight(compagnia):
    dynamodb = boto3.resource(DYNAMODB, REGIONE)
    table = dynamodb.Table('Servizi')
    response = table.scan(FilterExpression=Attr('Compagnia').eq(compagnia))

    bagaglioSpeciale = response['Items'][0]['Bagaglio speciale']
    bagaglioStivaMedio = response['Items'][0]['Bagaglio in stiva medio']
    bagaglioStivaGrande = response['Items'][0]['Bagaglio in stiva grande']
    assicurazioneBagagli = response['Items'][0]['Assicurazione bagagli']
    animaleDomestico = response['Items'][0]['Animale domestico']
    neonato = response['Items'][0]['Neonato']

    prezzi = []
    prezzi.append(bagaglioSpeciale)
    prezzi.append(bagaglioStivaMedio)
    prezzi.append(bagaglioStivaGrande)
    prezzi.append(assicurazioneBagagli)
    prezzi.append(animaleDomestico)
    prezzi.append(neonato)

    return prezzi



def storeSeatsPrices(airline, price1, price2, price6, price16, price18):
    dynamodb = boto3.resource(DYNAMODB, REGIONE)
    table = dynamodb.Table('PrezzoPosti')
    
    #store (actually update) an item in 'PrezzoPosti' table in DynamoDB
    table.put_item(
        Item = {
            'Compagnia': airline,
            '1': Decimal(price1),
            '2-5': Decimal(price2),
            '6-15': Decimal(price6),
            '16-17': Decimal(price16),
            '18-26': Decimal(price18)
        }
    )



def storeServicesPrices(airline, priceBM, priceBG, priceBS, priceAD, priceAB, priceTN):
    dynamodb = boto3.resource(DYNAMODB, REGIONE)
    table = dynamodb.Table('Servizi')

    #store (actually update) an item in 'Servizi' table in DynamoDB
    table.put_item(
        Item = {
            'Compagnia': airline,
            'Bagaglio in stiva medio': Decimal(priceBM),
            'Bagaglio in stiva grande': Decimal(priceBG),
            'Bagaglio speciale': Decimal(priceBS),
            'Animale domestico': Decimal(priceAD),
            'Assicurazione bagagli': Decimal(priceAB),
            'Neonato': Decimal(priceTN)
        }
    )



def getPrice(idVolo):
    dynamodb = boto3.resource(DYNAMODB, REGIONE)
    table = dynamodb.Table('Volo')

    response = table.scan(FilterExpression=Attr('Id').eq(idVolo))
    return response['Items'][0]['Prezzo base']
