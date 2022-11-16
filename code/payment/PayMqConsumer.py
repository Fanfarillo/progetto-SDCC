import pika, os, sys

def receiveMqBooking(logger):
    amqpUrl = os.environ['AMQP_URL']
    parameters = pika.URLParameters(amqpUrl)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='booProducer')

    def callback(ch, method, properties, body):
        #TODO: trovare un modo per restituire il body al chiamante
        channel.stop_consuming()

    #consume queued message
    channel.basic_consume(queue='booProducer', on_message_callback=callback, auto_ack=True)

    logger.info("[MESSAGE QUEUE] In attesa di messaggi da parte di Booking.")
    channel.start_consuming()
