import grpc
import time

from proto import Suggestions_pb2
from proto import Suggestions_pb2_grpc
from proto import Discovery_pb2
from proto import Discovery_pb2_grpc


# -------------------------------------------------- DISCOVERY ----------------------------------------------
ADDR_PORT = ''
DISCOVERY_SERVER = 'code_discovery_2:50060'
# -------------------------------------------------- DISCOVERY ----------------------------------------------


# --------------------------------------DISCOVERY -----------------------------
"""
Ha il compito di recuperare la porta su cui
il microservizio suggestions è in ascolto.
"""
def discovery_suggestions():
    global ADDR_PORT
    """
    Si tenta di contattare il discovery server registrato
    per ottenere la porta su cui il servizio di suggestions è in
    ascolto. Se la chiamata dovesse fallire, si attendono 5
    secondi per poi eseguire nuovamente il tentativo di connessione.
    """
    while(True):
        try:
            # Provo a connettermi al server.
            channel = grpc.insecure_channel(DISCOVERY_SERVER)
            stub = Discovery_pb2_grpc.DiscoveryServiceStub(channel)
            # Ottengo la porta su cui il microservizio di Payment è in ascolto.
            res = stub.get(Discovery_pb2.GetRequest(serviceName="frontend" , serviceNameTarget="suggestions"))
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
# --------------------------------------DISCOVERY -----------------------------


def getNumDaysBefore(card, today):

# -------------------------------- DISCOVERY -------------------------------------------------------------------
    """
    Verifico se il fronted già è a conoscenza della porta
    su cui contattare il micorservizio di payment.
    """
    if (ADDR_PORT == ''):
        discovery_suggestions()
# -------------------------------- DISCOVERY -------------------------------------------------------------------

    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    #create client stub
    stub = Suggestions_pb2_grpc.SuggestionsServiceStub(channel)

    #get response from Payment service
    output = stub.GetSelectedFlight(Suggestions_pb2.SelectedFlight(bookingDate=today, flightDate=card.data, airline=card.compagnia, departureAirport=card.partenza, arrivalAirport=card.arrivo))
    #we need to return the numeric value
    return output.numDaysBeforeConvenient
