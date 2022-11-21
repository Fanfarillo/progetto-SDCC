import pika, os, time

def sendMqBooking(idVolo, username, selectedSeatsStr, logger):
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

    #produce message
    channel.basic_publish(exchange='', routing_key='payProducer', body=idVolo+"\n"+username+"\n"+selectedSeatsStr)
    logger.info("Inviato un messaggio a Booking mediante la coda di messaggi.")
    connection.close()
