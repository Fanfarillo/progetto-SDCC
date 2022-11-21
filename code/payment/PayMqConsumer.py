import pika, os, sys, time

retValue = False

def receiveMqBooking(logger):
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

    channel.queue_declare(queue='booProducer')


    def callback(ch, method, properties, body):
        logger.info("[MESSAGE QUEUE] Ricevuto %r." % body)

        """
        receiveMqBooking() restituirà True se e solo se il body del messaggio ricevuto è "True",
        ovvero se e solo se la porzione del pattern Saga riguardante Booking è andata a buon fine
        """
        if body.decode("utf-8") == "True":
            retValue = True
        channel.stop_consuming()
        

    #consume queued message
    channel.basic_consume(queue='booProducer', on_message_callback=callback, auto_ack=True)

    logger.info("[MESSAGE QUEUE] In attesa di messaggi da parte di Booking...")
    channel.start_consuming()

    return retValue
