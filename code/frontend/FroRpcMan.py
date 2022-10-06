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

def sendNewPrice(flightId, newPrice):
    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    #create client stub
    stub = FroMan_pb2_grpc.FlightsInfoStub(channel)

    #get response from Flights Management service
    output = stub.ModifyFlight(FroMan_pb2.UpdatedFlight(flightId=flightId, newPrice=newPrice))
    #we need to return the boolean value
    return output.isOk    

def sendSeatsPrices(airline, price1, price2, price6, price16, price18):
    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    #create client stub
    stub = FroMan_pb2_grpc.FlightsInfoStub(channel)

    #get response from Flights Management service
    output = stub.ModifySeats(FroMan_pb2.UpdatedSeats(airline=airline, price1=price1, price2=price2, price6=price6, price16=price16, price18=price18))
    #we need to return the boolean value
    return output.isOk 

def sendServicesPrices(airline, priceBM, priceBG, priceBS, priceAD, priceAB, priceTN):
    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    #create client stub
    stub = FroMan_pb2_grpc.FlightsInfoStub(channel)

    #get response from Flights Management service
    output = stub.ModifyServices(FroMan_pb2.UpdatedServices(airline=airline, priceBM=priceBM, priceBG=priceBG, priceBS=priceBS, priceAD=priceAD, priceAB=priceAB, priceTN=priceTN))
    #we need to return the boolean value
    return output.isOk 
