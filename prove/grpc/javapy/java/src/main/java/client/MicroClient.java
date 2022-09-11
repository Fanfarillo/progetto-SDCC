package client;

import java.util.concurrent.TimeUnit;

import io.grpc.StatusRuntimeException;
import io.grpc.Channel;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;

import client.proto.*;

import client.proto.GreeterGrpc.GreeterBlockingStub;
import client.proto.GreeterGrpc.GreeterStub;

public class MicroClient {

    private final GreeterBlockingStub blockingStub;
    private final GreeterStub asyncStub;

    public MicroClient(Channel channel) {
        blockingStub = GreeterGrpc.newBlockingStub(channel);
        asyncStub = GreeterGrpc.newStub(channel);
    }

    public void getResponse(String id, String name) {
        Request input = Request.newBuilder().setId(id).setName(name).build();

        Response output;
        try {
            output = blockingStub.getServiceName(input);
            System.out.println("Response: " + output);

        } catch (StatusRuntimeException e) {
            System.out.println("Something went wrong during gRPC communication.");
        }

    }

    public static void main(String[] args) throws InterruptedException {
        //open gRPC channel
        String target = "localhost:50051";
        ManagedChannel channel = ManagedChannelBuilder.forTarget(target).usePlaintext().build();

        try {
            //create client stub
            MicroClient client = new MicroClient(channel);

            //get response
            client.getResponse("1", "What's your name?");          

        } finally {
           channel.shutdownNow().awaitTermination(5, TimeUnit.SECONDS); 
        }

    }

}

