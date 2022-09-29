import grpc
import time

from concurrent import futures
from datetime import datetime
from proto import FroMan_pb2
from proto import FroMan_pb2_grpc

from ManUtils import *

class FlightsInfoServicer(FroMan_pb2_grpc.FlightsInfoServicer):

    def AddFlight(self, NewFlight, context):
        #sanity checks are the following:
        #   1) Id should not exist yet
        #   2) Date should exist (e.g. it cannot be '31-04-2023')
        #   3) Departure airport != arrival airport
        #   4) Airline should be either EasyJet or ITA or Ryanair
        #   5) Price should be a number and it should be greater than zero
        #   6) Seats should be greater than zero

        isNewFlightId = checkFlightId(NewFlight.id)                 #condition 1)
        isExistentDate = checkDateExistance(NewFlight.date)         #condition 2)
        isValidAirline = (NewFlight.airline=='EasyJet' or NewFlight.airline=='ITA' or NewFlight.airline=='Ryanair')     #condition 4)
        isValidPrice = NewFlight.price.replace('.','',1).isdigit()  #condition 5)

        isOk = (isNewFlightId and isExistentDate and NewFlight.departureAirport!=NewFlight.arrivalAirport and isValidAirline and isValidPrice and NewFlight.seats>0)

        if isOk:
            registerFlight(NewFlight.id, NewFlight.date, NewFlight.departureAirport, NewFlight.arrivalAirport, NewFlight.departureTime, NewFlight.arrivalTime, NewFlight.airline, NewFlight.price, NewFlight.seats)

#create gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
FroMan_pb2_grpc.add_FlightsInfoServicer_to_server(FlightsInfoServicer(), server)

print('Starting server. Listening on port 50052.')
server.add_insecure_port('[::]:50052')
server.start()

try:
    while True:
        time.sleep(86400)   #86400 seconds == 24 hours
except KeyboardInterrupt:
    server.stop(0)