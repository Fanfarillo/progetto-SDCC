import pika, os, sys

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
                logger.info('[MESSAGE QUEUE] Ricevuto %r.' % body)

                #invio della risposta a Payment sull'altra coda di messaggi
                #TODO


        #consume queued messages
        channelC.basic_consume(queue='payProducer', on_message_callback=callback, auto_ack=True)
    
        logger.info('[MESSAGE QUEUE] In attesa di messaggi da parte di Payment...')
        channelC.start_consuming()




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
    mq.receiveMqPayment()
