import boto3
from boto3.dynamodb.conditions import Attr
from decimal import *

def storeSeatsPrices(airline, price1, price2, price6, price16, price18):
    dynamodb = boto3.resource('dynamodb')
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
    dynamodb = boto3.resource('dynamodb')
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
    print(idVolo)
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Volo')

    response = table.scan(FilterExpression=Attr('Id').eq(idVolo))

    print(response['Items'][0]['Prezzo base'])
    return response['Items'][0]['Prezzo base']
