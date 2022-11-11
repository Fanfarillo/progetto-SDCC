import grpc

from proto import Booking_pb2
from proto import Booking_pb2_grpc

# ADDR_PORT = 'booking:50053'   #server_IP_addr:port_num
# -------------------------------------------------- DISCOVERY ----------------------------------------------
ADDR_PORT = ''
# -------------------------------------------------- DISCOVERY ----------------------------------------------



# ----------------------------------------------------- DISCOVERY --------------------------------------------
def discovery_booking_micro(all_discovery_servers, logger):
    ok = False
    while(True):
        """
        Itero sui discovery servers noti al microservizio
        per ottenere la porta ricercata.
        """
        for discovery in all_discovery_servers:
            try:
                channel = grpc.insecure_channel(discovery)
                stub = Discovery_pb2_grpc.DiscoveryServiceStub(channel)
                res = stub.get(Discovery_pb2.GetRequest(serviceName="management" , serviceNameTarget="booking"))
            except:
                # Si è verificato un problema nella connessione con il discovery server
                logger.info('[ PUT DISCOVERY MANAGEMENT] Problema connessione con il discovery server ' + discovery_server + '.')
                time.sleep(2)
                continue
            if (res.port == '-1'):
                logger.info('[ PUT DISCOVERY MANAGEMENT] porta ancora non conosciuta dal discovery server ' + discovery_server + ' riprovare...')
                time.sleep(2)
                continue
            ok = True
            logger.info('[ PUT DISCOVERY MANAGEMENT] porta del servizio di management recuperata: ' + res.port + '.')
            ADDR_PORT = res.serviceName + ':' + res.port
            break
        if(ok):
            break
        time.sleep(5)
# ----------------------------------------------------- DISCOVERY --------------------------------------------




def checkFlightId(id, logger, all_discovery_servers):
# -------------------------------- DISCOVERY -------------------------------------------------------------------
    if (ADDR_PORT == ''):
        discovery_booking_micro(all_discovery_servers, logger)
# -------------------------------- DISCOVERY -------------------------------------------------------------------

    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num
    
    #create client stub
    stub = Booking_pb2_grpc.BookingServiceStub(channel)

    #get response from Flights Management service
    output = stub.SendId(Booking_pb2.IdMessage(id=id))
    #we need to return the boolean value
    return output.isOk

def registerFlight(id, date, departureAirport, arrivalAirport, departureTime, arrivalTime, airline, price, seats, logger, all_discovery_servers):
# -------------------------------- DISCOVERY -------------------------------------------------------------------
    if (ADDR_PORT == ''):
        discovery_booking_micro(all_discovery_servers, logger)
# -------------------------------- DISCOVERY -------------------------------------------------------------------

    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    #create client stub
    stub = Booking_pb2_grpc.BookingServiceStub(channel)

    #get response from Flights Management service
    output = stub.RegisterFlight(Booking_pb2.NewFlight2(id=id, date=date, departureAirport=departureAirport, arrivalAirport=arrivalAirport, departureTime=departureTime, arrivalTime=arrivalTime, airline=airline, price=price, seats=seats))
    #we need to return the boolean value
    return output.isOk

def updateFlightPrice(flightId, newPrice, logger, all_discovery_servers):
# -------------------------------- DISCOVERY -------------------------------------------------------------------
    if (ADDR_PORT == ''):
        discovery_booking_micro(all_discovery_servers, logger)
# -------------------------------- DISCOVERY -------------------------------------------------------------------

    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    #create client stub
    stub = Booking_pb2_grpc.BookingServiceStub(channel)

    #get response from Flights Management service
    output = stub.UpdateFlightPrice(Booking_pb2.UpdatedFlight2(flightId=flightId, newPrice=newPrice))
    #we need to return the boolean value
    return output.isOk
