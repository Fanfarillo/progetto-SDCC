package control;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import io.grpc.Server;
import io.grpc.ServerBuilder;

import utils.LogUtil;
import utils.DiscovUtil;

public class Suggestions {

    private static final int PORT = 50054;
    private Server server;
    /* La seguente lista inizialmente contiene solo il default discovery server per il microservizio di Suggestions.
     * Tuttavia, nel momento in cui si registra, all'interno possono essere inserite le informazioni relative all'altro discovery server. */
    private List<String> allDiscoveryServers;

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

        //--------------------------------------- DISCOVERY -------------------------------------------------

        //registrazione del microservizio al Discovery Server di default; inizialmente il microservizio è a conoscenza solo del discovery server 2
        allDiscoveryServers = new ArrayList<>();
        allDiscoveryServers.add("code_discovery_2:50060");
        opfile.writeLog("[DISCOVERY SERVER] Richiesta registrazione del microservizio sul discovery server...");
        List<String> discoveryServers = DiscovUtil.putDiscoveryServer(allDiscoveryServers, opfile);
        opfile.writeLog("[DISCOVERY SERVER] Registazione del microservizio sul discovery server " + allDiscoveryServers.get(0) + " avvenuta con successo.");

        //registro l'eventuale altro discovery server
        for(String item : discoveryServers) {
            if(!allDiscoveryServers.contains(item))
                allDiscoveryServers.add(item);
            
        }

        opfile.writeLog("[DISCOVERY SERVER LIST] I discovery server noti sono:\n");
        for(String item in allDiscoveryServers) {
            opfile.writeLog(item + "\n");
        }
        opfile.writeLog("\n\n");

        //--------------------------------------- DISCOVERY -------------------------------------------------

        server.blockUntilShutdown();

    }

}
