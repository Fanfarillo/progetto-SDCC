package control;

import java.io.IOException;

import io.grpc.Server;
import io.grpc.ServerBuilder;

import utils.LogUtil;

public class Suggestions {

    private static final int PORT = 50054;
    private Server server;

    public void start() throws IOException {
        server = ServerBuilder.forPort(PORT).addService(new Service()).build().start();
    }

    public void blockUntilShutdown() throws InterruptedException {

        if(server != null) {
            server.awaitTermination();
        }
         
    }

    public static void main(String[] args) throws Exception {

        LogUtil opfile = new LogUtil();
        opfile.createLog();     //creazione del file di log

        Suggestions server = new Suggestions();
        opfile.writeLog("Avvio del server in ascolto sulla porta 50054...");

        server.start();
        opfile.writeLog("Server avviato con successo.");
        server.blockUntilShutdown();

    }

}
