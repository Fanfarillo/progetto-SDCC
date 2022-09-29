import grpc
import time

from concurrent import futures
from proto import BooMan_pb2
from proto import BooMan_pb2_grpc
from BooDB import *

class FlightsAndPricesServicer(FroMan_pb2_grpc.FlightsAndPricesServicer):

    def SendId(self, IdMessage, context):
        #check if the id was not used for an other available flight
        isNew = isNewId(IdMessage.id)

        output = BooMan_pb2.IdResponse(isOk=isNew)
        return output

    def RegisterFlight(self, NewFlight, context):
        storeFlight(NewFlight.id, NewFlight.date, NewFlight.departureAirport, NewFlight.arrivalAirport, NewFlight.departureTime, NewFlight.arrivalTime, NewFlight.airline, NewFlight.price, NewFlight.seats)

        output = BooMan_pb2.RegisterResponse(isOk=True)
        return output
        
#create gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
BooMan_pb2_grpc.add_FlightsAndPricesServicer_to_server(FlightsAndPricesServicer(), server)

print('Starting server. Listening on port 50053.')
server.add_insecure_port('[::]:50053')
server.start()

try:
    while True:
        time.sleep(86400)   #86400 seconds == 24 hours
except KeyboardInterrupt:
    server.stop(0)
