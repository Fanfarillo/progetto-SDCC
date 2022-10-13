import grpc

from proto import Booking_pb2
from proto import Booking_pb2_grpc

ADDR_PORT = 'localhost:50053'   #server_IP_addr:port_num

def checkFlightId(id):
    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num
    
    #create client stub
    stub = Booking_pb2_grpc.BookingServiceStub(channel)

    #get response from Flights Management service
    output = stub.SendId(Booking_pb2.IdMessage(id=id))
    #we need to return the boolean value
    return output.isOk

def registerFlight(id, date, departureAirport, arrivalAirport, departureTime, arrivalTime, airline, price, seats):
    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    #create client stub
    stub = Booking_pb2_grpc.BookingServiceStub(channel)

    #get response from Flights Management service
    output = stub.RegisterFlight(Booking_pb2.NewFlight2(id=id, date=date, departureAirport=departureAirport, arrivalAirport=arrivalAirport, departureTime=departureTime, arrivalTime=arrivalTime, airline=airline, price=price, seats=seats))
    #we need to return the boolean value
    return output.isOk

def updateFlightPrice(flightId, newPrice):
    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    #create client stub
    stub = Booking_pb2_grpc.BookingServiceStub(channel)

    #get response from Flights Management service
    output = stub.UpdateFlightPrice(Booking_pb2.UpdatedFlight2(flightId=flightId, newPrice=newPrice))
    #we need to return the boolean value
    return output.isOk
