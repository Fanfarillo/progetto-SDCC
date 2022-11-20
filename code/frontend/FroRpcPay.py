import grpc
import time

from proto import Payment_pb2
from proto import Payment_pb2_grpc


# -------------------------------------------------- DISCOVERY ----------------------------------------------
ADDR_PORT = ''
DISCOVERY_SERVER = 'code_discovery_2:50060'
# -------------------------------------------------- DISCOVERY ----------------------------------------------


# --------------------------------------DISCOVERY -----------------------------
"""
Ha il compito di recuperare la porta su cui
il microservizio payment è in ascolto.
"""
def discovery_payment():
    global ADDR_PORT
    """
    Si tenta di contattare il discovery server registrato
    per ottenere la porta su cui il servizio di payment è in
    ascolto. Se la chiamata dovesse fallire, si attendono 5
    secondi per poi eseguire nuovamente il tentativo di connessione.
    """
    while(True):
        try:
            # Provo a connettermi al server.
            channel = grpc.insecure_channel(DISCOVERY_SERVER)
            stub = Discovery_pb2_grpc.DiscoveryServiceStub(channel)
            # Ottengo la porta su cui il microservizio di Payment è in ascolto.
            res = stub.get(Discovery_pb2.GetRequest(serviceName="frontend" , serviceNameTarget="payment"))
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


def sendPayment(username, card, postiSelezionati, dataPagamento, prezzoBase, prezzoSelezionePosti, prezzoServiziAggiuntivi, prezzoTotale, serviziSelezionati, email):

# -------------------------------- DISCOVERY -------------------------------------------------------------------
    """
    Verifico se il fronted già è a conoscenza della porta
    su cui contattare il micorservizio di payment.
    """
    if (ADDR_PORT == ''):
        discovery_payment()
# -------------------------------- DISCOVERY -------------------------------------------------------------------

    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    #create client stub
    stub = Payment_pb2_grpc.PayStub(channel)

    #get response from Payment service
    output = stub.AddPayment(Payment_pb2.NewPayment(username=username, idVolo=card.idVolo, selectedSeats=postiSelezionati, paymentDate=dataPagamento, basePrice=prezzoBase, seatsPrice=prezzoSelezionePosti, servicesPrice=prezzoServiziAggiuntivi, totalPrice=prezzoTotale, numStivaMedi=serviziSelezionati.bagaglioStivaMedio, numStivaGrandi=serviziSelezionati.bagaglioStivaGrande, numBagagliSpeciali=serviziSelezionati.bagaglioSpeciale, numAssicurazioni=serviziSelezionati.assicurazioneBagagli, numAnimali=serviziSelezionati.animaleDomestico, numNeonati=serviziSelezionati.neonato, email=email))
    #we need to return the boolean value
    return output.isOk   
