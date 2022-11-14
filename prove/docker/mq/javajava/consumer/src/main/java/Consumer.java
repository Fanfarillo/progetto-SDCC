import java.util.Map;
import java.net.*;

import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;
import com.rabbitmq.client.DeliverCallback;

public class Consumer {

    private final static String QUEUE_NAME = "hello";

    public static void main(String[] argv) throws Exception {

        Map<String, String> env = System.getenv();
        String amqpUrl = env.get("AMQP_URL");
        InetAddress amqpIp = InetAddress.getByName((URI.create(amqpUrl)).toURL().getHost());
        String amqpIpString = amqpIp.getHostAddress();

        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost(amqpIpString);

        Connection connection = factory.newConnection();
        Channel channel = connection.createChannel();

        channel.queueDeclare(QUEUE_NAME, false, false, false, null);
        System.out.println(" [*] Waiting for messages. To exit press CTRL+C");

        //consume queued messages
        DeliverCallback deliverCallback = (consumerTag, delivery) -> {
            String message = new String(delivery.getBody(), "UTF-8");
            System.out.println(" [x] Received '" + message + "'");
        };
        channel.basicConsume(QUEUE_NAME, true, deliverCallback, consumerTag -> { });

  }

}
