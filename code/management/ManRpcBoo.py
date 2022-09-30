import grpc

from proto import BooMan_pb2
from proto import BooMan_pb2_grpc

ADDR_PORT = 'localhost:50053'   #server_IP_addr:port_num

def checkFlightId(id):
    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    #create client stub
    stub = BooMan_pb2_grpc.FlightsAndPricesStub(channel)

    #get response from Flights Management service
    output = stub.SendId(BooMan_pb2.IdMessage(id=id))
    #we need to return the boolean value
    return output.isOk

def registerFlight(id, date, departureAirport, arrivalAirport, departureTime, arrivalTime, airline, price, seats):
    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    #create client stub
    stub = BooMan_pb2_grpc.FlightsAndPricesStub(channel)

    #get response from Flights Management service
    output = stub.RegisterFlight(BooMan_pb2.NewFlight2(id=id, date=date, departureAirport=departureAirport, arrivalAirport=arrivalAirport, departureTime=departureTime, arrivalTime=arrivalTime, airline=airline, price=price, seats=seats))
    #we need to return the boolean value
    return output.isOk    
