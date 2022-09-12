package server;

import java.io.IOException;

import io.grpc.Server;
import io.grpc.ServerBuilder;

public class MicroServer {

    private static final int PORT = 50051;
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

        MicroServer server = new MicroServer();
        server.start();
        server.blockUntilShutdown();

    }

}
