import pika, os, sys, time

from BooUtils import *
from BooDB import *

class MqChannels:

    def __init__(self, channel, logger):
        #canale a cui verranno collegate entrambe le code di messaggi
        self.channel = channel
        #logger
        self.logger = logger


    def receiveMqPayment(self):

        def callback(ch, method, properites, body):
            self.logger.info('[MESSAGE QUEUE] Ricevuto %r.' % body)
            bodyStr = body.decode("utf-8")      #conversione del body da binario a stringa

            #conversione del body del messaggio ricevuto nelle variabili idVolo (stringa), username (stringa) e selectedSeats (lista di stringhe)
            idVolo = getIdFromMsg(bodyStr)
            username = getUsernameFromMsg(bodyStr)
            selectedSeats = getSeatsFromMsg(bodyStr)

            msg = "False"       #body del messaggio da inviare a Payment

            #salvataggio nel db delle informazioni relative ai posti occupati; il valore di ritorno indica se la transazione complessa è andata a buon fine
            isOk = storeSelectedSeats(idVolo, username, selectedSeats, self.logger)           
            if isOk==True:
                msg = "True"

            #invio della risposta a Payment sull'altra coda di messaggi
            self.channel.basic_publish(exchange='', routing_key='booProducer', body=msg)
            self.logger.info('[MESSAGE QUEUE] Inviato un messaggio di risposta a Payment mediante la coda di messaggi.')
            #lascio la connessione aperta perché in futuro potrebbe essere necessario di inviare altri messaggi di risposta


        #consume queued messages
        self.channel.basic_consume(queue='payProducer', on_message_callback=callback, auto_ack=True)
    
        self.logger.info('[MESSAGE QUEUE] In attesa di messaggi da parte di Payment...')
        self.channel.start_consuming()




def defineQueues(logger):
    logger.info('Thread associato alle code di messaggi creato con successo.')

    while(True):
        try:
            amqpUrl = os.environ['AMQP_URL']
            parameters = pika.URLParameters(amqpUrl)
            connection = pika.BlockingConnection(parameters)
            channel = connection.channel()
            logger.info('[MESSAGE QUEUE] Connessione con RabbitMQ riuscita.')
            break
        except:
            time.sleep(2)
            logger.info('[MESSAGE QUEUE ERROR] Errore connessione RabbitMQ')

    channel.queue_declare(queue='payProducer')
    channel.queue_declare(queue='booProducer')

    mq = MqChannels(channel, logger)
    mq.receiveMqPayment()               #questa funzione lascia il thread in uno stato di blocco perenne tramite il metodo start_consuming()
