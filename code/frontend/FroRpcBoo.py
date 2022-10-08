import grpc

from proto import Boo_pb2
from proto import Boo_pb2_grpc

ADDR_PORT = 'localhost:50053'   #server_IP_addr:port_num


class Result:
    def __init__(self, cards, num):
        self.cards = cards
        self.num = num


class Card:
    def __init__(self, idVolo, compagnia, arrivo, partenza, orario, data):
        self.idVolo = idVolo
        self.compagnia = compagnia
        self.arrivo = arrivo
        self.partenza = partenza
        self.orario = orario
        self.data = data

def sendBookingInfo(giorno, mese, anno, aereoporto_partenza, aereoporto_arrivo, persone):
    #open gRPC channel
    print("entrato...")
    cards = []
    count = 0
    with grpc.insecure_channel(ADDR_PORT) as channel: #server_IP_addr:port_num
    
    #create client stub
        stub = Boo_pb2_grpc.BookingServiceStub(channel)
        print(stub)
        #get response from Registration service
    
        #output = stub.getAllFlights(Boo_pb2.getAllFlightsRequest(giorno=int(giorno), mese=int(mese), anno=int(anno), aereoporto_arrivo=aereoporto_arrivo, aereoporto_partenza=aereoporto_partenza, persone=int(persone)))
        for entry in stub.getAllFlights(Boo_pb2.getAllFlightsRequest(giorno=int(giorno), mese=int(mese), anno=int(anno), aereoporto_arrivo=aereoporto_arrivo, aereoporto_partenza=aereoporto_partenza, persone=int(persone))):
            print(entry.id)
            count = count + 1
            cards.append(Card(entry.id, entry.compagnia, entry.arrivo, entry.partenza, entry.orario, entry.data))
        #output = stub.SendId(Boo_pb2.IdMessage(id = "stringa"))
        #we need to return the boolean value
        result = Result(cards, count)
        return result


