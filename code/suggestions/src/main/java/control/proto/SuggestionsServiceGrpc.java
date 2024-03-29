package control.proto;

import static io.grpc.MethodDescriptor.generateFullMethodName;

/**
 */
@javax.annotation.Generated(
    value = "by gRPC proto compiler (version 1.49.0)",
    comments = "Source: Suggestions.proto")
@io.grpc.stub.annotations.GrpcGenerated
public final class SuggestionsServiceGrpc {

  private SuggestionsServiceGrpc() {}

  public static final String SERVICE_NAME = "proto.SuggestionsService";

  // Static method descriptors that strictly reflect the proto.
  private static volatile io.grpc.MethodDescriptor<control.proto.SelectedFlight,
      control.proto.SelectionResponse> getGetSelectedFlightMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "GetSelectedFlight",
      requestType = control.proto.SelectedFlight.class,
      responseType = control.proto.SelectionResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<control.proto.SelectedFlight,
      control.proto.SelectionResponse> getGetSelectedFlightMethod() {
    io.grpc.MethodDescriptor<control.proto.SelectedFlight, control.proto.SelectionResponse> getGetSelectedFlightMethod;
    if ((getGetSelectedFlightMethod = SuggestionsServiceGrpc.getGetSelectedFlightMethod) == null) {
      synchronized (SuggestionsServiceGrpc.class) {
        if ((getGetSelectedFlightMethod = SuggestionsServiceGrpc.getGetSelectedFlightMethod) == null) {
          SuggestionsServiceGrpc.getGetSelectedFlightMethod = getGetSelectedFlightMethod =
              io.grpc.MethodDescriptor.<control.proto.SelectedFlight, control.proto.SelectionResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "GetSelectedFlight"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  control.proto.SelectedFlight.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  control.proto.SelectionResponse.getDefaultInstance()))
              .setSchemaDescriptor(new SuggestionsServiceMethodDescriptorSupplier("GetSelectedFlight"))
              .build();
        }
      }
    }
    return getGetSelectedFlightMethod;
  }

  private static volatile io.grpc.MethodDescriptor<control.proto.OldFlight,
      control.proto.StoreOldResponse> getStoreOldFlightMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "StoreOldFlight",
      requestType = control.proto.OldFlight.class,
      responseType = control.proto.StoreOldResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<control.proto.OldFlight,
      control.proto.StoreOldResponse> getStoreOldFlightMethod() {
    io.grpc.MethodDescriptor<control.proto.OldFlight, control.proto.StoreOldResponse> getStoreOldFlightMethod;
    if ((getStoreOldFlightMethod = SuggestionsServiceGrpc.getStoreOldFlightMethod) == null) {
      synchronized (SuggestionsServiceGrpc.class) {
        if ((getStoreOldFlightMethod = SuggestionsServiceGrpc.getStoreOldFlightMethod) == null) {
          SuggestionsServiceGrpc.getStoreOldFlightMethod = getStoreOldFlightMethod =
              io.grpc.MethodDescriptor.<control.proto.OldFlight, control.proto.StoreOldResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "StoreOldFlight"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  control.proto.OldFlight.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  control.proto.StoreOldResponse.getDefaultInstance()))
              .setSchemaDescriptor(new SuggestionsServiceMethodDescriptorSupplier("StoreOldFlight"))
              .build();
        }
      }
    }
    return getStoreOldFlightMethod;
  }

  private static volatile io.grpc.MethodDescriptor<control.proto.GetLogFileRequestSug,
      control.proto.GetLogFileReplySug> getGetLogFileSugMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "getLogFileSug",
      requestType = control.proto.GetLogFileRequestSug.class,
      responseType = control.proto.GetLogFileReplySug.class,
      methodType = io.grpc.MethodDescriptor.MethodType.SERVER_STREAMING)
  public static io.grpc.MethodDescriptor<control.proto.GetLogFileRequestSug,
      control.proto.GetLogFileReplySug> getGetLogFileSugMethod() {
    io.grpc.MethodDescriptor<control.proto.GetLogFileRequestSug, control.proto.GetLogFileReplySug> getGetLogFileSugMethod;
    if ((getGetLogFileSugMethod = SuggestionsServiceGrpc.getGetLogFileSugMethod) == null) {
      synchronized (SuggestionsServiceGrpc.class) {
        if ((getGetLogFileSugMethod = SuggestionsServiceGrpc.getGetLogFileSugMethod) == null) {
          SuggestionsServiceGrpc.getGetLogFileSugMethod = getGetLogFileSugMethod =
              io.grpc.MethodDescriptor.<control.proto.GetLogFileRequestSug, control.proto.GetLogFileReplySug>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.SERVER_STREAMING)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "getLogFileSug"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  control.proto.GetLogFileRequestSug.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  control.proto.GetLogFileReplySug.getDefaultInstance()))
              .setSchemaDescriptor(new SuggestionsServiceMethodDescriptorSupplier("getLogFileSug"))
              .build();
        }
      }
    }
    return getGetLogFileSugMethod;
  }

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static SuggestionsServiceStub newStub(io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<SuggestionsServiceStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<SuggestionsServiceStub>() {
        @java.lang.Override
        public SuggestionsServiceStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new SuggestionsServiceStub(channel, callOptions);
        }
      };
    return SuggestionsServiceStub.newStub(factory, channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static SuggestionsServiceBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<SuggestionsServiceBlockingStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<SuggestionsServiceBlockingStub>() {
        @java.lang.Override
        public SuggestionsServiceBlockingStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new SuggestionsServiceBlockingStub(channel, callOptions);
        }
      };
    return SuggestionsServiceBlockingStub.newStub(factory, channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static SuggestionsServiceFutureStub newFutureStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<SuggestionsServiceFutureStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<SuggestionsServiceFutureStub>() {
        @java.lang.Override
        public SuggestionsServiceFutureStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new SuggestionsServiceFutureStub(channel, callOptions);
        }
      };
    return SuggestionsServiceFutureStub.newStub(factory, channel);
  }

  /**
   */
  public static abstract class SuggestionsServiceImplBase implements io.grpc.BindableService {

    /**
     */
    public void getSelectedFlight(control.proto.SelectedFlight request,
        io.grpc.stub.StreamObserver<control.proto.SelectionResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getGetSelectedFlightMethod(), responseObserver);
    }

    /**
     */
    public void storeOldFlight(control.proto.OldFlight request,
        io.grpc.stub.StreamObserver<control.proto.StoreOldResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getStoreOldFlightMethod(), responseObserver);
    }

    /**
     * <pre>
     * Logging
     * </pre>
     */
    public void getLogFileSug(control.proto.GetLogFileRequestSug request,
        io.grpc.stub.StreamObserver<control.proto.GetLogFileReplySug> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getGetLogFileSugMethod(), responseObserver);
    }

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return io.grpc.ServerServiceDefinition.builder(getServiceDescriptor())
          .addMethod(
            getGetSelectedFlightMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                control.proto.SelectedFlight,
                control.proto.SelectionResponse>(
                  this, METHODID_GET_SELECTED_FLIGHT)))
          .addMethod(
            getStoreOldFlightMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                control.proto.OldFlight,
                control.proto.StoreOldResponse>(
                  this, METHODID_STORE_OLD_FLIGHT)))
          .addMethod(
            getGetLogFileSugMethod(),
            io.grpc.stub.ServerCalls.asyncServerStreamingCall(
              new MethodHandlers<
                control.proto.GetLogFileRequestSug,
                control.proto.GetLogFileReplySug>(
                  this, METHODID_GET_LOG_FILE_SUG)))
          .build();
    }
  }

  /**
   */
  public static final class SuggestionsServiceStub extends io.grpc.stub.AbstractAsyncStub<SuggestionsServiceStub> {
    private SuggestionsServiceStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected SuggestionsServiceStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new SuggestionsServiceStub(channel, callOptions);
    }

    /**
     */
    public void getSelectedFlight(control.proto.SelectedFlight request,
        io.grpc.stub.StreamObserver<control.proto.SelectionResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getGetSelectedFlightMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void storeOldFlight(control.proto.OldFlight request,
        io.grpc.stub.StreamObserver<control.proto.StoreOldResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getStoreOldFlightMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     * <pre>
     * Logging
     * </pre>
     */
    public void getLogFileSug(control.proto.GetLogFileRequestSug request,
        io.grpc.stub.StreamObserver<control.proto.GetLogFileReplySug> responseObserver) {
      io.grpc.stub.ClientCalls.asyncServerStreamingCall(
          getChannel().newCall(getGetLogFileSugMethod(), getCallOptions()), request, responseObserver);
    }
  }

  /**
   */
  public static final class SuggestionsServiceBlockingStub extends io.grpc.stub.AbstractBlockingStub<SuggestionsServiceBlockingStub> {
    private SuggestionsServiceBlockingStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected SuggestionsServiceBlockingStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new SuggestionsServiceBlockingStub(channel, callOptions);
    }

    /**
     */
    public control.proto.SelectionResponse getSelectedFlight(control.proto.SelectedFlight request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getGetSelectedFlightMethod(), getCallOptions(), request);
    }

    /**
     */
    public control.proto.StoreOldResponse storeOldFlight(control.proto.OldFlight request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getStoreOldFlightMethod(), getCallOptions(), request);
    }

    /**
     * <pre>
     * Logging
     * </pre>
     */
    public java.util.Iterator<control.proto.GetLogFileReplySug> getLogFileSug(
        control.proto.GetLogFileRequestSug request) {
      return io.grpc.stub.ClientCalls.blockingServerStreamingCall(
          getChannel(), getGetLogFileSugMethod(), getCallOptions(), request);
    }
  }

  /**
   */
  public static final class SuggestionsServiceFutureStub extends io.grpc.stub.AbstractFutureStub<SuggestionsServiceFutureStub> {
    private SuggestionsServiceFutureStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected SuggestionsServiceFutureStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new SuggestionsServiceFutureStub(channel, callOptions);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<control.proto.SelectionResponse> getSelectedFlight(
        control.proto.SelectedFlight request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getGetSelectedFlightMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<control.proto.StoreOldResponse> storeOldFlight(
        control.proto.OldFlight request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getStoreOldFlightMethod(), getCallOptions()), request);
    }
  }

  private static final int METHODID_GET_SELECTED_FLIGHT = 0;
  private static final int METHODID_STORE_OLD_FLIGHT = 1;
  private static final int METHODID_GET_LOG_FILE_SUG = 2;

  private static final class MethodHandlers<Req, Resp> implements
      io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final SuggestionsServiceImplBase serviceImpl;
    private final int methodId;

    MethodHandlers(SuggestionsServiceImplBase serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_GET_SELECTED_FLIGHT:
          serviceImpl.getSelectedFlight((control.proto.SelectedFlight) request,
              (io.grpc.stub.StreamObserver<control.proto.SelectionResponse>) responseObserver);
          break;
        case METHODID_STORE_OLD_FLIGHT:
          serviceImpl.storeOldFlight((control.proto.OldFlight) request,
              (io.grpc.stub.StreamObserver<control.proto.StoreOldResponse>) responseObserver);
          break;
        case METHODID_GET_LOG_FILE_SUG:
          serviceImpl.getLogFileSug((control.proto.GetLogFileRequestSug) request,
              (io.grpc.stub.StreamObserver<control.proto.GetLogFileReplySug>) responseObserver);
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

  private static abstract class SuggestionsServiceBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoFileDescriptorSupplier, io.grpc.protobuf.ProtoServiceDescriptorSupplier {
    SuggestionsServiceBaseDescriptorSupplier() {}

    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return control.proto.Suggestions.getDescriptor();
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.ServiceDescriptor getServiceDescriptor() {
      return getFileDescriptor().findServiceByName("SuggestionsService");
    }
  }

  private static final class SuggestionsServiceFileDescriptorSupplier
      extends SuggestionsServiceBaseDescriptorSupplier {
    SuggestionsServiceFileDescriptorSupplier() {}
  }

  private static final class SuggestionsServiceMethodDescriptorSupplier
      extends SuggestionsServiceBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoMethodDescriptorSupplier {
    private final String methodName;

    SuggestionsServiceMethodDescriptorSupplier(String methodName) {
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
      synchronized (SuggestionsServiceGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new SuggestionsServiceFileDescriptorSupplier())
              .addMethod(getGetSelectedFlightMethod())
              .addMethod(getStoreOldFlightMethod())
              .addMethod(getGetLogFileSugMethod())
              .build();
        }
      }
    }
    return result;
  }
}
