import grpc
import time
import logging

from concurrent import futures
from proto import Payment_pb2
from proto import Payment_pb2_grpc

from PayDB import *
from PayUtils import *

class PayServicer(Payment_pb2_grpc.PayServicer):

    def AddPayment(self, NewPayment, context):
        logger.info("Richiesta di pagamento per il volo " + NewPayment.idVolo + " da parte di " + NewPayment.username + ".")

        """
        Per prima cosa, bisogna memorizzare le informazioni strettamente legate al pagamento nell'apposita tabella;
        dopodiché si contatta il microservizio Booking per passargli lo username dell'utente e i posti che vengono occupati da lui,
        in modo tale da aggiornare correttamente la tabella PostiOccupati.
        NB: gli aggiornamenti della tabella relativa al pagamento e della tabella PostiOccupati costituiscono una transazione all-or-nothing per cui,
        se dovessero esserci problemi nell'aggiornamento di PostiOccupati, dal lato pagamento bisogna effettuare il rollback della scrittura.
        E' qui che interviene il design pattern Saga per i microservizi.
        """
        
        selectedSeatsStr = listToString(NewPayment.selectedSeats)   #conversione della lista di posti selezionati in un'unica stringa

        #store delle informazioni legate al pagamento; qui idVolo e selectedSeats insieme formano la chiave primaria, per cui dovranno essere utilizzate per l'eventuale rimozione delle informazioni dal db dovuta a un rollback
        storePayment(NewPayment.idVolo, selectedSeatsStr, NewPayment.username, NewPayment.paymentDate, NewPayment.basePrice, NewPayment.seatsPrice, NewPayment.servicesPrice, NewPayment.totalPrice, NewPayment.numStivaMedi, NewPayment.numStivaGrandi, NewPayment.numBagagliSpeciali, NewPayment.numAssicurazioni, NewPayment.numAnimali, NewPayment.numNeonati, NewPayment.email)

        #TODO: un sacco di roba

        output = Payment_pb2.PayResponse(isOk=isOk)
        return output


"""
Costruisco un file di LOG in cui andare ad
inserire le richieste che giungono dagli altri
microservizi. Inoltre, inserisco delle informazioni
di warnings nel momento in cui le richieste falliscono.
"""
logging.basicConfig(filename="payment.log", format=f'%(levelname)s - %(asctime)s - %(message)s')
logger = logging.getLogger("paymentInfo")
logger.setLevel(logging.INFO)


#create gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
Payment_pb2_grpc.add_PayServicer_to_server(PayServicer(), server)


logger.info('Avvio del server in ascolto sulla porta 50055...')
server.add_insecure_port('[::]:50055')
server.start()
logger.info('Server avviato con successo.')


try:
    while True:
        time.sleep(86400)   #86400 seconds == 24 hours
except KeyboardInterrupt:
    server.stop(0)
