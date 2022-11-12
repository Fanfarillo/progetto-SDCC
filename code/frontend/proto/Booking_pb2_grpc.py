# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto import Booking_pb2 as proto_dot_Booking__pb2


class BookingServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getAllFlights = channel.unary_stream(
                '/proto.BookingService/getAllFlights',
                request_serializer=proto_dot_Booking__pb2.getAllFlightsRequest.SerializeToString,
                response_deserializer=proto_dot_Booking__pb2.getAllFlightsReply.FromString,
                )
        self.SendId = channel.unary_unary(
                '/proto.BookingService/SendId',
                request_serializer=proto_dot_Booking__pb2.IdMessage.SerializeToString,
                response_deserializer=proto_dot_Booking__pb2.IdResponse.FromString,
                )
        self.RegisterFlight = channel.unary_unary(
                '/proto.BookingService/RegisterFlight',
                request_serializer=proto_dot_Booking__pb2.NewFlight2.SerializeToString,
                response_deserializer=proto_dot_Booking__pb2.RegisterResponse.FromString,
                )
        self.UpdateFlightPrice = channel.unary_unary(
                '/proto.BookingService/UpdateFlightPrice',
                request_serializer=proto_dot_Booking__pb2.UpdatedFlight2.SerializeToString,
                response_deserializer=proto_dot_Booking__pb2.UpdateResponse.FromString,
                )
        self.getAllAvailableSeatsForFlight = channel.unary_stream(
                '/proto.BookingService/getAllAvailableSeatsForFlight',
                request_serializer=proto_dot_Booking__pb2.AvailableSeatRequest.SerializeToString,
                response_deserializer=proto_dot_Booking__pb2.AvailableSeatReply.FromString,
                )
        self.GetAirports = channel.unary_unary(
                '/proto.BookingService/GetAirports',
                request_serializer=proto_dot_Booking__pb2.AirportsRequest.SerializeToString,
                response_deserializer=proto_dot_Booking__pb2.AirportsResponse.FromString,
                )
        self.getLogFileBoo = channel.unary_stream(
                '/proto.BookingService/getLogFileBoo',
                request_serializer=proto_dot_Booking__pb2.GetLogFileRequestBoo.SerializeToString,
                response_deserializer=proto_dot_Booking__pb2.GetLogFileReplyBoo.FromString,
                )


class BookingServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getAllFlights(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

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

    def UpdateFlightPrice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getAllAvailableSeatsForFlight(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAirports(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getLogFileBoo(self, request, context):
        """Logging
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BookingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getAllFlights': grpc.unary_stream_rpc_method_handler(
                    servicer.getAllFlights,
                    request_deserializer=proto_dot_Booking__pb2.getAllFlightsRequest.FromString,
                    response_serializer=proto_dot_Booking__pb2.getAllFlightsReply.SerializeToString,
            ),
            'SendId': grpc.unary_unary_rpc_method_handler(
                    servicer.SendId,
                    request_deserializer=proto_dot_Booking__pb2.IdMessage.FromString,
                    response_serializer=proto_dot_Booking__pb2.IdResponse.SerializeToString,
            ),
            'RegisterFlight': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterFlight,
                    request_deserializer=proto_dot_Booking__pb2.NewFlight2.FromString,
                    response_serializer=proto_dot_Booking__pb2.RegisterResponse.SerializeToString,
            ),
            'UpdateFlightPrice': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateFlightPrice,
                    request_deserializer=proto_dot_Booking__pb2.UpdatedFlight2.FromString,
                    response_serializer=proto_dot_Booking__pb2.UpdateResponse.SerializeToString,
            ),
            'getAllAvailableSeatsForFlight': grpc.unary_stream_rpc_method_handler(
                    servicer.getAllAvailableSeatsForFlight,
                    request_deserializer=proto_dot_Booking__pb2.AvailableSeatRequest.FromString,
                    response_serializer=proto_dot_Booking__pb2.AvailableSeatReply.SerializeToString,
            ),
            'GetAirports': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAirports,
                    request_deserializer=proto_dot_Booking__pb2.AirportsRequest.FromString,
                    response_serializer=proto_dot_Booking__pb2.AirportsResponse.SerializeToString,
            ),
            'getLogFileBoo': grpc.unary_stream_rpc_method_handler(
                    servicer.getLogFileBoo,
                    request_deserializer=proto_dot_Booking__pb2.GetLogFileRequestBoo.FromString,
                    response_serializer=proto_dot_Booking__pb2.GetLogFileReplyBoo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'proto.BookingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BookingService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getAllFlights(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/proto.BookingService/getAllFlights',
            proto_dot_Booking__pb2.getAllFlightsRequest.SerializeToString,
            proto_dot_Booking__pb2.getAllFlightsReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/proto.BookingService/SendId',
            proto_dot_Booking__pb2.IdMessage.SerializeToString,
            proto_dot_Booking__pb2.IdResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/proto.BookingService/RegisterFlight',
            proto_dot_Booking__pb2.NewFlight2.SerializeToString,
            proto_dot_Booking__pb2.RegisterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateFlightPrice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.BookingService/UpdateFlightPrice',
            proto_dot_Booking__pb2.UpdatedFlight2.SerializeToString,
            proto_dot_Booking__pb2.UpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getAllAvailableSeatsForFlight(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/proto.BookingService/getAllAvailableSeatsForFlight',
            proto_dot_Booking__pb2.AvailableSeatRequest.SerializeToString,
            proto_dot_Booking__pb2.AvailableSeatReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAirports(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.BookingService/GetAirports',
            proto_dot_Booking__pb2.AirportsRequest.SerializeToString,
            proto_dot_Booking__pb2.AirportsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getLogFileBoo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/proto.BookingService/getLogFileBoo',
            proto_dot_Booking__pb2.GetLogFileRequestBoo.SerializeToString,
            proto_dot_Booking__pb2.GetLogFileReplyBoo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
