package utils;

import utils.proto.DiscoveryServiceGrpc.DiscoveryServiceBlockingStub;
import utils.proto.DiscoveryServiceGrpc.DiscoveryServiceStub;

public class DiscovUtil {

    private final DiscoveryServiceBlockingStub blockingStub;
    private final DiscoveryServiceStub asyncStub;

    public DiscovUtil(Channel channel) {
        blockingStub = DiscoveryServiceGrpc.newBlockingStub(channel);
        asyncStub = DiscoveryServiceGrpc.newStub(channel);
    }

    public void getReply(String serviceName, String port) throws Exception {
        PutRequest input = PutRequest.newBuilder().setServiceName(serviceName).setPort(port).build();
        PutReply output = blockingStub.put(input);
        return output;

    }

    public static List<String> putDiscoveryServer(List<String> discoveryServers, LogUtil opfile) {
        
        List<String> newDiscoveryServers = new ArrayList<>();
        PutReply res;   //risultato ottenuto dal server gRPC (il discovery server)

        /* Si tenta di contattare il discovery server registrato per memorizzare la porta su cui il servizio di Suggestions è in ascolto.
         * Se le chiamate dovessero fallire, si attendono 5 secondi per poi eseguire nuovamente il tentativo di connessione. */
        boolean ok = false;
        while(1) {
            //itero sui discovery server noti
            for(String discoveryServer : discoveryServers) {

                try {
                    //EQUIVALENTE DI: channel = grpc.insecure_channel(discovery_server)
                    ManagedChannel channel = ManagedChannelBuilder.forTarget(discoveryServer).usePlaintext().build();

                    //EQUIVALENTE DI: stub = Discovery_pb2_grpc.DiscoveryServiceStub(channel)
                    DiscovUtil client = new DiscovUtil(channel);

                    //EQUIVALENTE DI: res = stub.put(Discovery_pb2.PutRequest(serviceName="suggestions", port="50054"))
                    res = client.getReply("suggestions", "50054");

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

                for(String server : res.getList_server().getServers()) {
                    newDiscoveryServers.add(server);

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
