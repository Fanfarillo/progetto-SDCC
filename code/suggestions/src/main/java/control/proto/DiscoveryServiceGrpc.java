package control.proto;

import static io.grpc.MethodDescriptor.generateFullMethodName;

/**
 */
@javax.annotation.Generated(
    value = "by gRPC proto compiler (version 1.49.0)",
    comments = "Source: Discovery.proto")
@io.grpc.stub.annotations.GrpcGenerated
public final class DiscoveryServiceGrpc {

  private DiscoveryServiceGrpc() {}

  public static final String SERVICE_NAME = "proto.DiscoveryService";

  // Static method descriptors that strictly reflect the proto.
  private static volatile io.grpc.MethodDescriptor<control.proto.GetRequest,
      control.proto.GetReply> getGetMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "get",
      requestType = control.proto.GetRequest.class,
      responseType = control.proto.GetReply.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<control.proto.GetRequest,
      control.proto.GetReply> getGetMethod() {
    io.grpc.MethodDescriptor<control.proto.GetRequest, control.proto.GetReply> getGetMethod;
    if ((getGetMethod = DiscoveryServiceGrpc.getGetMethod) == null) {
      synchronized (DiscoveryServiceGrpc.class) {
        if ((getGetMethod = DiscoveryServiceGrpc.getGetMethod) == null) {
          DiscoveryServiceGrpc.getGetMethod = getGetMethod =
              io.grpc.MethodDescriptor.<control.proto.GetRequest, control.proto.GetReply>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "get"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  control.proto.GetRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  control.proto.GetReply.getDefaultInstance()))
              .setSchemaDescriptor(new DiscoveryServiceMethodDescriptorSupplier("get"))
              .build();
        }
      }
    }
    return getGetMethod;
  }

  private static volatile io.grpc.MethodDescriptor<control.proto.PutRequest,
      control.proto.PutReply> getPutMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "put",
      requestType = control.proto.PutRequest.class,
      responseType = control.proto.PutReply.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<control.proto.PutRequest,
      control.proto.PutReply> getPutMethod() {
    io.grpc.MethodDescriptor<control.proto.PutRequest, control.proto.PutReply> getPutMethod;
    if ((getPutMethod = DiscoveryServiceGrpc.getPutMethod) == null) {
      synchronized (DiscoveryServiceGrpc.class) {
        if ((getPutMethod = DiscoveryServiceGrpc.getPutMethod) == null) {
          DiscoveryServiceGrpc.getPutMethod = getPutMethod =
              io.grpc.MethodDescriptor.<control.proto.PutRequest, control.proto.PutReply>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "put"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  control.proto.PutRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  control.proto.PutReply.getDefaultInstance()))
              .setSchemaDescriptor(new DiscoveryServiceMethodDescriptorSupplier("put"))
              .build();
        }
      }
    }
    return getPutMethod;
  }

  private static volatile io.grpc.MethodDescriptor<control.proto.microserviceInfoRequest,
      control.proto.microserviceInfoReply> getSendMicroserviceInfoMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "sendMicroserviceInfo",
      requestType = control.proto.microserviceInfoRequest.class,
      responseType = control.proto.microserviceInfoReply.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<control.proto.microserviceInfoRequest,
      control.proto.microserviceInfoReply> getSendMicroserviceInfoMethod() {
    io.grpc.MethodDescriptor<control.proto.microserviceInfoRequest, control.proto.microserviceInfoReply> getSendMicroserviceInfoMethod;
    if ((getSendMicroserviceInfoMethod = DiscoveryServiceGrpc.getSendMicroserviceInfoMethod) == null) {
      synchronized (DiscoveryServiceGrpc.class) {
        if ((getSendMicroserviceInfoMethod = DiscoveryServiceGrpc.getSendMicroserviceInfoMethod) == null) {
          DiscoveryServiceGrpc.getSendMicroserviceInfoMethod = getSendMicroserviceInfoMethod =
              io.grpc.MethodDescriptor.<control.proto.microserviceInfoRequest, control.proto.microserviceInfoReply>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "sendMicroserviceInfo"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  control.proto.microserviceInfoRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  control.proto.microserviceInfoReply.getDefaultInstance()))
              .setSchemaDescriptor(new DiscoveryServiceMethodDescriptorSupplier("sendMicroserviceInfo"))
              .build();
        }
      }
    }
    return getSendMicroserviceInfoMethod;
  }

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static DiscoveryServiceStub newStub(io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<DiscoveryServiceStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<DiscoveryServiceStub>() {
        @java.lang.Override
        public DiscoveryServiceStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new DiscoveryServiceStub(channel, callOptions);
        }
      };
    return DiscoveryServiceStub.newStub(factory, channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static DiscoveryServiceBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<DiscoveryServiceBlockingStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<DiscoveryServiceBlockingStub>() {
        @java.lang.Override
        public DiscoveryServiceBlockingStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new DiscoveryServiceBlockingStub(channel, callOptions);
        }
      };
    return DiscoveryServiceBlockingStub.newStub(factory, channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static DiscoveryServiceFutureStub newFutureStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<DiscoveryServiceFutureStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<DiscoveryServiceFutureStub>() {
        @java.lang.Override
        public DiscoveryServiceFutureStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new DiscoveryServiceFutureStub(channel, callOptions);
        }
      };
    return DiscoveryServiceFutureStub.newStub(factory, channel);
  }

  /**
   */
  public static abstract class DiscoveryServiceImplBase implements io.grpc.BindableService {

    /**
     * <pre>
     *Consente di ottenere la porta relativa
     *al microservizio passato come parametro.
     * </pre>
     */
    public void get(control.proto.GetRequest request,
        io.grpc.stub.StreamObserver<control.proto.GetReply> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getGetMethod(), responseObserver);
    }

    /**
     * <pre>
     *Consente di registrare la porta relativa
     *al microservizio passato come parametro.
     * </pre>
     */
    public void put(control.proto.PutRequest request,
        io.grpc.stub.StreamObserver<control.proto.PutReply> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getPutMethod(), responseObserver);
    }

    /**
     * <pre>
     *I microservizi per il discovery service si
     *scambiano tra di loro le informazioni.
     * </pre>
     */
    public void sendMicroserviceInfo(control.proto.microserviceInfoRequest request,
        io.grpc.stub.StreamObserver<control.proto.microserviceInfoReply> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getSendMicroserviceInfoMethod(), responseObserver);
    }

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return io.grpc.ServerServiceDefinition.builder(getServiceDescriptor())
          .addMethod(
            getGetMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                control.proto.GetRequest,
                control.proto.GetReply>(
                  this, METHODID_GET)))
          .addMethod(
            getPutMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                control.proto.PutRequest,
                control.proto.PutReply>(
                  this, METHODID_PUT)))
          .addMethod(
            getSendMicroserviceInfoMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                control.proto.microserviceInfoRequest,
                control.proto.microserviceInfoReply>(
                  this, METHODID_SEND_MICROSERVICE_INFO)))
          .build();
    }
  }

  /**
   */
  public static final class DiscoveryServiceStub extends io.grpc.stub.AbstractAsyncStub<DiscoveryServiceStub> {
    private DiscoveryServiceStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected DiscoveryServiceStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new DiscoveryServiceStub(channel, callOptions);
    }

    /**
     * <pre>
     *Consente di ottenere la porta relativa
     *al microservizio passato come parametro.
     * </pre>
     */
    public void get(control.proto.GetRequest request,
        io.grpc.stub.StreamObserver<control.proto.GetReply> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getGetMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     * <pre>
     *Consente di registrare la porta relativa
     *al microservizio passato come parametro.
     * </pre>
     */
    public void put(control.proto.PutRequest request,
        io.grpc.stub.StreamObserver<control.proto.PutReply> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getPutMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     * <pre>
     *I microservizi per il discovery service si
     *scambiano tra di loro le informazioni.
     * </pre>
     */
    public void sendMicroserviceInfo(control.proto.microserviceInfoRequest request,
        io.grpc.stub.StreamObserver<control.proto.microserviceInfoReply> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getSendMicroserviceInfoMethod(), getCallOptions()), request, responseObserver);
    }
  }

  /**
   */
  public static final class DiscoveryServiceBlockingStub extends io.grpc.stub.AbstractBlockingStub<DiscoveryServiceBlockingStub> {
    private DiscoveryServiceBlockingStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected DiscoveryServiceBlockingStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new DiscoveryServiceBlockingStub(channel, callOptions);
    }

    /**
     * <pre>
     *Consente di ottenere la porta relativa
     *al microservizio passato come parametro.
     * </pre>
     */
    public control.proto.GetReply get(control.proto.GetRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getGetMethod(), getCallOptions(), request);
    }

    /**
     * <pre>
     *Consente di registrare la porta relativa
     *al microservizio passato come parametro.
     * </pre>
     */
    public control.proto.PutReply put(control.proto.PutRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getPutMethod(), getCallOptions(), request);
    }

    /**
     * <pre>
     *I microservizi per il discovery service si
     *scambiano tra di loro le informazioni.
     * </pre>
     */
    public control.proto.microserviceInfoReply sendMicroserviceInfo(control.proto.microserviceInfoRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getSendMicroserviceInfoMethod(), getCallOptions(), request);
    }
  }

  /**
   */
  public static final class DiscoveryServiceFutureStub extends io.grpc.stub.AbstractFutureStub<DiscoveryServiceFutureStub> {
    private DiscoveryServiceFutureStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected DiscoveryServiceFutureStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new DiscoveryServiceFutureStub(channel, callOptions);
    }

    /**
     * <pre>
     *Consente di ottenere la porta relativa
     *al microservizio passato come parametro.
     * </pre>
     */
    public com.google.common.util.concurrent.ListenableFuture<control.proto.GetReply> get(
        control.proto.GetRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getGetMethod(), getCallOptions()), request);
    }

    /**
     * <pre>
     *Consente di registrare la porta relativa
     *al microservizio passato come parametro.
     * </pre>
     */
    public com.google.common.util.concurrent.ListenableFuture<control.proto.PutReply> put(
        control.proto.PutRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getPutMethod(), getCallOptions()), request);
    }

    /**
     * <pre>
     *I microservizi per il discovery service si
     *scambiano tra di loro le informazioni.
     * </pre>
     */
    public com.google.common.util.concurrent.ListenableFuture<control.proto.microserviceInfoReply> sendMicroserviceInfo(
        control.proto.microserviceInfoRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getSendMicroserviceInfoMethod(), getCallOptions()), request);
    }
  }

  private static final int METHODID_GET = 0;
  private static final int METHODID_PUT = 1;
  private static final int METHODID_SEND_MICROSERVICE_INFO = 2;

  private static final class MethodHandlers<Req, Resp> implements
      io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final DiscoveryServiceImplBase serviceImpl;
    private final int methodId;

    MethodHandlers(DiscoveryServiceImplBase serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_GET:
          serviceImpl.get((control.proto.GetRequest) request,
              (io.grpc.stub.StreamObserver<control.proto.GetReply>) responseObserver);
          break;
        case METHODID_PUT:
          serviceImpl.put((control.proto.PutRequest) request,
              (io.grpc.stub.StreamObserver<control.proto.PutReply>) responseObserver);
          break;
        case METHODID_SEND_MICROSERVICE_INFO:
          serviceImpl.sendMicroserviceInfo((control.proto.microserviceInfoRequest) request,
              (io.grpc.stub.StreamObserver<control.proto.microserviceInfoReply>) responseObserver);
          break;
        default:
          throw new AssertionError();
      }
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public io.grpc.stub.StreamObserver<Req> invoke(
        io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        default:
          throw new AssertionError();
      }
    }
  }

  private static abstract class DiscoveryServiceBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoFileDescriptorSupplier, io.grpc.protobuf.ProtoServiceDescriptorSupplier {
    DiscoveryServiceBaseDescriptorSupplier() {}

    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return control.proto.Discovery.getDescriptor();
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.ServiceDescriptor getServiceDescriptor() {
      return getFileDescriptor().findServiceByName("DiscoveryService");
    }
  }

  private static final class DiscoveryServiceFileDescriptorSupplier
      extends DiscoveryServiceBaseDescriptorSupplier {
    DiscoveryServiceFileDescriptorSupplier() {}
  }

  private static final class DiscoveryServiceMethodDescriptorSupplier
      extends DiscoveryServiceBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoMethodDescriptorSupplier {
    private final String methodName;

    DiscoveryServiceMethodDescriptorSupplier(String methodName) {
      this.methodName = methodName;
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.MethodDescriptor getMethodDescriptor() {
      return getServiceDescriptor().findMethodByName(methodName);
    }
  }

  private static volatile io.grpc.ServiceDescriptor serviceDescriptor;

  public static io.grpc.ServiceDescriptor getServiceDescriptor() {
    io.grpc.ServiceDescriptor result = serviceDescriptor;
    if (result == null) {
      synchronized (DiscoveryServiceGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new DiscoveryServiceFileDescriptorSupplier())
              .addMethod(getGetMethod())
              .addMethod(getPutMethod())
              .addMethod(getSendMicroserviceInfoMethod())
              .build();
        }
      }
    }
    return result;
  }
}
