import boto3
from decimal import *


DYNAMODB = 'dynamodb'
REGIONE = 'us-east-1'


def storePayment(idVolo, postiSelezionati, username, dataPagamento, prezzoBase, prezzoSelezionePosti, prezzoServiziAggiuntivi, prezzoTotale, numStivaMedi, numStivaGrandi, numBagagliSpeciali, numAssicurazioni, numAnimali, numNeonati, email):
    dynamodb = boto3.resource(DYNAMODB, REGIONE)
    table = dynamodb.Table('Pagamento')
    
    #store an item in 'Pagamento' table in DynamoDB
    table.put_item(
        Item = {
            'IdVolo': idVolo,
            'PostiSelezionati': postiSelezionati,
            'Username': username,
            'DataPagamento': dataPagamento,
            'PrezzoBase': prezzoBase,
            'PrezzoSelezionePosti': prezzoSelezionePosti,
            'PrezzoServiziAggiuntivi': prezzoServiziAggiuntivi,
            'PrezzoTotale': prezzoTotale,
            'NumStivaMedi': numStivaMedi,
            'NumStivaGrandi': numStivaGrandi,
            'NumBagagliSpeciali': numBagagliSpeciali,
            'NumAssicurazioni': numAssicurazioni,
            'NumAnimali': numAnimali,
            'NumNeonati': numNeonati,
            'Email': email
        }
    )

def deletePayment(idVolo, postiSelezionati):
    dynamodb = boto3.resource(DYNAMODB, REGIONE)
    table = dynamodb.Table('Pagamento')

    #delete an item from 'Pagamento' table in DynamoDB
    table.delete_item(
        TableName='Pagamento',
        Key={
            'IdVolo': idVolo,
            'PostiSelezionati': postiSelezionati
        }
    )
