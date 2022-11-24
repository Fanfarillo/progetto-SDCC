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
            logger.info('[MESSAGE QUEUE ERROR] Errore connessione RabbitMQ.')

    channel.queue_declare(queue='booProducer')


    def callback(ch, method, properties, body):
        global retValue       #impone che il retValue che utilizziamo in questa funzione è proprio la variabile globale e non una nuova variabile locale
        bodyStr = body.decode("utf-8")
        logger.info("[MESSAGE QUEUE] Ricevuto %s da parte di Booking." % bodyStr)

        """
        receiveMqBooking() restituirà True se e solo se il body del messaggio ricevuto è "True",
        ovvero se e solo se la porzione del pattern Saga riguardante Booking è andata a buon fine
        """
        if bodyStr == 'True':
            retValue = True
        channel.stop_consuming()
        

    #consume queued message
    channel.basic_consume(queue='booProducer', on_message_callback=callback, auto_ack=True)

    logger.info("[MESSAGE QUEUE] In attesa di messaggi da parte di Booking...")
    channel.start_consuming()

    logger.info("[MESSAGE QUEUE] Restituisco l'esito della transazione saga al frontend.")
    return retValue
