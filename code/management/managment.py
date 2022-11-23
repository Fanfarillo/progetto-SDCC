import grpc
import time
import logging

from concurrent import futures
from datetime import datetime

from proto import Managment_pb2
from proto import Managment_pb2_grpc

from ManRpcBoo import *
from ManUtils import *
from ManDB import *
from ManDiscov import *



"""
La seguente lista contiene inizialmente solo il
default discovery server per il microservizio di Management.
Tuttavia, nel momento in cui si registra, all'interno possono
essere inserite le informazioni relative all'altro
discovery server.
"""
all_discovery_servers = ['code_discovery_1:50060']

CHUNK_DIM = 1000




class FlightsInfoServicer(Managment_pb2_grpc.FlightsInfoServicer):



    def getLogFileMan(self, request, context):
    	# Logging.
        logger.info("[LOGGING] richiesta dati di logging...\n\n")
        r = -1
        q = -1
        
        
        f = open("managment.log","r")
        
        contenuto = f.read()
        
        dim = len(contenuto)
        
        q = dim // CHUNK_DIM
        r = dim % CHUNK_DIM
        
        if(q==0):
        	yield Managment_pb2.GetLogFileReplyMan(chunk_file = contenuto.encode(), num_chunk  =0)
        else:
        	count = 0        
        	for i in range(0, q):
        		try:
        			yield Managment_pb2.GetLogFileReplyMan(chunk_file = contenuto[i*CHUNK_DIM:i*CHUNK_DIM+CHUNK_DIM].encode(), num_chunk  =i)
        		except:
        			logger.info("[LOGGING] Dati di logging inviati senza successo...")
        		count = count + 1
        	if(r > 0):
        		lower_bound = count * CHUNK_DIM
        		yield Managment_pb2.GetLogFileReplyMan(chunk_file = contenuto[lower_bound:lower_bound+r].encode(), num_chunk  =count)
        logger.info("[LOGGING] Dati di logging inviati con successo...")
        # open file 
        f.close()



    def AddFlight(self, NewFlight, context):
        #sanity checks are the following:
        #   1) Id should not exist yet
        #   2) Date should exist (e.g. it cannot be '31-04-2023')
        #   3) Date should be future
        #   4) Departure airport != arrival airport
        #   5) Airline should be either EasyJet or ITA or Ryanair
        #   6) Price should be a number and it should be greater than zero
        #   7) Seats should be greater than zero

        logger.info("Richiesta di aggiunta di un nuovo volo: [" + NewFlight.id + "," + NewFlight.date + "," + NewFlight.departureAirport + "," + NewFlight.arrivalAirport + "," + NewFlight.departureTime + "," + NewFlight.arrivalTime + "," + NewFlight.airline + "," + NewFlight.price + "]")

        isNewFlightId = checkFlightId(NewFlight.id, logger, all_discovery_servers)                 #condition 1)
        isExistentDate = checkDateExistance(NewFlight.date)         #condition 2)
        if isExistentDate:
            isFutureDate = checkFutureDate(NewFlight.date)          #condition 3)
        isValidAirline = (NewFlight.airline=='EasyJet' or NewFlight.airline=='ITA' or NewFlight.airline=='Ryanair')     #condition 5)
        isValidPrice = NewFlight.price.replace('.','',1).isdigit()  #condition 6)

        isOk = False    #isOk will be True only if ALL the conditions are satisfied

        if not isNewFlightId:
            err = "ESISTE GIÀ UN VOLO CON QUESTO ID.\nPROVA A INSERIRE NUOVAMENTE I DATI DEL VOLO."
        elif not isExistentDate:
            err = "LA DATA INSERITA NON ESISTE.\nPROVA A INSERIRE NUOVAMENTE I DATI DEL VOLO."
        elif not isFutureDate:
            err = "LA DATA INSERITA DEVE ESSERE SUCCESSIVA A QUELLA ODIERNA.\nPROVA A INSERIRE NUOVAMENTE I DATI DEL VOLO."
        elif NewFlight.departureAirport==NewFlight.arrivalAirport:
            err = "L'AEROPORTO DI PARTENZA COINCIDE CON QUELLO DI ARRIVO.\nPROVA A INSERIRE NUOVAMENTE I DATI DEL VOLO."
        elif not isValidAirline:
            err = "LA COMPAGNIA AEREA SELEZIONATA NON È VALIDA.\nPROVA A INSERIRE NUOVAMENTE I DATI DEL VOLO."
        elif not isValidPrice:
            err = "IL PREZZO DEL VOLO NON È STATO SCRITTO CORRETTAMENTE.\nPROVA A INSERIRE NUOVAMENTE I DATI DEL VOLO."
        elif NewFlight.seats<=0:
            err = "IL NUMERO DI POSTI A SEDERE DEVE ESSERE MAGGIORE DI ZERO.\nPROVA A INSERIRE NUOVAMENTE I DATI DEL VOLO."
        else:
            isOk = True
            err = None

        if isOk:
            #questa funzione arrotonda alla seconda cifra dopo la virgola (per difetto) il valore di NewFlight.price
            roundedPrice = roundPrice(NewFlight.price)
            #we can decide to do something with return value of registerFlight; at the moment we will not use it
            registerFlight(NewFlight.id, NewFlight.date, NewFlight.departureAirport, NewFlight.arrivalAirport, NewFlight.departureTime, NewFlight.arrivalTime, NewFlight.airline, roundedPrice, NewFlight.seats, logger, all_discovery_servers)

        output = Managment_pb2.AddResponse(isOk=isOk, error=err)
        return output



    def ModifyFlight(self, UpdatedFlight, context):
        #sanity checks are the following:
        #   1) Flight id should already exist
        #   2) Price should be a number and it should be greater than zero

        logger.info("Richiesta di modifica del prezzo di un volo: [" + UpdatedFlight.flightId + "," + UpdatedFlight.newPrice + "]")

        isExistentFlightId = not checkFlightId(UpdatedFlight.flightId, logger, all_discovery_servers)       #condition 1)
        isValidPrice = UpdatedFlight.newPrice.replace('.','',1).isdigit()                                   #condition 2)

        isOk = False    #isOk will be True only if ALL the conditions are satisfied

        if not isExistentFlightId:
            err = "NON ESISTE UN VOLO CON QUESTO ID.\nPROVA A INSERIRE NUOVAMENTE I DATI DEL VOLO."
        elif not isValidPrice:
            err = "IL PREZZO DEL VOLO NON È STATO SCRITTO CORRETTAMENTE.\nPROVA A INSERIRE NUOVAMENTE I DATI DEL VOLO."
        else:
            isOk = True
            err = None

        if isOk:
            roundedPrice = roundPrice(UpdatedFlight.newPrice)
            #we can decide to do something with return value of registerFlight; at the moment we will not use it
            updateFlightPrice(UpdatedFlight.flightId, roundedPrice, logger, all_discovery_servers)

        output = Managment_pb2.ModFlightResponse(isOk=isOk, error=err)
        return output



    def ModifySeats(self, UpdatedSeats, context):

        logger.info("Richiesta di modifica del prezzo dei posti a sedere: [" + UpdatedSeats.airline + ", fila 1: €" + UpdatedSeats.price1 + ", file 2-5: €" + UpdatedSeats.price2 + ", file 6-15: €" + UpdatedSeats.price6 + ", file 16-17: €" + UpdatedSeats.price16 + ", file 18-25: €" + UpdatedSeats.price18 + "]")

        #all the prices should be numbers and should be greater than zero
        isOk = (UpdatedSeats.price1.replace('.','',1).isdigit() and UpdatedSeats.price2.replace('.','',1).isdigit() and UpdatedSeats.price6.replace('.','',1).isdigit() and UpdatedSeats.price16.replace('.','',1).isdigit() and UpdatedSeats.price18.replace('.','',1).isdigit())

        #if all the prices are ok, then save them into remote database (DynamoDB)
        if isOk:
            err = None
            roundedPrice1 = roundPrice(UpdatedSeats.price1)
            roundedPrice2 = roundPrice(UpdatedSeats.price2)
            roundedPrice6 = roundPrice(UpdatedSeats.price6)
            roundedPrice16 = roundPrice(UpdatedSeats.price16)
            roundedPrice18 = roundPrice(UpdatedSeats.price18)
            storeSeatsPrices(UpdatedSeats.airline, roundedPrice1, roundedPrice2, roundedPrice6, roundedPrice16, roundedPrice18)      
        else:
            err = "QUALCHE PREZZO NON È STATO SCRITTO CORRETTAMENTE.\nPROVA A INSERIRE NUOVAMENTE I PREZZI."

        output = Managment_pb2.ModSeatsResponse(isOk=isOk, error=err)
        return output



    def ModifyServices(self, UpdatedServices, context):

        logger.info("Richiesta di modifica del prezzo dei servizi aggiuntivi: [" + UpdatedServices.airline + ", stiva medio: €" + UpdatedServices.priceBM + ", stiva grande: €" + UpdatedServices.priceBG + ", bagaglio speciale: €" + UpdatedServices.priceBS + ", animale: €" + UpdatedServices.priceAD + ", assicurazione: €" + UpdatedServices.priceAB + ", neonato: €" + UpdatedServices.priceTN + "]")

        #all the prices should be numbers and should be greater than zero
        isOk = (UpdatedServices.priceBM.replace('.','',1).isdigit() and UpdatedServices.priceBG.replace('.','',1).isdigit() and UpdatedServices.priceBS.replace('.','',1).isdigit() and UpdatedServices.priceAD.replace('.','',1).isdigit() and UpdatedServices.priceAB.replace('.','',1).isdigit() and UpdatedServices.priceTN.replace('.','',1).isdigit())

        if isOk:
            err = None
            roundedPriceBM = roundPrice(UpdatedServices.priceBM)
            roundedPriceBG = roundPrice(UpdatedServices.priceBG)
            roundedPriceBS = roundPrice(UpdatedServices.priceBS)
            roundedPriceAD = roundPrice(UpdatedServices.priceAD)
            roundedPriceAB = roundPrice(UpdatedServices.priceAB)
            roundedPriceTN = roundPrice(UpdatedServices.priceTN)
            storeServicesPrices(UpdatedServices.airline, roundedPriceBM, roundedPriceBG, roundedPriceBS, roundedPriceAD, roundedPriceAB, roundedPriceTN)
        else:
            err = "QUALCHE PREZZO NON È STATO SCRITTO CORRETTAMENTE.\nPROVA A INSERIRE NUOVAMENTE I PREZZI."

        output = Managment_pb2.ModServicesResponse(isOk=isOk, error=err)
        return output



    def GetPriceFlight(self, request, context):

        logger.info("Richiesta del prezzo del volo " + request.idVolo + ".")

        response = getPrice(request.idVolo)
        return Managment_pb2.PriceReply(price=str(response))



    """
    Recupera il prezzo dei posti relativi alla
    compagnia area passata come parametro. Il
    prezzo di tali posti viene inserito all'interno
    della struttura dati seguendo un ordine predefinito.
    """
    def GetAllSeatsFlight(self, request, context):
        """
        1. 1
        2. 2-5
        3. 6-15
        4. 16-17
        5. 18-26
        """
        logger.info("Richiesta del prezzo dei posti per la compagnia area " + request.compagnia + ".")
        prezzi = getAllSeatsFlight(request.compagnia)

        for item in prezzi:
            ret = Managment_pb2.SeatCostReply(prezzo=str(item))            
            yield ret



    """
    Recupera il prezzo dei servizi aggiuntivi
    che vengono offerti dalla compagnia area
    passata come parametro. Il prezzo di tali
    servizi viene inserito all'interno della
    struttura dati seguendo un ordine predefinito.
    """
    def GetAlladditionalServicesFlight(self, request, context):
        """
        1. bagaglioSpeciale
        2. bagaglioStivaMedio
        3. bagaglioStivaGrande
        4. assicurazioneBagagli
        5. animaleDomestico
        6. neonato
        """
        logger.info("Richiesta del prezzo dei servizi aggiuntivi offerti dalla compagnia area " + request.compagnia + ".")
        prezzi = getAlladditionalServicesFlight(request.compagnia)

        for item in prezzi:
            ret = Managment_pb2.AdditionalServiceCostReply(prezzo=str(item))
            yield ret



"""
Costruisco un file di LOG in cui andare ad
inserire le richieste che giungono dagli altri
microservizi. Inoltre, inserisco delle informazioni
di warnings nel momento in cui le richieste falliscono.
"""
logging.basicConfig(filename="managment.log", format=f'%(levelname)s - %(asctime)s - %(message)s')
logger = logging.getLogger("managmentInfo")
logger.setLevel(logging.INFO)



#create gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
Managment_pb2_grpc.add_FlightsInfoServicer_to_server(FlightsInfoServicer(), server)



logger.info('Avvio del server in ascolto sulla porta 50052...')
server.add_insecure_port('[::]:50052')
server.start()
logger.info('Server avviato con successo.')




# ------------------------------------------- DISCOVERY -------------------------------------------------------------------------------------------

"""
Registrazione del microservizio al Discovery Server di default.
Inizialmente il microservizio di management è a conoscenza solamente
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
