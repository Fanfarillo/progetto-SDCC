package utils;

import java.util.concurrent.TimeUnit;
import java.util.ArrayList;
import java.util.List;

import io.grpc.StatusRuntimeException;
import io.grpc.Channel;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;

import control.proto.*;

import control.proto.DiscoveryServiceGrpc.DiscoveryServiceBlockingStub;
import control.proto.DiscoveryServiceGrpc.DiscoveryServiceStub;

public class DiscovUtil {

    private final DiscoveryServiceBlockingStub blockingStub;
    private final DiscoveryServiceStub asyncStub;

    public DiscovUtil(Channel channel) {
        blockingStub = DiscoveryServiceGrpc.newBlockingStub(channel);
        asyncStub = DiscoveryServiceGrpc.newStub(channel);
    }

    public PutReply getReply(String serviceName, String port) throws Exception {
        PutRequest input = PutRequest.newBuilder().setServiceName(serviceName).setPort(port).build();
        PutReply output = blockingStub.put(input);
        return output;

    }

    public static List<String> putDiscoveryServer(List<String> discoveryServers, LogUtil opfile) throws Exception {
        
        List<String> newDiscoveryServers = new ArrayList<>();
        PutReply res;   //risultato ottenuto dal server gRPC (il discovery server)

        /* Si tenta di contattare il discovery server registrato per memorizzare la porta su cui il servizio di Suggestions è in ascolto.
         * Se le chiamate dovessero fallire, si attendono 5 secondi per poi eseguire nuovamente il tentativo di connessione. */
        boolean ok = false;
        while(true) {
            //itero sui discovery server noti
            for(String discoveryServer : discoveryServers) {

                //EQUIVALENTE DI: channel = grpc.insecure_channel(discovery_server)
                ManagedChannel channel = ManagedChannelBuilder.forTarget(discoveryServer).usePlaintext().build();

                try {
                    //EQUIVALENTE DI: stub = Discovery_pb2_grpc.DiscoveryServiceStub(channel)
                    DiscovUtil client = new DiscovUtil(channel);

                    //EQUIVALENTE DI: res = stub.put(Discovery_pb2.PutRequest(serviceName="suggestions", port="50055"))
                    res = client.getReply("code_suggestions_1", "50055");    //ATTENZIONE: è code_suggestions_1 perché trattasi della copia primaria del servizio

                }
                catch(Exception e) {        //si va qui se si è verificato un problema nella connessione con il discovery server
                    opfile.writeLog("[PUT DISCOVERY REGISTRATION] Problema connessione con il discovery server " + discoveryServer + ".");
                    Thread.sleep(2000);     //2 seconds sleep
                    continue;

                }
                finally {
                    channel.shutdownNow().awaitTermination(5, TimeUnit.SECONDS);
                }

                if(!res.getResult()) {      //si va qui se si è verificato un problema con DynamoDB
                    opfile.writeLog("[PUT DISCOVERY REGISTRATION] Problema DynamoDB con il discovery server " + discoveryServer + ".");
                    Thread.sleep(2000);     //2 seconds sleep
                    continue;

                }

                int i=0;    //indice per i server in DiscoveryServers
                while(true) {
                    String server = res.getListServer().getServers(i);
                    if(server==null)
                        break;

                    newDiscoveryServers.add(server);
                    i++;

                }

                ok = true;
                opfile.writeLog("[PUT DISCOVERY REGISTRATION] Registrazione avvenuta con successo presso il discovery server " + discoveryServer + ".");
                break;

            }

            if(ok)
                break;

            opfile.writeLog("[PUT DISCOVERY REGISTRATION] Registrazione avvenuta con insuccesso presso tutti i discovery server.");
            Thread.sleep(5000);     //5 seconds sleep

        }

        return newDiscoveryServers;     

    }

}
