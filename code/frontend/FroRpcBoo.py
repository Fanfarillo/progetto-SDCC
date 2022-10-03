import grpc

from proto import Boo_pb2
from proto import Boo_pb2_grpc

ADDR_PORT = 'localhost:50053'   #server_IP_addr:port_num

def sendBookingInfo(giorno, mese, anno, aereoporto_partenza, aereoporto_arrivo, persone):
    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    #create client stub
    stub = Boo_pb2_grpc.BookingServiceStub(channel)

    #get response from Registration service
    output = stub.getAllFlights(Boo_pb2.SignUpInfo(giorno=giorno, mese=mese, anno=anno, aereoporto_partenza=aereoporto_partenza, aereoporto_arrivo=aereoporto_arrivo, persone=persone))
    #we need to return the boolean value
    return output


