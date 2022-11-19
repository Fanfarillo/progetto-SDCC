package control;

import java.util.concurrent.TimeUnit;

import io.grpc.StatusRuntimeException;
import io.grpc.Channel;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;

import control.proto.*;

import control.proto.SuggestionsServiceGrpc.SuggestionsServiceBlockingStub;
import control.proto.SuggestionsServiceGrpc.SuggestionsServiceStub;

public class SugClient {

    private final SuggestionsServiceBlockingStub blockingStub;
    private final SuggestionsServiceStub asyncStub;

    public SugClient(Channel channel) {
        blockingStub = SuggestionsServiceGrpc.newBlockingStub(channel);
        asyncStub = SuggestionsServiceGrpc.newStub(channel);
    }

    public void sendMsg(String oldFlightsMsg) throws Exception {
        OldFlight input = OldFlight.newBuilder().setOldFlightsMsg(oldFlightsMsg).build();
        blockingStub.storeOldFlight(input);
    }

    public static void sendToSecondary(String msg) {
        //open gRPC channel
        String target = "code_suggestions_2:50054";
        ManagedChannel channel = ManagedChannelBuilder.forTarget(target).usePlaintext().build();

        try {           
            //create client stub
            SugClient client = new SugClient(channel);
            //send message
            client.sendMsg(msg);

        }
        catch(Exception e) {
            e.printStackTrace();
        }
        finally {
            try {
                channel.shutdownNow().awaitTermination(5, TimeUnit.SECONDS);
            }
            catch(Exception e1) {
                e1.printStackTrace();
            }
        }

    }

}
