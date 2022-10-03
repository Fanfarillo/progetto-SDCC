import grpc

from proto import Boo_pb2
from proto import Boo_pb2_grpc

ADDR_PORT = 'localhost:50053'   #server_IP_addr:port_num

def sendBookingInfo(giorno, mese, anno, aereoporto_partenza, aereoporto_arrivo, persone):
    #open gRPC channel
    print("entrato...")
    output = 0
    with grpc.insecure_channel(ADDR_PORT) as channel: #server_IP_addr:port_num
    
    #create client stub
        stub = Boo_pb2_grpc.BookingServiceStub(channel)
        print(stub)
        #get response from Registration service
    
        #output = stub.getAllFlights(Boo_pb2.getAllFlightsRequest(giorno=int(giorno), mese=int(mese), anno=int(anno), aereoporto_arrivo=aereoporto_arrivo, aereoporto_partenza=aereoporto_partenza, persone=int(persone)))
        for entry in stub.getAllFlights(Boo_pb2.getAllFlightsRequest(giorno=int(giorno), mese=int(mese), anno=int(anno), aereoporto_arrivo=aereoporto_arrivo, aereoporto_partenza=aereoporto_partenza, persone=int(persone))):
            print(entry.id)
            output = output + 1
        #output = stub.SendId(Boo_pb2.IdMessage(id = "stringa"))
        #we need to return the boolean value
        print("ciao")
        return output


