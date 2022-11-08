package control;

import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;
import com.rabbitmq.client.DeliverCallback;

import utils.LogUtil;

public class MsgConsumer {

    private final static String QUEUE_NAME = "past_flights";

    public static void main(String[] argv) throws Exception {

        LogUtil opfile = new LogUtil();
        opfile.createLog();                 //creazione del file di log

        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        Connection connection = factory.newConnection();
        Channel channel = connection.createChannel();

        channel.queueDeclare(QUEUE_NAME, false, false, false, null);
        opfile.writeLog(" [*] La message queue è in attesa di messaggi.");

        //consume queued messages; I guess each message corresponds to a specific flight
        DeliverCallback deliverCallback = (consumerTag, delivery) -> {
            String message = new String(delivery.getBody(), "UTF-8");
            opfile.writeLog(" [x] Ricevuto il messaggio '" + message + "'");
            PopulateArff.storeNewData(message);     //questa funzione aggiunge dati al training set (e, in particolare, al file Train.arff)
        };
        channel.basicConsume(QUEUE_NAME, true, deliverCallback, consumerTag -> { });

  }

}
