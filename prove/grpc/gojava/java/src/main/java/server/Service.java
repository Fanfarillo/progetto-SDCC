package server;

import io.grpc.stub.StreamObserver;

import server.proto.GreeterGrpc.GreeterImplBase;
import server.proto.Request;
import server.proto.Response;

public class Service extends GreeterImplBase {

    @Override
    public void getServiceName(Request req, StreamObserver<Response> responseObserver) {      
        System.out.println("Request: " + req.getName());

        Response response = Response.newBuilder().setServiceName("M2").build();

        //send data to the client
        responseObserver.onNext(response);
        responseObserver.onCompleted();

    }

}
