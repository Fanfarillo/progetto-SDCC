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




class FlightsInfoServicer(Managment_pb2_grpc.FlightsInfoServicer):




    def AddFlight(self, NewFlight, context):
        #sanity checks are the following:
        #   1) Id should not exist yet
        #   2) Date should exist (e.g. it cannot be '31-04-2023')
        #   3) Date should be future
        #   4) Departure airport != arrival airport
        #   5) Airline should be either EasyJet or ITA or Ryanair
        #   6) Price should be a number and it should be greater than zero
        #   7) Seats should be greater than zero

        logger.info("Messaggio Matteo...")

        isNewFlightId = checkFlightId(NewFlight.id)                 #condition 1)
        isExistentDate = checkDateExistance(NewFlight.date)         #condition 2)
        if isExistentDate:
            isFutureDate = checkFutureDate(NewFlight.date)          #condition 3)
        isValidAirline = (NewFlight.airline=='EasyJet' or NewFlight.airline=='ITA' or NewFlight.airline=='Ryanair')     #condition 5)
        isValidPrice = NewFlight.price.replace('.','',1).isdigit()  #condition 6)

        isOk = (isNewFlightId and isExistentDate and isFutureDate and NewFlight.departureAirport!=NewFlight.arrivalAirport and isValidAirline and isValidPrice and NewFlight.seats>0)

        if isOk:
            #we can decide to do something with return value of registerFlight; at the moment we will not use it
            registerFlight(NewFlight.id, NewFlight.date, NewFlight.departureAirport, NewFlight.arrivalAirport, NewFlight.departureTime, NewFlight.arrivalTime, NewFlight.airline, NewFlight.price, NewFlight.seats)

        output = Managment_pb2.AddResponse(isOk=isOk)
        return output




    def ModifyFlight(self, UpdatedFlight, context):
        #sanity checks are the following:
        #   1) Flight id should already exist
        #   2) Price should be a number and it should be greater than zero

        logger.info("Messaggio Matteo...")

        isExistentFlightId = not checkFlightId(UpdatedFlight.flightId)      #condition 1)
        isValidPrice = UpdatedFlight.newPrice.replace('.','',1).isdigit()   #condition 2)

        isOk = isExistentFlightId and isValidPrice

        if isOk:
            #we can decide to do something with return value of registerFlight; at the moment we will not use it
            updateFlightPrice(UpdatedFlight.flightId, UpdatedFlight.newPrice)

        output = Managment_pb2.ModFlightResponse(isOk=isOk)
        return output




    def ModifySeats(self, UpdatedSeats, context):

        logger.info("Messaggio Matteo...")

        #all the prices should be numbers and should be greater than zero
        isOk = (UpdatedSeats.price1.replace('.','',1).isdigit() and UpdatedSeats.price2.replace('.','',1).isdigit() and UpdatedSeats.price6.replace('.','',1).isdigit() and UpdatedSeats.price16.replace('.','',1).isdigit() and UpdatedSeats.price18.replace('.','',1).isdigit())

        #if all the prices are ok, then save them into remote database (DynamoDB)
        if isOk:
            storeSeatsPrices(UpdatedSeats.airline, UpdatedSeats.price1, UpdatedSeats.price2, UpdatedSeats.price6, UpdatedSeats.price16, UpdatedSeats.price18)

        output = Managment_pb2.ModSeatsResponse(isOk=isOk)
        return output




    def ModifyServices(self, UpdatedServices, context):

        logger.info("Messaggio Matteo...")

        #all the prices should be numbers and should be greater than zero
        isOk = (UpdatedServices.priceBM.replace('.','',1).isdigit() and UpdatedServices.priceBG.replace('.','',1).isdigit() and UpdatedServices.priceBS.replace('.','',1).isdigit() and UpdatedServices.priceAD.replace('.','',1).isdigit() and UpdatedServices.priceAB.replace('.','',1).isdigit() and UpdatedServices.priceTN.replace('.','',1).isdigit())

        if isOk:
            storeServicesPrices(UpdatedServices.airline, UpdatedServices.priceBM, UpdatedServices.priceBG, UpdatedServices.priceBS, UpdatedServices.priceAD, UpdatedServices.priceAB, UpdatedServices.priceTN)

        output = Managment_pb2.ModServicesResponse(isOk=isOk)
        return output




    def GetPriceFlight(self, request, context):

        logger.info("Messaggio Matteo...")

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
        logger.info("Richiesta del prezzo dei posti per la compagnia area " + request.compagnia + "...")
        prezzi = getAllSeatsFlight(request.compagnia)

        for item in prezzi:
            ret = Managment_pb2.SeatCostReply(prezzo=int(item))            
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
        logger.info("Richiesta del prezzo dei servizi aggiuntivi offerti dalla compagnia area " + request.compagnia + "...")
        prezzi = getAlladditionalServicesFlight(request.compagnia)

        for item in prezzi:
            ret = Managment_pb2.AdditionalServiceCostReply(prezzo=int(item))
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




logger.info('Avvio del server in ascolto sulla porta 50051...')
server.add_insecure_port('[::]:50052')
server.start()
logger.info('Server avviato con successo...')




try:
    while True:
        time.sleep(86400)   #86400 seconds == 24 hours
except KeyboardInterrupt:
    server.stop(0)
