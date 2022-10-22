package control;

import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;
import com.rabbitmq.client.DeliverCallback;

public class MsgConsumer {

    private final static String QUEUE_NAME = "past_flights";

    public static void main(String[] argv) throws Exception {

        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        Connection connection = factory.newConnection();
        Channel channel = connection.createChannel();

        channel.queueDeclare(QUEUE_NAME, false, false, false, null);
        System.out.println(" [*] Waiting for messages. To exit press CTRL+C");

        //consume queued messages; I guess each message corresponds to a specific flight
        DeliverCallback deliverCallback = (consumerTag, delivery) -> {
            String message = new String(delivery.getBody(), "UTF-8");
            System.out.println(" [x] Received '" + message + "'");
            PopulateArff.storeNewData(message);     //questa funzione aggiunge dati al training set (e, in particolare, al file Train.arff)
        };
        channel.basicConsume(QUEUE_NAME, true, deliverCallback, consumerTag -> { });

  }

}
