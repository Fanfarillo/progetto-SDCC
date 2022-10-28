import grpc
import time
import logging

from concurrent import futures
from proto import Booking_pb2
from proto import Booking_pb2_grpc
from BooDB import *




postiTotali = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1','A2', 'B2', 'C2', 'D2', 'E2', 'F2','A3', 'B3', 'C3', 'D3', 'E3', 'F3',
'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5','A6', 'B6', 'C6', 'D6', 'E6', 'F6','A7', 'B7', 'C7', 'D7', 'E7', 'F7',
'A8', 'B8', 'C8', 'D8', 'E8', 'F8','A9', 'B9', 'C9', 'D9', 'E9', 'F10','A10', 'B10', 'C10', 'D10', 'E10', 'F10','A11', 'B11', 'C11', 'D11', 'E11', 'F11',
'A12', 'B12', 'C12', 'D12', 'E12', 'F12', 'A13', 'B13', 'C13', 'D13', 'E13', 'F13','A14', 'B14', 'C14', 'D14', 'E14', 'F14','A15', 'B15', 'C1', 'D15', 'E15', 'F15','A16', 'B16', 'C16', 'D16', 'E16', 'F16',
'A17', 'B17', 'C17', 'D17', 'E17', 'F17','A18', 'B18', 'C18', 'D18', 'E18', 'F18','A19', 'B19', 'C19', 'D19', 'E19', 'F19','A20', 'B20', 'C20', 'D20', 'E20', 'F20',
"A21", "B21", "C21", "D21", "E21", "F21","A22", "B22", "C22", "D22", "E22", "F22","A23", "B23", "C23", "D23", "E23", "F23","A24", "B24", "C24", "D24", "E24", "F24",
"A25", "B25", "C25", "D25", "E25", "F25","A26", "B26", "C26", "D26", "E26", "F26"]




class BookingInfoServicer(Booking_pb2_grpc.BookingServiceServicer):




    """
    Recupera tutti i voli attualmente disponibili
    che rispettano i criteri di selezione passati
    come parametri.
    """
    def getAllFlights(self, request, context):
        logger.info("Richiesta dei voli disponibili: [" + str(request.giorno) + "," + str(request.mese) + "," + str(request.anno) + "," + request.aereoporto_arrivo + "," + request.aereoporto_partenza + "]")
        
        """
        Recupero tutti i voli relativi ai parametri
        della richiesta ricevuta.
        """
        flights = retrieveFlights(request.giorno, request.mese, request.anno, request.aereoporto_arrivo, request.aereoporto_partenza)
        
        for flight in flights:
            postiDisp = Booking_pb2.postiDisponibili()

            """
            Tengo traccia del numero totale posti
            """
            count = 0

            """
            Fissato un volo, itero su tutti i posti
            disponibili per tale volo andandoli ad
            aggiungere all'interno della struttura
            dati che contiene la lista dei posti
            disponibili per tale volo.
            """
            for posto in flight.postiDisponibili:
                count = count + 1
                postiDisp.posti.append(posto)
            
            """
            Tra tutti i voli disponibili che corrispondono
            ai parametri richiesti, si scartano tutti quelli
            che hanno un numero di posti disponibili pari a zero
            o inferiore. Questo controllo può essere visto come
            un ulteriore controllo di sicurezza.
            """
            if len(postiDisp.posti) > 0:
                ret = Booking_pb2.getAllFlightsReply(id = flight.idKey, compagnia = flight.compagnia_aerea, arrivo = flight.arrivo, partenza = flight.partenza, data = flight.data, orario = flight.orario, prezzoBase = flight.prezzo, posti = postiDisp, numPosti = count)
                yield ret




    def SendId(self, IdMessage, context):
        #check if the id was not used for an other available flight
        isNew = isNewId(IdMessage.id)
        if isNew:
            logger.info("Messaggio Matteo...")
        else:
            logger.info("Messaggio Matteo...")
        output = Booking_pb2.IdResponse(isOk=isNew)
        return output




    def RegisterFlight(self, NewFlight2, context):
        logger.info("Messaggio Matteo...")
        storeFlight(NewFlight2.id, NewFlight2.date, NewFlight2.departureAirport, NewFlight2.arrivalAirport, NewFlight2.departureTime, NewFlight2.arrivalTime, NewFlight2.airline, NewFlight2.price, NewFlight2.seats)
        output = Booking_pb2.RegisterResponse(isOk=True)
        return output




    def UpdateFlightPrice(self, UpdatedFlight2, context):
        logger.info("Messaggio Matteo...")
        storeUpdatedFlight(UpdatedFlight2.flightId, UpdatedFlight2.newPrice)
        output = Booking_pb2.UpdateResponse(isOk=True)
        return output
    



    """
    Recupera tutti i posti che sono attualmente
    disponibili per il volo il cui identificativo
    è passato al metodo.
    
    def getAllAvailableSeatsForFlight(self, request, context):
        logger.info("Richiesta dei posti disponibili per il volo " + request.idVolo)
        postiDisponibili = retrieveAvailableSeats(request.idVolo, postiTotali)
        for posto in postiDisponibili:
            ret = Booking_pb2.AvailableSeatReply(idPosto = posto)
            yield ret
    """



"""
Costruisco un file di LOG in cui andare ad
inserire le richieste che giungono dagli altri
microservizi. Inoltre, inserisco delle informazioni
di warnings nel momento in cui le richieste falliscono.
"""
logging.basicConfig(filename="booking.log", format=f'%(levelname)s - %(asctime)s - %(message)s')
logger = logging.getLogger("bookingInfo")
logger_warnings = logging.getLogger("bookingWarnings")
logger.setLevel(logging.INFO)
logger_warnings.setLevel(logging.WARNING)




#create gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
Booking_pb2_grpc.add_BookingServiceServicer_to_server(BookingInfoServicer(), server)




logger.info('Avvio del server in ascolto sulla porta 50051...')
server.add_insecure_port('[::]:50053')
server.start()
logger.info('Server avviato con successo...')




try:
    while True:
        time.sleep(86400)   #86400 seconds == 24 hours
except KeyboardInterrupt:
    server.stop(0)
