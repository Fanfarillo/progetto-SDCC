import grpc
import time

from concurrent import futures
from proto import Boo_pb2
from proto import Boo_pb2_grpc
from BooDB import *

class BookingInfoServicer(Boo_pb2_grpc.BookingServiceServicer):

    """def getAllFlights(self, request, context):
        flights = retrieveFlights(request.giorno, request.mese, request.anno, request.aereoporto_arrivo, request.aereoporto_partenza, request.persone)
        for flight in flights:
            ret = Boo_pb2.getAllFlightsReply(id = flight.idKey, compagnia = flight.compagnia_aerea, flight.arrivo, flight.partenza, flight.data, flight.orario)
            print("ciao2")
            yield ret"""
    
    def SendId(self, IdMessage, context):
        #check if the id was not used for an other available flight
        isNew = isNewId(IdMessage.id)
        print("ci")
        output = Boo_pb2.IdResponse(isOk=isNew)
        return output

    def RegisterFlight(self, NewFlight2, context):
        storeFlight(NewFlight2.id, NewFlight2.date, NewFlight2.departureAirport, NewFlight2.arrivalAirport, NewFlight2.departureTime, NewFlight2.arrivalTime, NewFlight2.airline, NewFlight2.price, NewFlight2.seats)
        output = Boo_pb2.RegisterResponse(isOk=True)
        return output

    def UpdateFlightPrice(self, UpdatedFlight2, context):
        storeUpdatedFlight(UpdatedFlight2.flightId, UpdatedFlight2.newPrice)
        output = Boo_pb2.UpdateResponse(isOk=True)
        return output

#create gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
Boo_pb2_grpc.add_BookingServiceServicer_to_server(BookingInfoServicer(), server)

print('Starting server. Listening on port 50053.')
server.add_insecure_port('[::]:50053')
server.start()

#server.wait_for_termination()

try:
    while True:
        time.sleep(86400)   #86400 seconds == 24 hours
except KeyboardInterrupt:
    server.stop(0)
