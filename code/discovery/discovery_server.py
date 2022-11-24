import boto3
import time
import logging
import grpc
import sys
from proto import Discovery_pb2
from proto import Discovery_pb2_grpc
import threading
from concurrent import futures
from boto3.dynamodb.conditions import Attr



class Microservice:
    def __init__(self, serviceName, port):
        self.serviceName = serviceName
        self.port = port



# Porta su cui è in ascolto il Discovery server.
PORT = '50060'

#Nomi dei due Discovery Server
SERVER_1 = "code_discovery_1"
SERVER_2 = "code_discovery_2"

# Cache contenente tutti gli oggetti Microservice che sono stati registrati.
all_microservices_cache = []

# Cache contenente tutti i nomi dei microservizi che sono stati registrati.
all_microservices_cache_names = []

# Indirizzo dell'altro Discovery Server
# ADDR_PORT = 'localhost:50055'

# Lista degli altri Discovery Servers
#MICROSERVICE_DISCOVERY_SERVER_LIST = ['localhost:50055']
MICROSERVICE_DISCOVERY_SERVER_LIST = []

# Costanti utilizzate nel codice per accedere al DB remoto
MICROSERVICE_TABLE = 'Microservizi'
DYNAMODB = 'dynamodb'
REGIONE = 'us-east-1'



# Discovery Server
class DiscoveryServicer(Discovery_pb2_grpc.DiscoveryServiceServicer):
    """
    Consente di ottenere la porta relativa
    al microservizio passato come parametro.
    """
    def get(self, request, context):
        try:
            # Verifico se è presente l'informazione richiesta.
            all_microservices_cache_names.index(request.serviceNameTarget)

            # Logging
            logger.info('[GET] Richiesta di GET servita con successo.\nIl microservizio richiesto è effettivamente registrato.\n{serviceName:'+ request.serviceName + '\t\t\tserviceNameTarget:'+ request.serviceNameTarget +'}\n')

            # Cerco la porta relativa al microservizio richiesto.
            for m in all_microservices_cache:
                if m.serviceName == request.serviceNameTarget:
                    return Discovery_pb2.GetReply(serviceName=m.serviceName, port=m.port)
                              
        except:
            """
            Il Discovery server ancora non è a conoscenza
            delle informazioni relative al microservizio richiesto.
            """

            # Logging
            logger_warnings.warning('[GET] Non è possibile servire la richiesta di GET poichè non si dispone delle informazioni richieste.\n{serviceName:'+ request.serviceName + '\t\t\serviceNameTarget:'+ request.serviceNameTarget +'}\n')
            
            return Discovery_pb2.GetReply(serviceName=request.serviceNameTarget, port='-1')
     

    


    """
    Consente di registrare la porta relativa
    al microservizio passati come parametri.
    """
    def put(self, request, context):

        try:
            """
            Verifico se il servizio è stato già
            inserito in precedenza.
            """
            all_microservices_cache_names.index(request.serviceName)
            logger.info('[PUT] Richiesta di PUT ma il servizio è stato già registrato.\n{serviceName:'+ request.serviceName + '\t\t\port:'+ request.port +'}')
        except ValueError:

            """
            Il microservizio non è stato ancora registrato.
            Registro le informazioni relative alla
            porta e al nome del microservizio all'interno
            del database per la prima volta.
            """
            try:
                dynamodb = boto3.resource(DYNAMODB, REGIONE)
                table = dynamodb.Table(MICROSERVICE_TABLE)

                table.put_item(
	            Item = {
                    'Id': request.serviceName,
                    'Porta': request.port
	                }
                )
            except Exception:
                # Avviso il microservizio che si è verificato un errore nella PUT
                logger_warnings.warning('[PUT] Registrazione del servizio terminata senza successo.\n{serviceName:'+ request.serviceName + '\t\t\tport:'+ request.port +'}\n')
                return Discovery_pb2.PutReply(result=False)

            # Creazione della nuova istanza di microservizio
            microservice = Microservice(request.serviceName, request.port)
            # Registrazione nella cache della nuova istanza di microservizio            
            all_microservices_cache.append(microservice)
            all_microservices_cache_names.append(microservice.serviceName)
            logger.info('[PUT] Registrazione del servizio conclusa con successo.\n{serviceName:'+ request.serviceName + '\t\t\tport:'+ request.port +'}')

        # Comunico al microservizio gli altri Discovery Servers
        discovery_servers = Discovery_pb2.DiscoveryServers()
        for server in MICROSERVICE_DISCOVERY_SERVER_LIST:
            discovery_servers.servers.append(server)
        
        # Logging
        logger.info('[PUT] Comunicazione degli altri Discovery Server al servizio.\n{serviceName:'+ request.serviceName + '\t\t\tport:'+ request.port +'}\n')
      
        return Discovery_pb2.PutReply(result=True, list_server=discovery_servers)

        


    """
    Elenco tutti i microservizi che sono
    stati passati come parametro al metodo
    RPC.
    """
    def sendMicroserviceInfo(self, request, context):
        microservice_info_ricevute = []
        logger.info("[SENDMICROSERVICEINFO] Ricezione informazioni relative ai microservizi conosciuti dall'altro server...")
        for microservizio in request.microservices.microservices_list:            
            try:
                # Verifico se l'informazione è già presente all'interno della cache.
                all_microservices_cache_names.index(microservizio.serviceName)
            except ValueError:
                # Il valore non è presente nella cache e aggiungo l'informazione.
                m = Microservice(microservizio.serviceName, microservizio.port)
                all_microservices_cache.append(m)
                all_microservices_cache_names.append(microservizio.serviceName)
            microservice_info_ricevute.append(microservizio.serviceName)

        # Logging
        logger.info("[SENDMICROSERVICEINFO] microservizi ricevuti: " + str(microservice_info_ricevute) + ".")

        """
        Rispondo al server inviando le informazioni
        sui microservizi che mi sono note in modo
        da condividere le informazioni tra i due
        Discovery server.
        """
        # Inizializzo la lista contenente i microservizi.
        response = Discovery_pb2.infoMicroservices()

        for microservizio in all_microservices_cache:
            # Prendo il singolo microservizio.
            ms = Discovery_pb2.infoMicroservice(serviceName=microservizio.serviceName, port = microservizio.port)
            # Lo appendo alla lista dei microservizi.
            response.microservices_list.append(ms)
        
        # Restituisco i servizi da me conosciuti.
        ret = Discovery_pb2.microserviceInfoReply(microservices=response)
        logger.info("[SENDMICROSERVICEINFO] Invio delle informazioni relative ai microservizi da me conosciuti...\n")
        return ret




def periodicUpdate():
    dynamodb = boto3.resource(DYNAMODB, REGIONE)
    table = dynamodb.Table(MICROSERVICE_TABLE)

    # Inizializzo un contatore degli aggiornamenti.
    contatore = 0
    while(1):

        # Logging
        logger.info('[AGGIORNAMENTO PERIODICO]: aggiornamento numero ' + str(contatore) + ".")

        all_microservices_cache = []
        all_microservices_cache_names = []

        """
        Il discovery server recupera le informazioni
        aggiornate dal database. Periodicamente, il server
        si allinea alle informazioni corrette per poi
        comunicarle ai microservizi che le richiedono.
        """

        # Ottengo tutte le informazioni relative ai microservizi
        response = table.scan()
        data = response['Items']

        # Itero sui risultati della Query.
        for diz in data:
            porta = diz['Porta']
            nome = diz['Id']
            all_microservices_cache_names.append(nome)
            all_microservices_cache.append(Microservice(nome, porta))
        
        if len(all_microservices_cache)==0:
            """
            Se il server non ha ricevuto informazioni
            da alcun microservizio, allora non ha alcuna
            informazione da inviare all'altro discovery
            server.
            """
            logger.info('[AGGIORNAMENTO PERIODICO]: tentativo di aggiornamento numero ' + str(contatore) + ' fallito poiché non si ha alcuna informazione.\n')

            """
            Blocco il thread aspettando di ricevere 
            delle informazioni dai microservizi o dall'altro
            server
            """ 
            time.sleep(10)
            contatore = contatore + 1
            continue

        """
        All'interno della struttura dati sono
        presenti delle informazioni che possono
        essere inviate. Eseguo una scansione
        di questi dati per poter costruire il
        parametro di input da inviare.
        """

        """
        Inizializzo la lista che conterrà le
        informazioni relative ai microservizi noti.
        """
        request = Discovery_pb2.infoMicroservices()

        # Logging
        logger.info('[AGGIORNAMENTO PERIODICO]: microservizi attualmente conosciuti\n' + str(all_microservices_cache_names))

        """
        Costruisco il parametro da passare
        all'invocazione del metodo RPC.
        """
        for microservizio in all_microservices_cache:

            # Prendo il singolo microservizio.
            ms = Discovery_pb2.infoMicroservice(serviceName=microservizio.serviceName, port = microservizio.port)

            # Lo appendo alla lista dei microservizi.
            request.microservices_list.append(ms)

        """
        Invio le informazioni mantenute all'interno della
        cache all'altro discovery server. Inoltre, mi
        aspetto di ricevere le informazioni sui microservizi
        da lui conosciuti.
        """
        try:
            output = stub.sendMicroserviceInfo(Discovery_pb2.microserviceInfoRequest(microservices=request))
            logger.info('[AGGIORNAMENTO PERIODICO]: scambio informazioni con il discovery server avvenuto con successo.\n' + str(all_microservices_cache_names)+"\n")
        except:
            logger_warnings.warning('[AGGIORNAMENTO PERIODICO]: ci sono delle informazioni da comunicare ma il server non è attulmente raggiungibile.\n')
            contatore = contatore + 1
        """
        Blocco il thread per evitare di comunicare
        continuamente le informazioni all'altro
        server di Discovery. Ogni 10 secondi il thread
        tenterà di comunicare le informazioni sulla
        discovery all'altro server.
        """
        time.sleep(10)
        contatore = contatore + 1




"""
Costruisco un file di LOG in cui andare ad
inserire le richieste che giungono dagli altri
microservizi. Inoltre, inserisco delle informazioni
di warnings nel momento in cui le richieste falliscono.
"""
logging.basicConfig(filename="discovery_1.log", format=f'%(levelname)s - %(asctime)s - %(message)s')
logger = logging.getLogger("discovery_1_info")
logger_warnings = logging.getLogger("discovery_1_warnings")
logger.setLevel(logging.INFO)
logger_warnings.setLevel(logging.WARNING)


#------------------------------INIZIO CODICE CHE GESTISCE LA REPLICAZIONE DEL DISCOVERY SERVER-----------------------------

try:
    # Recupero i parametri passati da linea di comando
    params = sys.argv

    # Recupero l'indirizzo IP del container
    own_ip_address = params[1]

    # Recupero gli indirizzi IP di entrambi i Discovery server
    server_1 = params[2]
    server_2 = params[3]
except:
    sys.exit(1)

other_discovery_server = None

# Identificazione del nome del container
if(own_ip_address==server_1):
    # Il container ha nome SERVER_1 e dovrà quindi contattare SERVER_2
    other_discovery_server = SERVER_2
    logger.info('[SETUP NOME DEL CONTAINER]:' + SERVER_1 +"\t"+ server_1 +"\n")
else:
    logger.info('[SETUP NOME DEL CONTAINER]:' + SERVER_2 +"\t"+ server_2 +"\n")
    other_discovery_server = SERVER_1

if other_discovery_server is None:
    logger_warnings.warning("[ FATAL ]: Errore nella risoluzione dell'indirizzo IP del discovery server.")            
    sys.exit(1)



# Creazione del server RPC
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
Discovery_pb2_grpc.add_DiscoveryServiceServicer_to_server(DiscoveryServicer(), server)

# Scrivo le informazioni all'interno del Logging
logger.info('Avvio del server in ascolto sulla porta '+ PORT + '...')
# Avvio del server RPC.
server.add_insecure_port('[::]:' + PORT)
server.start()
# Scrivo le informazioni all'interno del Logging
logger.info('Server avviato con successo.\n')




"""
Creazione di un thread che periodicamente
invia i propri dati all'altro discrovery
server.
"""
ADDR_PORT = other_discovery_server+':' + PORT
MICROSERVICE_DISCOVERY_SERVER_LIST.append(ADDR_PORT)
channel = grpc.insecure_channel(ADDR_PORT)
stub = Discovery_pb2_grpc.DiscoveryServiceStub(channel)
x = threading.Thread(target=periodicUpdate)
x.start()

#------------------------------FINE CODICE CHE GESTISCE LA REPLICAZIONE DEL DISCOVERY SERVER-----------------------------



# Main thread...
try:
    while True:
        time.sleep(86400)   #86400 seconds == 24 hours
except KeyboardInterrupt:
    server.stop(0)