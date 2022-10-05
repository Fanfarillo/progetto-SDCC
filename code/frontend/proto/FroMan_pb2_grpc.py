# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto import FroMan_pb2 as proto_dot_FroMan__pb2


class FlightsInfoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddFlight = channel.unary_unary(
                '/proto.FlightsInfo/AddFlight',
                request_serializer=proto_dot_FroMan__pb2.NewFlight.SerializeToString,
                response_deserializer=proto_dot_FroMan__pb2.AddResponse.FromString,
                )
        self.ModifyFlight = channel.unary_unary(
                '/proto.FlightsInfo/ModifyFlight',
                request_serializer=proto_dot_FroMan__pb2.UpdatedFlight.SerializeToString,
                response_deserializer=proto_dot_FroMan__pb2.ModFlightResponse.FromString,
                )
        self.ModifySeats = channel.unary_unary(
                '/proto.FlightsInfo/ModifySeats',
                request_serializer=proto_dot_FroMan__pb2.UpdatedSeats.SerializeToString,
                response_deserializer=proto_dot_FroMan__pb2.ModSeatsResponse.FromString,
                )


class FlightsInfoServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddFlight(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ModifyFlight(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ModifySeats(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FlightsInfoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddFlight': grpc.unary_unary_rpc_method_handler(
                    servicer.AddFlight,
                    request_deserializer=proto_dot_FroMan__pb2.NewFlight.FromString,
                    response_serializer=proto_dot_FroMan__pb2.AddResponse.SerializeToString,
            ),
            'ModifyFlight': grpc.unary_unary_rpc_method_handler(
                    servicer.ModifyFlight,
                    request_deserializer=proto_dot_FroMan__pb2.UpdatedFlight.FromString,
                    response_serializer=proto_dot_FroMan__pb2.ModFlightResponse.SerializeToString,
            ),
            'ModifySeats': grpc.unary_unary_rpc_method_handler(
                    servicer.ModifySeats,
                    request_deserializer=proto_dot_FroMan__pb2.UpdatedSeats.FromString,
                    response_serializer=proto_dot_FroMan__pb2.ModSeatsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'proto.FlightsInfo', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FlightsInfo(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddFlight(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.FlightsInfo/AddFlight',
            proto_dot_FroMan__pb2.NewFlight.SerializeToString,
            proto_dot_FroMan__pb2.AddResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ModifyFlight(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.FlightsInfo/ModifyFlight',
            proto_dot_FroMan__pb2.UpdatedFlight.SerializeToString,
            proto_dot_FroMan__pb2.ModFlightResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ModifySeats(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.FlightsInfo/ModifySeats',
            proto_dot_FroMan__pb2.UpdatedSeats.SerializeToString,
            proto_dot_FroMan__pb2.ModSeatsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
