from proto import Discovery_pb2
from proto import Discovery_pb2_grpc
import grpc
import time




#initialString is a string like '0', '1', '2',..., '59', while twoDigitsString is a string like '00', '01', '02',..., '59'
def getTwoDigitsString(initialString):
    intValue = int(initialString)

    if intValue < 10:
        twoDigitsString = '0'+initialString
    else:
        twoDigitsString = initialString

    return twoDigitsString



# ---------------------------------------- DISCOVERY ---------------------------------------------
def put_discovery_server(discovery_servers, logger):
    new_discovery_servers = []
    """
    Si tenta di contattare i discovery server registrati
    per memorizzare la porta su cui il servizio di booking è in
    ascolto. Se le chiamate dovesse fallire, si attendono 5
    secondi per poi eseguire nuovamente il tentativo di connessione.
    """
    ok = False
    while(True):
        # Itero sui discovery servers noti al microservizio di booking       
        for discovery_server in discovery_servers:
            try:
                # Provo a connettermi al server
                channel = grpc.insecure_channel(discovery_server)
                stub = Discovery_pb2_grpc.DiscoveryServiceStub(channel)
                # Memorizzo il servizio
                res = stub.put(Discovery_pb2.PutRequest(serviceName="booking" , port="50053"))
            except:
                # Si è verificato un problema nella connessione con il discovery server
                logger.info('[ PUT DISCOVERY BOOKING ] Problema connessione con il discovery server ' + discovery_server + '.')
                time.sleep(2)
                continue
            if(not res.result):
                # Si è verificato un problema con la richesta DynamoDB
                logger.info('[ PUT DISCOVERY BOOKING ] Problema DynamoDB con il discovery server ' + discovery_server + '.')
                time.sleep(2)
                continue
                
            for server in res.list_server.servers:
                # Recupero i discovery servers nel messaggio di risposta
                new_discovery_servers.append(server)
            ok = True
            logger.info('[ PUT DISCOVERY BOOKING ] Registrazione avvenuta con successo presso il discovery server ' + discovery_server + '.')
            break
        if(ok):
            break
        logger.info('[ PUT DISCOVERY BOOKING ] Registrazione avvenuta con insuccesso presso tutti i discovery servers...')        
        time.sleep(5)       

    return new_discovery_servers
# ---------------------------------------- DISCOVERY ---------------------------------------------