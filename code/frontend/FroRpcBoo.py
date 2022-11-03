import grpc
from proto import Booking_pb2
from proto import Booking_pb2_grpc

ADDR_PORT = 'booking:50053'



class Result:
    def __init__(self, cards, num):
        self.cards = cards
        self.num = num




class Card:
    def __init__(self, idVolo, compagnia, arrivo, partenza, orario, data, prezzoBase, posti, numPosti):
        # Identificativo del volo
        self.idVolo = idVolo
        # Compagnia aerea
        self.compagnia = compagnia
        # Aereoporto di arrivo
        self.arrivo = arrivo
        # Aereoporto di partenza
        self.partenza = partenza
        # Orario di partenza del volo
        self.orario = orario
        # Data del volo
        self.data = data
        # Prezzo totale
        self.prezzoBase = prezzoBase
        # Lista dei posti disponibili
        self.posti = posti
        # Numero dei posti disponibili
        self.numPosti = numPosti




"""
Ha il compito di costruire la lista di Card contenenti
le informazioni relative ai voli che corrispondono ai
dati inseriti dall'utente. Bisogna tener conto anche del
fatto che l'utente ha richiesto di prenotare un certo
numero N di biglietti. I voli che devono essere restituiti
hanno la disponibilità richiesta dall'utente (i.e., Disponibilità >= N)
"""
def sendBookingInfo(giorno, mese, anno, aereoporto_partenza, aereoporto_arrivo):
    cards = []
    count = 0
    #with grpc.insecure_channel(ADDR_PORT) as channel: #server_IP_addr:port_num
    channel = grpc.insecure_channel(ADDR_PORT)
    stub = Booking_pb2_grpc.BookingServiceStub(channel)
    # Costruisco la lista delle Cards contenenti le informazioni relative ai voli.
    for entry in stub.getAllFlights(Booking_pb2.getAllFlightsRequest(giorno=int(giorno), mese=int(mese), anno=int(anno), aereoporto_arrivo=aereoporto_arrivo, aereoporto_partenza=aereoporto_partenza)):
        count = count + 1
        cards.append(Card(entry.id, entry.compagnia, entry.arrivo, entry.partenza, entry.orario, entry.data, entry.prezzoBase, entry.posti, entry.numPosti))
    result = Result(cards, count)
    return result

