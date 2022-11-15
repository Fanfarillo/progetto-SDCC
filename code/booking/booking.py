import grpc
import time
import logging

from concurrent import futures
from proto import Booking_pb2
from proto import Booking_pb2_grpc

from BooDB import *
from BooDiscov import *


postiTotali = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5',
'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'A10', 'B10', 'C10', 'D10', 'E10', 'F10',
'A11', 'B11', 'C11', 'D11', 'E11', 'F11', 'A12', 'B12', 'C12', 'D12', 'E12', 'F12', 'A13', 'B13', 'C13', 'D13', 'E13', 'F13', 'A14', 'B14', 'C14', 'D14', 'E14', 'F14', 'A15', 'B15', 'C15', 'D15', 'E15', 'F15',
'A16', 'B16', 'C16', 'D16', 'E16', 'F16', 'A17', 'B17', 'C17', 'D17', 'E17', 'F17', 'A18', 'B18', 'C18', 'D18', 'E18', 'F18', 'A19', 'B19', 'C19', 'D19', 'E19', 'F19', 'A20', 'B20', 'C20', 'D20', 'E20', 'F20',
"A21", "B21", "C21", "D21", "E21", "F21", "A22", "B22", "C22", "D22", "E22", "F22", "A23", "B23", "C23", "D23", "E23", "F23", "A24", "B24", "C24", "D24", "E24", "F24", "A25", "B25", "C25", "D25", "E25", "F25",
"A26", "B26", "C26", "D26", "E26", "F26"]



"""
La seguente lista contiene inizialmente solo il
default discovery server per il microservizio di booking.
Tuttavia, nel momento in cui si registra, all'interno possono
essere inserite le informazioni relative all'altro
discovery server.
"""
all_discovery_servers = ['code_discovery_1:50060']

CHUNK_DIM = 1000




class BookingInfoServicer(Booking_pb2_grpc.BookingServiceServicer):


    def getLogFileBoo(self, request, context):
    	# Logging.
        logger.info("[LOGGING] richiesta dati di logging...\n\n")
        r = -1
        q = -1
        
        
        f = open("booking.log","r")
        
        contenuto = f.read()
        
        dim = len(contenuto)
        
        q = dim // CHUNK_DIM
        r = dim % CHUNK_DIM
        
        if(q==0):
        	yield Booking_pb2.GetLogFileReplyBoo(chunk_file = contenuto.encode(), num_chunk  =0)
        else:
        	count = 0        
        	for i in range(0, q):
        		try:
        			yield Booking_pb2.GetLogFileReplyBoo(chunk_file = contenuto[i:i+CHUNK_DIM].encode(), num_chunk  =i)
        		except:
        			logger.info("[LOGGING] Dati di logging inviati senza successo...")
        		count = count + 1
        	if(r > 0):
        		lower_bound = count * CHUNK_DIM
        		yield Booking_pb2.GetLogFileReplyBoo(chunk_file = contenuto[lower_bound:lower_bound+r].encode(), num_chunk  =count)
        logger.info("[LOGGING] Dati di logging inviati con successo...")
        # open file 
        f.close()
        f = open("booking.log", "r+") 
  
        # absolute file positioning
        f.seek(0) 
  
        # to erase all data 
        f.truncate()
        f.close()






    """
    Recupera tutti i voli attualmente disponibili
    che rispettano i criteri di selezione passati
    come parametri.
    """
    def getAllFlights(self, request, context):
        logger.info("Richiesta dei voli disponibili: [" + str(request.giorno) + "," + str(request.mese) + "," + str(request.anno) + "," + request.aeroporto_arrivo + "," + request.aeroporto_partenza + "]")
        
        """
        Recupero tutti i voli relativi ai parametri
        della richiesta ricevuta.
        """
        flights = retrieveFlights(request.giorno, request.mese, request.anno, request.aeroporto_arrivo, request.aeroporto_partenza, all_discovery_servers, logger)
        
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



    def GetAirports(self, AirportsRequest, context):
        if AirportsRequest.isDummy:
            logger.info("Recupero dummy degli aeroporti.")
            departures = ["Fiumicino (Roma)", "Heathrow (Londra)", "Charles De Gaulle (Parigi)"]
            arrivals = ["Fiumicino (Roma)", "Heathrow (Londra)", "Charles De Gaulle (Parigi)"]

        else:
            logger.info("Recupero degli aeroporti coinvolti nei voli disponibili.")
            departures = retrieveDepartures()
            arrivals = retrieveArrivals()

        output = Booking_pb2.AirportsResponse(departureAirports=departures, arrivalAirports=arrivals)
        return output



    def SendId(self, IdMessage, context):
        #check if the id was not used for an other available flight
        isNew = isNewId(IdMessage.id)
        if isNew:
            logger.info("[REGISTRAZIONE DI UN NUOVO VOLO] L'ID del nuovo volo non è ancora presenta all'interno del sistema, per cui il volo potrà essere aggiunto correttamente.")
        else:
            logger.info("[REGISTRAZIONE DI UN NUOVO VOLO] L'ID del nuovo volo è già presente all'interno del sistema, per cui il volo non potrà essere aggiunto.")
        output = Booking_pb2.IdResponse(isOk=isNew)
        return output




    def RegisterFlight(self, NewFlight2, context):
        logger.info("Registrazione del nuovo volo in corso...")
        storeFlight(NewFlight2.id, NewFlight2.date, NewFlight2.departureAirport, NewFlight2.arrivalAirport, NewFlight2.departureTime, NewFlight2.arrivalTime, NewFlight2.airline, NewFlight2.price, NewFlight2.seats)
        output = Booking_pb2.RegisterResponse(isOk=True)
        return output




    def UpdateFlightPrice(self, UpdatedFlight2, context):
        logger.info("Aggiornamento del prezzo del volo in corso...")
        storeUpdatedFlight(UpdatedFlight2.flightId, UpdatedFlight2.newPrice)
        output = Booking_pb2.UpdateResponse(isOk=True)
        return output
    


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



logger.info('Avvio del server in ascolto sulla porta 50053...')
server.add_insecure_port('[::]:50053')
server.start()
logger.info('Server avviato con successo.')


# ------------------------------------------- DISCOVERY -------------------------------------------------------------------------------------------

"""
Registrazione del microservizio al Discovery Server di default.
Inizialmente il microservizio di booking è a conoscenza solamente
del discovery server 1
"""
logger.info('[DISCOVERY SERVER] Richiesta registrazione del microservizio sul discovery server ...')
discovery_servers = put_discovery_server(all_discovery_servers, logger)
logger.info('[DISCOVERY SERVER] Registrazione del microservizio sul discovery server ' + all_discovery_servers[0] + ' avvenuta con successo...')




# Registro l'eventuale altro discovery server
for item in discovery_servers:
    try:
        all_discovery_servers.index(item)
    except:
        # Inserisco il Discovery Server mancante all'interno della lista.
        all_discovery_servers.append(item)


logger.info('[DISCOVER SERVERS LIST] I discovery servers noti sono:\n')
for item in all_discovery_servers:
    logger.info(item + '\n')
logger.info('\n\n')

# ------------------------------------------- DISCOVERY -------------------------------------------------------------------------------------------

try:
    while True:
        time.sleep(86400)   #86400 seconds == 24 hours
except KeyboardInterrupt:
    server.stop(0)
