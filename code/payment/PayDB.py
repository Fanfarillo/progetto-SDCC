import boto3
import logging

from decimal import *


DYNAMODB = 'dynamodb'
REGIONE = 'us-east-1'
TABELLA_PAGAMENTO = 'Pagamento'


def storePayment(idVolo, postiSelezionati, username, dataPagamento, prezzoBase, prezzoSelezionePosti, prezzoServiziAggiuntivi, prezzoTotale, numStivaMedi, numStivaGrandi, numBagagliSpeciali, numAssicurazioni, numAnimali, numNeonati, email, logger):
    dynamodb = boto3.resource(DYNAMODB, REGIONE)
    table = dynamodb.Table(TABELLA_PAGAMENTO)

    #controllo se esiste già un elemento con i valori di idVolo e postiSelezionati dati dai parametri in input; se sì, la put_item non verrà invocata
    response = table.get_item(
        Key = {
            'IdVolo': idVolo,
            'Posti': postiSelezionati            
        }
    )

    if not 'Item' in response:
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

    else:
        logger.info("Impossibile aggiungere il pagamento dell'utente " + username + " per il volo " + idVolo + ".")



def deletePayment(idVolo, postiSelezionati, username, logger):
    dynamodb = boto3.resource(DYNAMODB, REGIONE)
    table = dynamodb.Table(TABELLA_PAGAMENTO)

    """
    Controllo se l'elemento con i valori di idVolo e postiSelezionati dati dai parametri in input ha anche il campo Username pari allo username passato
    in input; in tal caso si procede all'eliminazione dell'elemento dalla tabella; altrimenti, vuol dire che l'elemento è relativo al pagamento di un
    altro utente e non va eliminato.
    """
    response = table.get_item(
        Key = {
            'IdVolo': idVolo,
            'Posti': postiSelezionati            
        }
    )

    if 'Item' in response:
        item = response['Item']
        retrievedUsername = item['Username']    
    
        if retrievedUsername == username:
            #delete an item from 'Pagamento' table in DynamoDB
            table.delete_item(
                TableName=TABELLA_PAGAMENTO,
                Key={
                    'IdVolo': idVolo,
                    'Posti': postiSelezionati
                }
            )
        else:
            logger.info("Impossibile eliminare il pagamento dell'utente " + username + " per il volo " + idVolo + " poiché non esiste.")

    else:
        logger.info("Impossibile eliminare il pagamento dell'utente " + username + " per il volo " + idVolo + " poiché non esiste.")
