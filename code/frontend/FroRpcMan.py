import grpc

from proto import FroMan_pb2
from proto import FroMan_pb2_grpc

ADDR_PORT = 'localhost:50052'   #server_IP_addr:port_num

def sendNewFlight(id, date, departureAirport, arrivalAirport, departureTime, arrivalTime, airline, price, seats):
    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    #create client stub
    stub = FroMan_pb2_grpc.FlightsInfoStub(channel)

    #get response from Flights Management service
    output = stub.AddFlight(FroMan_pb2.NewFlight(id=id, date=date, departureAirport=departureAirport, arrivalAirport=arrivalAirport, departureTime=departureTime, arrivalTime=arrivalTime, airline=airline, price=price, seats=seats))
    #we need to return the boolean value
    return output.isOk
