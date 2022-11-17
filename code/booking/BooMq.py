import pika, os, sys

from BooUtils import *
from BooDB import *

class MqChannels:

    def __init__(self, channelC, channelP, logger):
        #canale in cui Booking consumerà
        self.channelC = channelC
        #canale su cui Booking invierà messaggi
        self.channelP = channelP
        #logger
        self.logger = logger


        def receiveMqPayment(self):

            def callback(ch, method, properites, body):
                self.logger.info('[MESSAGE QUEUE] Ricevuto %r.' % body)

                #conversione del body del messaggio ricevuto nelle variabili idVolo (stringa), username (stringa) e selectedSeats (lista di stringhe)
                idVolo = getIdFromMsg(body)
                username = getUsernameFromMsg(body)
                selectedSeats = getSeatsFromMsg(body)

                #salvataggio nel db delle informazioni relative ai posti occupati; il valore di ritorno indica se la transazione complessa è andata a buon fine
                isOk = storeSelectedSeats(idVolo, username, selectedSeats, this.logger)
                msg = "False"       #body del messaggio da inviare a Payment
                if msg==True:
                    msg = "True"

                #invio della risposta a Payment sull'altra coda di messaggi
                self.channelP.basic_publish(exchange='', routing_key='booProducer', body=msg)
                self.logger.info('[MESSAGE QUEUE] Inviato un messaggio di risposta a Payment mediante la coda di messaggi.')
                #lascio la connessione aperta perché in futuro potrebbe essere necessario di inviare altri messaggi di risposta


            #consume queued messages
            self.channelC.basic_consume(queue='payProducer', on_message_callback=callback, auto_ack=True)
    
            self.logger.info('[MESSAGE QUEUE] In attesa di messaggi da parte di Payment...')
            self.channelC.start_consuming()




def defineQueues(logger):
    logger.info('Thread associato alle code di messaggi creato con successo.')

    amqpUrl = os.environ['AMQP_URL']
    parameters = pika.URLParameters(amqpUrl)
    connection = pika.BlockingConnection(parameters)
    channelC = connection.channel()     #consumer channel
    channelP = connection.channel()     #producer channel

    channelC.queue_declare(queue='payProducer')
    channelP.queue_declare(queue='booProducer')

    mq = MqChannels(channelC, channelP, logger)
    mq.receiveMqPayment()               #questa funzione lascia il thread in uno stato di blocco perenne tramite il metodo start_consuming()
