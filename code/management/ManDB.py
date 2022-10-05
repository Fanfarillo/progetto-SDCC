import boto3

from decimal import *

def storeSeatsPrices(airline, price1, price2, price6, price16, price18):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('PrezzoPosti')
    
    #store an item in 'Utente' table in DynamoDB
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
