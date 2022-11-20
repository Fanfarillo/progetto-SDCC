import grpc
import time

from proto import Managment_pb2
from proto import Managment_pb2_grpc
from proto import Discovery_pb2
from proto import Discovery_pb2_grpc


# -------------------------------------------------- DISCOVERY ----------------------------------------------
ADDR_PORT = ''
DISCOVERY_SERVER = 'code_discovery_1:50060'
# -------------------------------------------------- DISCOVERY ----------------------------------------------




class AdditionalServices:
    def __init__(self, bagaglioSpeciale, bagaglioStivaMedio, bagaglioStivaGrande, assicurazioneBagagli, animaleDomestico, neonato):
        self.bagaglioStivaMedio = bagaglioStivaMedio
        self.animaleDomestico = animaleDomestico
        self.assicurazioneBagagli = assicurazioneBagagli
        self.bagaglioStivaGrande = bagaglioStivaGrande
        self.bagaglioSpeciale = bagaglioSpeciale
        self.neonato = neonato



class SeatsFlight:
    def __init__(self, primo, secondo, terzo, quarto, quinto):
        self.primo = primo
        self.secondo = secondo
        self.terzo = terzo
        self.quarto = quarto
        self.quinto = quinto




# -------------------------------- DISCOVERY -------------------------------------------------------------------
"""
Ha il compito di recuperare la porta su cui
il microservizio di Management è in ascolto.
"""
def discovery_management():
    global ADDR_PORT
    """
    Si tenta di contattare il discovery server registrato
    per ottenere la porta su cui il servizio di management è in
    ascolto. Se la chiamata dovesse fallire, si attendono 5
    secondi per poi eseguire nuovamente il tentativo di connessione.
    """
    while(True):
        try:
            # Provo a connettermi al server.
            channel = grpc.insecure_channel(DISCOVERY_SERVER)
            stub = Discovery_pb2_grpc.DiscoveryServiceStub(channel)
            # Ottengo la porta su cui il microservizio di Management è in ascolto.
            res = stub.get(Discovery_pb2.GetRequest(serviceName="frontend" , serviceNameTarget="management"))
            if (res.port == -1):
                # Il discovery server ancora non è a conoscenza della porta richiesta.
                time.sleep(5)
                continue            
            ADDR_PORT = res.serviceName + ':' + res.port
            break
        except:
            # Problema nella connessione con il server.
            time.sleep(5)
            continue
# -------------------------------- DISCOVERY -------------------------------------------------------------------


def sendIdCompanySeatsPrice(compagnia):   
# -------------------------------- DISCOVERY -------------------------------------------------------------------
    """
    Verifico se il fronted già è a conoscenza della porta
    su cui contattare il micorservizio di management.
    """
    if (ADDR_PORT == ''):
        discovery_management()
# -------------------------------- DISCOVERY -------------------------------------------------------------------

    # Apertura di un gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    # Creazione del client stub
    stub = Managment_pb2_grpc.FlightsInfoStub(channel)

    output = []
    # Ottengo uno stream di messaggio da parte del Server
    for entry in stub.GetAllSeatsFlight(Managment_pb2.SeatCostRequest(compagnia=compagnia)):
        output.append(entry.prezzo)
    
    """
    output[0] = primo
    output[1] = secondo
    output[2] = terzo
    output[3] = quarto
    output[4] = quinto   
    """
    
    seatsFlight = SeatsFlight(output[0], output[1], output[2], output[3], output[4])
    return seatsFlight



def sendIdCompanyAdditionalService(compagnia):
 # -------------------------------- DISCOVERY -------------------------------------------------------------------
    """
    Verifico se il fronted già è a conoscenza della porta
    su cui contattare il micorservizio di management.
    """
    if (ADDR_PORT == ''):
        discovery_management()
# -------------------------------- DISCOVERY -------------------------------------------------------------------

    # Apertura di un gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    # Creazione del client stub
    stub = Managment_pb2_grpc.FlightsInfoStub(channel)

    output = []
    # Ottengo uno stream di messaggio da parte del Server
    for entry in stub.GetAlladditionalServicesFlight(Managment_pb2.AdditionalServiceCostRequest(compagnia=compagnia)):
        output.append(entry.prezzo)

    """
    output[0] = bagaglioSpeciale
    output[1] = bagaglioStivaMedio
    output[2] = bagaglioStivaGrande
    output[3] = assicurazioneBagagli
    output[4] = animaleDomestico
    output[5] = neonato
    """

    additionalServices = AdditionalServices(output[0], output[1], output[2], output[3], output[4], output[5])
    return additionalServices



def sendNewFlight(id, date, departureAirport, arrivalAirport, departureTime, arrivalTime, airline, price, seats):
# -------------------------------- DISCOVERY -------------------------------------------------------------------
    """
    Verifico se il fronted già è a conoscenza della porta
    su cui contattare il micorservizio di management.
    """
    if (ADDR_PORT == ''):
        discovery_management()
# -------------------------------- DISCOVERY -------------------------------------------------------------------

    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    #create client stub
    stub = Managment_pb2_grpc.FlightsInfoStub(channel)

    #get response from Flights Management service
    output = stub.AddFlight(Managment_pb2.NewFlight(id=id, date=date, departureAirport=departureAirport, arrivalAirport=arrivalAirport, departureTime=departureTime, arrivalTime=arrivalTime, airline=airline, price=price, seats=seats))
    return output



def sendNewPrice(flightId, newPrice):
 # -------------------------------- DISCOVERY -------------------------------------------------------------------
    """
    Verifico se il fronted già è a conoscenza della porta
    su cui contattare il micorservizio di management.
    """
    if (ADDR_PORT == ''):
        discovery_management()
# -------------------------------- DISCOVERY -------------------------------------------------------------------

    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    #create client stub
    stub = Managment_pb2_grpc.FlightsInfoStub(channel)

    #get response from Flights Management service
    output = stub.ModifyFlight(Managment_pb2.UpdatedFlight(flightId=flightId, newPrice=newPrice))
    return output



def sendSeatsPrices(airline, price1, price2, price6, price16, price18):
# -------------------------------- DISCOVERY -------------------------------------------------------------------
    """
    Verifico se il fronted già è a conoscenza della porta
    su cui contattare il micorservizio di management.
    """
    if (ADDR_PORT == ''):
        discovery_management()
# -------------------------------- DISCOVERY -------------------------------------------------------------------

    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    #create client stub
    stub = Managment_pb2_grpc.FlightsInfoStub(channel)

    #get response from Flights Management service
    output = stub.ModifySeats(Managment_pb2.UpdatedSeats(airline=airline, price1=price1, price2=price2, price6=price6, price16=price16, price18=price18))
    return output



def sendServicesPrices(airline, priceBM, priceBG, priceBS, priceAD, priceAB, priceTN):
# -------------------------------- DISCOVERY -------------------------------------------------------------------
    """
    Verifico se il fronted già è a conoscenza della porta
    su cui contattare il micorservizio di management.
    """
    if (ADDR_PORT == ''):
        discovery_management()
# -------------------------------- DISCOVERY -------------------------------------------------------------------

    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    #create client stub
    stub = Managment_pb2_grpc.FlightsInfoStub(channel)

    #get response from Flights Management service
    output = stub.ModifyServices(Managment_pb2.UpdatedServices(airline=airline, priceBM=priceBM, priceBG=priceBG, priceBS=priceBS, priceAD=priceAD, priceAB=priceAB, priceTN=priceTN))
    return output
