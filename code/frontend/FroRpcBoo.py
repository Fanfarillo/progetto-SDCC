import grpc
from proto import Booking_pb2
from proto import Booking_pb2_grpc

ADDR_PORT = 'booking:50053'


class CardResult:
    def __init__(self, cards, num):
        self.cards = cards
        self.num = num


class Card:
    def __init__(self, idVolo, compagnia, arrivo, partenza, orario, data, prezzoBase, posti, numPosti):
        # Identificativo del volo
        self.idVolo = idVolo
        # Compagnia aerea
        self.compagnia = compagnia
        # Aeroporto di arrivo
        self.arrivo = arrivo
        # Aeroporto di partenza
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


class AirportResult:
    def __init__(self, departures, arrivals):
        self.departures = departures    #tutti gli aeroporti di partenza
        self.arrivals = arrivals        #tutti gli aeroporti di arrivo



"""
Ha il compito di costruire la lista di Card contenenti
le informazioni relative ai voli che corrispondono ai
dati inseriti dall'utente. Bisogna tener conto anche del
fatto che l'utente ha richiesto di prenotare un certo
numero N di biglietti. I voli che devono essere restituiti
hanno la disponibilità richiesta dall'utente (i.e., Disponibilità >= N)
"""
def sendBookingInfo(giorno, mese, anno, aeroporto_partenza, aeroporto_arrivo):
    cards = []
    count = 0

    #with grpc.insecure_channel(ADDR_PORT) as channel: #server_IP_addr:port_num
    channel = grpc.insecure_channel(ADDR_PORT)
    stub = Booking_pb2_grpc.BookingServiceStub(channel)

    # Costruisco la lista delle Cards contenenti le informazioni relative ai voli.
    for entry in stub.getAllFlights(Booking_pb2.getAllFlightsRequest(giorno=int(giorno), mese=int(mese), anno=int(anno), aeroporto_arrivo=aeroporto_arrivo, aeroporto_partenza=aeroporto_partenza)):
        count = count + 1
        cards.append(Card(entry.id, entry.compagnia, entry.arrivo, entry.partenza, entry.orario, entry.data, entry.prezzoBase, entry.posti, entry.numPosti))
    result = CardResult(cards, count)
    return result


"""
Ha il compito di costruire un oggetto composto da due liste di aeroporti.
La prima lista contiene gli aeroporti di partenza di tutti i voli,
mentre la seconda contiene gli aeroporti di arrivo di tutti i voli.
"""
def retrieveAirports():
    departures = []
    arrivals = []

    channel = grpc.insecure_channel(ADDR_PORT)
    stub = Booking_pb2_grpc.BookingServiceStub(channel)

    #costruisco le liste degli aeroporti di partenza e di arrivo
    output = stub.GetAirports(Booking_pb2.AirportsRequest(isDummy=False))
    for airport in output.departureAirports:
        departures.append(airport)
    for airport in output.arrivalAirports:
        arrivals.append(airport)
    
    result = AirportResult(departures, arrivals)
    return result
