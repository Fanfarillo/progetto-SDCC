import time
import logging
import grpc

from proto import Discovery_pb2
from proto import Discovery_pb2_grpc
from proto import Managment_pb2
from proto import Managment_pb2_grpc
from proto import Booking_pb2
from proto import Booking_pb2_grpc
from proto import Registration_pb2
from proto import Registration_pb2_grpc
from proto import Payment_pb2
from proto import Payment_pb2_grpc
from proto import Suggestions_pb2
from proto import Suggestions_pb2_grpc

from concurrent import futures


class Microservizio:
    def __init__(self, nome, porta, conn):
        self.nome = nome
        self.porta = porta
        self.conn = conn



# Crea l'associazione tra il microservizi e il file di LOG.
class LogFileMicro:
    def __init__(self, nome, f):
        self.nome = nome
        self.f = f



logger = None
logger_warnings = None

# Questi sono i nomi con cui i microservizi si sono registrati.
MICROSERVICES = ["booking", "management", "registration", "payment", "code_suggestions_1"]

# la lista contiene tutti entrambi i discovery server.
ALL_DISCOVERY_SERVERS = ['code_discovery_1:50060', 'code_discovery_2:50060']

# la lista contenente le connnessioni verso i microservizi.
grpc_connections = []

# la lista contenente gli oggetti Python per scrivere all'interno dei file di LOG.
files = []



"""
Questa funzione deve creare il file di
Log in cui il server centralizzato può 
registrare gli eventi di ricezione dei dati.
"""
def log_file():
    global logger
    global logger_warnings

    """
    Costruisco un file di LOG in cui andare a
    registrare gli eventi relativi alla ricezione
    del contenuto dei file di LOG dai microservizi.
    """
    logging.basicConfig(filename="server_logging.log", format=f'%(levelname)s - %(asctime)s - %(message)s')
    logger = logging.getLogger("server_logging_info")
    logger_warnings = logging.getLogger("server_logging_warning")
    logger.setLevel(logging.INFO)
    logger_warnings.setLevel(logging.WARNING)




"""
Recupero le porte su cui i microservizi sono
in ascolto. Successivamente, stabilisco le
connessioni con questi microservizi per poi
poter ottenere i dati di monitoraggio.
"""
def set_conn_micro():
    global grpc_connections

    """
    Tengo traccia dei microservizi di cui
    ancora non ho ottenuto la porta.
    """
    microservizi_rimanenti = MICROSERVICES.copy()

    # Itero finché non ho recuperato tutte le porte necessarie.
    count = 0
    # Ottenfo il numero dei microservizi da monitorare.
    dim = len(MICROSERVICES)

    while(count < dim):
        """
        Itero sui discovery servers per ottenere
        la porta del microservizio ricercata.
        """
        for discovery in ALL_DISCOVERY_SERVERS:
            if (count >= dim):
                # L'iterazione precedente ha risolto tutte le porte.
                break
            # Itero sui discovery servers
            try:
                # Provo a connettermi al Discovery server.
                channel = grpc.insecure_channel(discovery)
                stub = Discovery_pb2_grpc.DiscoveryServiceStub(channel)
            except:
                # Si è verificato un problema nella connessione con il discovery server e passo al discovery server successivo
                logger.info('[ GET DISCOVERY SERVICE] Problema connessione con il discovery server ' + discovery + '.\n')
                time.sleep(2)
                continue
            """
            La connessione al Discovery Server è stata
            completata con successo. Recupero la porta
            su cui sono in ascolto i servizi.
            """
            microservizi_da_rimuovere = []
            for service in microservizi_rimanenti:
                try:
                    res = stub.get(Discovery_pb2.GetRequest(serviceName="log server" , serviceNameTarget=service))
                except:
                    logger.info('[ GET DISCOVERY SERVICE] errore nel recupero della porta del microservizio '+ service + ' dal discovery server ' + discovery + ' riprovare...\n')
                    time.sleep(2)
                    # Passo al discovery server successivo poiché ho avuto un problema con questo discovery server.
                    break

                """
                Sono riuscito a contattare correttamente il discovery server.
                Faccio un controllo sul valore della porta che mi è stato ritornato.
                """
                if (res.port == '-1'):
                    logger.info('[ GET DISCOVERY SERVICE] porta del micoroservizio '+ service +' ancora non registrata nel discovery server ' + discovery + ' riprovare...\n')
                    time.sleep(2)
                    # Passo al servizio successivo.
                    continue
                logger.info('[ GET DISCOVERY SERVICE] porta del servizio di '+ service +'recuperata: ' + res.port + ' dal discovery server '+ discovery +'.\n')
                # Aggiungo il microservizio alla lista in modo da connettermi successivamente.
                grpc_connections.append(Microservizio(res.serviceName, res.port, None))
                # Registro il fatto che il servizio che è stato recuperato con successo.
                count = count + 1
                microservizi_da_rimuovere.append(service)

            # Rimuovo i servizi che sono stati recuperati con successo.
            for service in microservizi_da_rimuovere:
                try:
                    microservizi_rimanenti.remove(service)
                except:
                    logger.info("[ GET DISCOVERY SERVICE] Errore nella rimozione del servizio " + service + ".\n")
    
    # Ho recuperato tutte quante le porte dei microservizi.

    count = 0
    conn_concluse = []
    """
    Creo le connessioni grpc verso i microservizi
    di cui ho precedentemente recuperato le porte.
    """
    while(count < dim):
        for grpc_conn in grpc_connections:
            try:
                conn_concluse.index(grpc_conn.nome)
                # la connessione è stata già stabilita e passo alla successiva.
                continue
            except:
                logger.info("[ CONNESSIONI ] Tentativo di connessione al microservizio di " + grpc_conn.nome + "...\n")
            
            try:
                # Creazione del canale.
                channel = grpc.insecure_channel(grpc_conn.nome+':'+grpc_conn.porta)

                # Creazione dello stub correto.
                if(grpc_conn.nome == "booking"):
                    stub = Booking_pb2_grpc.BookingServiceStub(channel)
                elif(grpc_conn.nome == "management"):
                    stub = Managment_pb2_grpc.FlightsInfoStub(channel)
                elif(grpc_conn.nome == "registration"):
                    stub = Registration_pb2_grpc.UsersInfoStub(channel)
                elif(grpc_conn.nome == "payment"):
                    stub = Payment_pb2_grpc.PayStub(channel)
                elif(grpc_conn.nome == "code_suggestions_1"):
                    stub = Suggestions_pb2_grpc.SuggestionsServiceStub(channel)
            
                grpc_conn.conn = stub

                # Registro il fatto che questa connessione si è conclusa con successo.
                logger.info("[ CONNESSIONI ] Tentativo di connessione al microservizio di " + grpc_conn.nome + " avvenuta con successo.\n")
                count = count + 1
                conn_concluse.append(grpc_conn.nome)
            except:
                time.sleep(2)
                continue

    # Ho stabilito le connessioni con tuti i microservizi.





"""
Questa funzione crea i file di log per
i microservizi che devono essere monitorati.
"""
def log_file_microservizi():
    global files
    for grpc_conn in grpc_connections:
        f = open(grpc_conn.nome + '.log', "w")
        files.append(LogFileMicro(grpc_conn.nome, f))




"""
Questa funzione si occupa di recuperare il
contenuto dei file di LOG dei microservizi.
"""
def run_logger():
    # Contatore delle richieste che vengono fatte ai microservizi
    count = 0
    for item in files:
        if(item.nome=="booking"):
            boo = item
        elif(item.nome=="management"):
            man = item
        elif(item.nome=="registration"):
            reg = item
        elif(item.nome=="payment"):
            pay = item
        elif(item.nome=="code_suggestions_1"):
            sug = item

    while(True):
        count = count + 1
        for grpc_conn in grpc_connections:
            
            # Distinguo i microservizi da contattare.
            if(grpc_conn.nome ==  "booking"):
                try:
                    for response in grpc_conn.conn.getLogFileBoo(Booking_pb2.GetLogFileRequestBoo(numRichiesta=count)):
                        logging_info = response.chunk_file.decode()
                        boo.f.write(logging_info)
                        boo.f.flush()
                        logger.info("[ LOGGING ] Richiesta al microservizio di Booking completata con successo.\n")
                except:
                    logger.info("[ LOGGING ] Errore nella ricezione dei dati da parte del servizio di Booking.\n")
            elif(grpc_conn.nome ==  "management"):
                try:
                    for response in grpc_conn.conn.getLogFileMan(Managment_pb2.GetLogFileRequestMan(numRichiesta=count)):
                        logging_info = response.chunk_file.decode()
                        man.f.write(logging_info)
                        man.f.flush()
                        logger.info("[ LOGGING ] Richiesta al microservizio di Management completata con successo.\n")
                except:
                    logger.info("[ LOGGING ] Errore nella ricezione dei dati da parte del servizio di Management.\n")
            elif(grpc_conn.nome ==  "registration"):
                try:
                    for response in grpc_conn.conn.getLogFileReg(Registration_pb2.GetLogFileRequestReg(numRichiesta=count)):
                        logging_info = response.chunk_file.decode()
                        reg.f.write(logging_info)
                        reg.f.flush()
                        logger.info("[ LOGGING ] Richiesta al microservizio di Registration completata con successo.\n")
                except:
                    logger.info("[ LOGGING ] Errore nella ricezione dei dati da parte del servizio di Registration.\n")
            elif(grpc_conn.nome ==  "payment"):
                try:
                    for response in grpc_conn.conn.getLogFilePay(Payment_pb2.GetLogFileRequestPay(numRichiesta=count)):
                        logging_info = response.chunk_file.decode()
                        pay.f.write(logging_info)
                        pay.f.flush()
                        logger.info("[ LOGGING ] Richiesta al microservizio di Payment completata con successo.\n")
                except:
                    logger.info("[ LOGGING ] Errore nella ricezione dei dati da parte del servizio di Payment.\n")
            elif(grpc_conn.nome ==  "code_suggestions_1"):
                try:
                    for response in grpc_conn.conn.getLogFileSug(Suggestions_pb2.GetLogFileRequestSug(numRichiesta=count)):
                        logging_info = response.chunk_file.decode()
                        sug.f.write(logging_info)
                        sug.f.flush()
                        logger.info("[ LOGGING ] Richiesta al microservizio di Suggestions completata con successo.\n")
                except:
                    logger.info("[ LOGGING ] Errore nella ricezione dei dati da parte del servizio di Suggestions.\n")
        
        time.sleep(10)




if __name__ == "__main__":
    log_file()
    set_conn_micro()
    log_file_microservizi()
    run_logger()
