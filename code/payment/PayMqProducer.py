import pika, os

def sendMqBooking(idVolo, username, selectedSeatsStr, logger):
    amqpUrl = os.environ['AMQP_URL']
    parameters = pika.URLParameters(amqpUrl)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='payProducer')

    #produce message
    channel.basic_publish(exchange='', routing_key='payProducer', body=idVolo+"\n"+username+"\n"+selectedSeatsStr)
    logger.info("Inviato un messaggio a Booking mediante la coda di messaggi.")
    connection.close()
