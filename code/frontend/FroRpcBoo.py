import grpc

from proto import Boo_pb2
from proto import Boo_pb2_grpc

ADDR_PORT = 'localhost:50053'   #server_IP_addr:port_num

def sendBookingInfo(giorno, mese, anno, aereoporto_partenza, aereoporto_arrivo, persone):
    #open gRPC channel
    print("entrato...")
    try:
        channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    #create client stub
        stub = Boo_pb2_grpc.BookingServiceStub(channel)

    #get response from Registration service
    
        output = stub.getAllFlights(Boo_pb2.getAllFlightsRequest(giorno=int(giorno), mese=int(mese), anno=int(anno), aereoporto_partenza=aereoporto_partenza, aereoporto_arrivo=aereoporto_arrivo, persone=int(persone)))
    except:
        print("ECCEZIONE...")
    #we need to return the boolean value
    print("ciao")
    return output


