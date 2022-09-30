# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto import BooMan_pb2 as proto_dot_BooMan__pb2


class FlightsAndPricesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendId = channel.unary_unary(
                '/proto.FlightsAndPrices/SendId',
                request_serializer=proto_dot_BooMan__pb2.IdMessage.SerializeToString,
                response_deserializer=proto_dot_BooMan__pb2.IdResponse.FromString,
                )
        self.RegisterFlight = channel.unary_unary(
                '/proto.FlightsAndPrices/RegisterFlight',
                request_serializer=proto_dot_BooMan__pb2.NewFlight2.SerializeToString,
                response_deserializer=proto_dot_BooMan__pb2.RegisterResponse.FromString,
                )


class FlightsAndPricesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterFlight(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FlightsAndPricesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendId': grpc.unary_unary_rpc_method_handler(
                    servicer.SendId,
                    request_deserializer=proto_dot_BooMan__pb2.IdMessage.FromString,
                    response_serializer=proto_dot_BooMan__pb2.IdResponse.SerializeToString,
            ),
            'RegisterFlight': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterFlight,
                    request_deserializer=proto_dot_BooMan__pb2.NewFlight2.FromString,
                    response_serializer=proto_dot_BooMan__pb2.RegisterResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'proto.FlightsAndPrices', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FlightsAndPrices(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.FlightsAndPrices/SendId',
            proto_dot_BooMan__pb2.IdMessage.SerializeToString,
            proto_dot_BooMan__pb2.IdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterFlight(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.FlightsAndPrices/RegisterFlight',
            proto_dot_BooMan__pb2.NewFlight2.SerializeToString,
            proto_dot_BooMan__pb2.RegisterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
