import java.util.Map;
import java.net.*;
import java.nio.charset.StandardCharsets;

import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;

public class Producer {

    private final static String QUEUE_NAME = "hello";

    public static void main(String[] argv) throws Exception {

        Map<String, String> env = System.getenv();
        String amqpUrl = env.get("AMQP_URL");
        InetAddress amqpIp = InetAddress.getByName((URI.create(amqpUrl)).toURL().getHost());
        String amqpIpString = amqpIp.getHostAddress();

        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost(amqpIpString);

        try (Connection connection = factory.newConnection();
             Channel channel = connection.createChannel()) {

            channel.queueDeclare(QUEUE_NAME, false, false, false, null);
            String message = "Hello World!";

            //produce message
            channel.basicPublish("", QUEUE_NAME, null, message.getBytes(StandardCharsets.UTF_8));
            System.out.println(" [x] Sent '" + message + "'");

        }
    }
}
