import grpc
import time
import logging

from concurrent import futures
from proto import Payment_pb2
from proto import Payment_pb2_grpc

from PayDB import *
from PayUtils import *
from PayDiscov import *
from PayMqProducer import *
from PayMqConsumer import *


# ------------------------------------------------------ DISCOVERY -----------------------------------------------------
"""
La seguente lista contiene inizialmente solo il
default discovery server per il microservizio di Payment.
Tuttavia, nel momento in cui si registra, all'interno possono
essere inserite le informazioni relative all'altro
discovery server.
"""
all_discovery_servers = ['code_discovery_2:50060']
# ------------------------------------------------------ DISCOVERY -----------------------------------------------------
CHUNK_DIM = 1000


class PayServicer(Payment_pb2_grpc.PayServicer):


    def getLogFilePay(self, request, context):
    	# Logging.
        logger.info("[LOGGING] richiesta dati di logging...\n\n")
        r = -1
        q = -1
        
        
        f = open("payment.log","r")
        
        contenuto = f.read()
        
        dim = len(contenuto)
        
        q = dim // CHUNK_DIM
        r = dim % CHUNK_DIM
        
        if(q==0):
        	yield Registration_pb2.GetLogFileReplyReg(chunk_file = contenuto.encode(), num_chunk  =0)
        else:
        	count = 0        
        	for i in range(0, q):
        		try:
        			yield Registration_pb2.GetLogFileReplyReg(chunk_file = contenuto[i:i+CHUNK_DIM].encode(), num_chunk  =i)
        		except:
        			logger.info("[LOGGING] Dati di logging inviati senza successo...")
        		count = count + 1
        	if(r > 0):
        		lower_bound = count * CHUNK_DIM
        		yield Registration_pb2.GetLogFileReplyReg(chunk_file = contenuto[lower_bound:lower_bound+r].encode(), num_chunk  =count)
        logger.info("[LOGGING] Dati di logging inviati con successo...")
        # open file 
        f.close()
        f = open("payment.log", "r+") 
  
        # absolute file positioning
        f.seek(0) 
  
        # to erase all data 
        f.truncate()
        f.close()



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

        #invio di username e lista di posti selezionati a Booking mediante una coda di messaggi
        sendMqBooking(NewPayment.username, selectedSeatsStr, logger)

        #ricezione di un messaggio da parte di Booking indicante se la transazione complessa è andata a buon fine o meno
        isFinalized = receiveMqBooking(logger)

        #se la transazione NON è andata a buon fine, allora si effettua il rollback della porzione di transazione già effettuata in Payment
        if not isFinalized:
            deletePayment(NewPayment.idVolo, selectedSeatsStr)

        output = Payment_pb2.PayResponse(isOk=isFinalized)
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


# ------------------------------------------- DISCOVERY -------------------------------------------------------------------------------------------

"""
Registrazione del microservizio al Discovery Server di default.
Inizialmente il microservizio di registration è a conoscenza solamente
del discovery server 2
"""
logger.info('[DISCOVERY SERVER] Richiesta registrazione del microservizio sul discovery server ...')
discovery_servers = put_discovery_server(all_discovery_servers, logger)
logger.info('[DISCOVERY SERVER] Registrazione del microservizio sul discovery server ' + all_discovery_servers[0] + ' avvenuta con successo...')




# Registro l'eventuale altro discovery server
for item in discovery_servers:
    try:
        all_discovery_servers.index(item)
    except:
        # Inserisco il Discovery Server mancante all'interno della lista.
        all_discovery_servers.append(item)


logger.info('[DISCOVER SERVERS LIST] I discovery servers noti sono:\n')
for item in all_discovery_servers:
    logger.info(item + '\n')
logger.info('\n\n')

# ------------------------------------------- DISCOVERY -------------------------------------------------------------------------------------------


try:
    while True:
        time.sleep(86400)   #86400 seconds == 24 hours
except KeyboardInterrupt:
    server.stop(0)
