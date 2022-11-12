# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto import Discovery_pb2 as proto_dot_Discovery__pb2


class DiscoveryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get = channel.unary_unary(
                '/DiscoveryService/get',
                request_serializer=proto_dot_Discovery__pb2.GetRequest.SerializeToString,
                response_deserializer=proto_dot_Discovery__pb2.GetReply.FromString,
                )
        self.put = channel.unary_unary(
                '/DiscoveryService/put',
                request_serializer=proto_dot_Discovery__pb2.PutRequest.SerializeToString,
                response_deserializer=proto_dot_Discovery__pb2.PutReply.FromString,
                )
        self.sendMicroserviceInfo = channel.unary_unary(
                '/DiscoveryService/sendMicroserviceInfo',
                request_serializer=proto_dot_Discovery__pb2.microserviceInfoRequest.SerializeToString,
                response_deserializer=proto_dot_Discovery__pb2.microserviceInfoReply.FromString,
                )


class DiscoveryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def get(self, request, context):
        """
        Consente di ottenere la porta relativa
        al microservizio passato come parametro.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def put(self, request, context):
        """
        Consente di registrare la porta relativa
        al microservizio passato come parametro.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sendMicroserviceInfo(self, request, context):
        """
        I microservizi per il discovery service si
        scambiano tra di loro le informazioni.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DiscoveryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=proto_dot_Discovery__pb2.GetRequest.FromString,
                    response_serializer=proto_dot_Discovery__pb2.GetReply.SerializeToString,
            ),
            'put': grpc.unary_unary_rpc_method_handler(
                    servicer.put,
                    request_deserializer=proto_dot_Discovery__pb2.PutRequest.FromString,
                    response_serializer=proto_dot_Discovery__pb2.PutReply.SerializeToString,
            ),
            'sendMicroserviceInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.sendMicroserviceInfo,
                    request_deserializer=proto_dot_Discovery__pb2.microserviceInfoRequest.FromString,
                    response_serializer=proto_dot_Discovery__pb2.microserviceInfoReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DiscoveryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DiscoveryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DiscoveryService/get',
            proto_dot_Discovery__pb2.GetRequest.SerializeToString,
            proto_dot_Discovery__pb2.GetReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def put(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DiscoveryService/put',
            proto_dot_Discovery__pb2.PutRequest.SerializeToString,
            proto_dot_Discovery__pb2.PutReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def sendMicroserviceInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DiscoveryService/sendMicroserviceInfo',
            proto_dot_Discovery__pb2.microserviceInfoRequest.SerializeToString,
            proto_dot_Discovery__pb2.microserviceInfoReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
