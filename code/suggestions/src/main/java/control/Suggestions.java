package control;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import io.grpc.Server;
import io.grpc.ServerBuilder;

import utils.LogUtil;
import utils.DiscovUtil;

public class Suggestions {

    private static final int PORT = 50055;
    private static final String SUGGESTIONS_1 = "code_suggestions_1";
    private static final String SUGGESTIONS_2 = "code_suggestions_2";

    public static String ownIpAddress;      //conterrà l'indirizzo IP del container
    public static String suggestions1;
    public static String suggestions2;      //suggestions1 e suggestions2 conterranno gli indirizzi IP di entrambe le copie di Suggestions

    private Server server;

    /* La seguente lista inizialmente contiene solo il default discovery server per il microservizio di Suggestions.
     * Tuttavia, nel momento in cui si registra, all'interno possono essere inserite le informazioni relative all'altro discovery server. */
    private static List<String> allDiscoveryServers;


    public void start() throws IOException {
        server = ServerBuilder.forPort(PORT).addService(new Service()).build().start();
    }


    public void blockUntilShutdown() throws InterruptedException {

        if(server != null) {
            server.awaitTermination();
        }
         
    }


    public static void main(String[] args) throws Exception {

        LogUtil opfile = LogUtil.getInstance();     //ottenimento del file di log

        //--------------------------------------- INIZIO CODICE CHE GESTISCE LE REPLICAZIONE DI SUGGESTIONS -------------------------------------------------

        if(args.length != 3) {
            opfile.writeLog("[ERROR] È richiesto il passaggio di 3 parametri da linea di comando.");
            System.exit(1);
        }

        ownIpAddress = args[0];             //indirizzo IP del container
        suggestions1 = args[1];
        suggestions2 = args[2];             //suggestions1 e suggestions2 sono gli indirizzi IP di entrambe le copie di Suggestions
        String otherSuggestions = null;     //nome dell'altro container (dell'altra copia di Suggestions)

        //identificazione del nome del container
        if(ownIpAddress.equals(suggestions1)) {
            //qui il container ha nome SUGGESTIONS_1 e dovrà quindi contattare SUGGESTIONS_2; SUGGESTIONS_1 è la copia primaria di Suggestions
            otherSuggestions = SUGGESTIONS_2;
            opfile.writeLog("[SETUP NOME DEL CONTAINER] " + SUGGESTIONS_1 + "\t" + suggestions1 + "\n");
        }
        else {
            //qui il container ha nome SUGGESTIONS_2 e dovrà quindi ricevere i dati da SUGGESTIONS_1; SUGGESTIONS_2 è la copia secondaria di Suggestions
            otherSuggestions = SUGGESTIONS_1;
            opfile.writeLog("[SETUP NOME DEL CONTAINER] " + SUGGESTIONS_2 + "\t" + suggestions2 + "\n");            
        }

        if(otherSuggestions==null) {
            opfile.writeLog("[FATAL] Errore nella risoluzione dell'indirizzo IP del discovery server.");
            System.exit(1);
        }

        //--------------------------------------- FINE CODICE CHE GESTISCE LE REPLICAZIONE DI SUGGESTIONS -------------------------------------------------

        //avvio del server RPC
        Suggestions server = new Suggestions();
        opfile.writeLog("Avvio del server in ascolto sulla porta 50055...");
        server.start();
        opfile.writeLog("Server avviato con successo.");

        //--------------------------------------- DISCOVERY -------------------------------------------------

        /* Registrazione del microservizio al Discovery Server di default; inizialmente il microservizio è a conoscenza solo del discovery server 2. 
         * Per giunta, solo la copia primaria di Suggestions si renderà disponibile ad accettare richieste di connessione da parte degli altri servizi,
         * dunque solo lei si registra al discovery service. L'altra copia, invece, rimane solo in attesa di ricevere aggiornamenti da parte della primaria.
         */
        if(ownIpAddress.equals(suggestions1)) {

            allDiscoveryServers = new ArrayList<>();
            allDiscoveryServers.add("discovery:50060");
            opfile.writeLog("[DISCOVERY SERVER] Richiesta registrazione del microservizio sul discovery server...");
            List<String> discoveryServers = DiscovUtil.putDiscoveryServer(allDiscoveryServers, opfile);
            opfile.writeLog("[DISCOVERY SERVER] Registrazione del microservizio sul discovery server " + allDiscoveryServers.get(0) + " avvenuta con successo.");

            //registro l'eventuale altro discovery server
            for(String item : discoveryServers) {
                if(!allDiscoveryServers.contains(item))
                    allDiscoveryServers.add(item);
            
            }

            opfile.writeLog("[DISCOVERY SERVER LIST] I discovery server noti sono:\n");
            for(String item : allDiscoveryServers) {
                opfile.writeLog(item + "\n");
            }
            opfile.writeLog("\n\n");

        } 

        //--------------------------------------- DISCOVERY -------------------------------------------------

        server.blockUntilShutdown();

    }

}
