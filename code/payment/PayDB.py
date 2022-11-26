import boto3
from decimal import *


DYNAMODB = 'dynamodb'
REGIONE = 'us-east-1'
TABELLA_PAGAMENTO = 'Pagamento'


def storePayment(idVolo, postiSelezionati, username, dataPagamento, prezzoBase, prezzoSelezionePosti, prezzoServiziAggiuntivi, prezzoTotale, numStivaMedi, numStivaGrandi, numBagagliSpeciali, numAssicurazioni, numAnimali, numNeonati, email):
    dynamodb = boto3.resource(DYNAMODB, REGIONE)
    table = dynamodb.Table(TABELLA_PAGAMENTO)
    
    #store an item in 'Pagamento' table in DynamoDB
    table.put_item(
        Item = {
            'IdVolo': idVolo,
            'Posti': postiSelezionati,
            'Username': username,
            'Data pagamento': dataPagamento,
            'Prezzo base': prezzoBase,
            'Prezzo selezione posti': prezzoSelezionePosti,
            'Prezzo servizi aggiuntivi': prezzoServiziAggiuntivi,
            'Prezzo totale': prezzoTotale,
            'Num stiva medi': numStivaMedi,
            'Num stiva grandi': numStivaGrandi,
            'Num bagagli speciali': numBagagliSpeciali,
            'Num assicurazioni': numAssicurazioni,
            'Num animali': numAnimali,
            'Num neonati': numNeonati,
            'Email': email
        }
    )

def deletePayment(idVolo, postiSelezionati):
    dynamodb = boto3.resource(DYNAMODB, REGIONE)
    table = dynamodb.Table(TABELLA_PAGAMENTO)

    #delete an item from 'Pagamento' table in DynamoDB
    table.delete_item(
        TableName=TABELLA_PAGAMENTO,
        Key={
            'IdVolo': idVolo,
            'Posti': postiSelezionati
        }
    )
