import grpc
from proto import Booking_pb2
from proto import Booking_pb2_grpc



ADDR_PORT = 'localhost:50053'   #server_IP_addr:port_num



class Result:
    def __init__(self, cards, num):
        self.cards = cards
        self.num = num



class Card:
    def __init__(self, idVolo, compagnia, arrivo, partenza, orario, data, prezzoTotale):
        self.idVolo = idVolo
        self.compagnia = compagnia
        self.arrivo = arrivo
        self.partenza = partenza
        self.orario = orario
        self.data = data
        self.prezzoTotale = prezzoTotale



def sendBookingInfo(giorno, mese, anno, aereoporto_partenza, aereoporto_arrivo, persone):
    #open gRPC channel
    print("entrato...")
    cards = []
    count = 0
    with grpc.insecure_channel(ADDR_PORT) as channel: #server_IP_addr:port_num
    
    #create client stub
        stub = Booking_pb2_grpc.BookingServiceStub(channel)
        print(stub)
        #get response from Registration service
        print("LOG: prima del ciclo...")
        #output = stub.getAllFlights(Boo_pb2.getAllFlightsRequest(giorno=int(giorno), mese=int(mese), anno=int(anno), aereoporto_arrivo=aereoporto_arrivo, aereoporto_partenza=aereoporto_partenza, persone=int(persone)))
        for entry in stub.getAllFlights(Booking_pb2.getAllFlightsRequest(giorno=int(giorno), mese=int(mese), anno=int(anno), aereoporto_arrivo=aereoporto_arrivo, aereoporto_partenza=aereoporto_partenza, persone=int(persone))):
            print(entry.id)
            count = count + 1
            cards.append(Card(entry.id, entry.compagnia, entry.arrivo, entry.partenza, entry.orario, entry.data, entry.prezzoBase))
        #output = stub.SendId(Boo_pb2.IdMessage(id = "stringa"))
        #we need to return the boolean value
        result = Result(cards, count)
        return result



def sendIdVoloPostiDisponibili(idVolo):
    #open gRPC channel
    print("entrato...")
    with grpc.insecure_channel(ADDR_PORT) as channel: #server_IP_addr:port_num
        count = 0
    #create client stub
        stub = Booking_pb2_grpc.BookingServiceStub(channel)
        print(stub)
        #get response from Registration service
        print("LOG: prima del ciclo...")
        #output = stub.getAllFlights(Boo_pb2.getAllFlightsRequest(giorno=int(giorno), mese=int(mese), anno=int(anno), aereoporto_arrivo=aereoporto_arrivo, aereoporto_partenza=aereoporto_partenza, persone=int(persone)))
        for entry in stub.getAllAvailableSeatsForFlight(Booking_pb2.AvailableSeatRequest(idVolo = idVolo)):
            print(entry.idPosto)
            count = count + 1


