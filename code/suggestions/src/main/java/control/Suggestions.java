package control;

import java.io.IOException;

import io.grpc.Server;
import io.grpc.ServerBuilder;

public class Suggestions {

    private static final int PORT = 50054;
    private Server server;

    public void start() throws IOException {

        server = ServerBuilder.forPort(PORT).addService(new Service()).build().start();
        System.out.println("Starting server. Listening on port " + server.getPort() + ".");
    
    }

    public void blockUntilShutdown() throws InterruptedException {

        if(server != null) {
            server.awaitTermination();
        }
         
    }

    public static void main(String[] args) throws IOException, InterruptedException {

        Suggestions server = new Suggestions();
        server.start();
        server.blockUntilShutdown();

    }

}
