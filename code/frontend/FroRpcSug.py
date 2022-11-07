import grpc

from proto import Suggestions_pb2
from proto import Suggestions_pb2_grpc


ADDR_PORT = 'suggestions:50054'


def getNumDaysBefore(card, today):
    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    #create client stub
    stub = Suggestions_pb2_grpc.SuggestionsServiceStub(channel)

    #get response from Payment service
    output = stub.GetSelectedFlight(Suggestions_pb2.SelectedFlight(bookingDate=today, flightDate=card.data, airline=card.compagnia, departureAirport=card.partenza, arrivalAirport=card.arrivo))
    #we need to return the numeric value
    return output.numDaysBeforeConvenient
