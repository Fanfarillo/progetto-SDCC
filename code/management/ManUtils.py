from datetime import datetime, date
from proto import Discovery_pb2
from proto import Discovery_pb2_grpc
import grpc
import time

#this function checks if provided date exists
#not existing dates are 30/02, 31/02, 31/04, 31/06, 31/09, 31/11 and, for not leap years, 29/09
#NOTE: years that are multiple of 100 and are not multiple of 400 are NOT leap years
def checkDateExistance(dateStr):
    yearStr = dateStr[-4:]
    monthStr = dateStr[3:5]
    dayStr = dateStr[0:2]

    yearInt = int(yearStr)

    if (dayStr=='31' and (monthStr=='02' or monthStr=='04' or monthStr=='06' or monthStr=='09' or monthStr=='11')) or (dayStr=='30' and monthStr=='02'):
        return False
    elif dayStr=='29' and monthStr=='02' and (yearInt%4!=0 or (yearInt%100==0 and yearInt%400!=0)):
        return False
    else:
        return True

#this function checks if provided date is future (i.e. is greater than today)
def checkFutureDate(dateStr):
    dateObj = datetime.strptime(dateStr, '%d-%m-%Y').date()
    today = date.today()
    if dateObj > today:
        return True
    else:
        return False

def roundPrice(initialPrice):

    if not initialPrice.isdigit():      #questo è il caso in cui abbiamo una virgola all'interno del prezzo
        for i in range(0,len(initialPrice)):

            if initialPrice[i] == '.' and i == len(initialPrice)-1:
                return initialPrice[0:i]
            elif initialPrice[i] == '.' and i <= len(initialPrice)-2 and i >= len(initialPrice)-3:
                return initialPrice
            elif initialPrice[i] == '.' and i <= len(initialPrice)-4:
                return initialPrice[0:i+3]

    else:                               #questo è il caso in cui il prezzo è intero
        return initialPrice




def put_discovery_server(discovery_servers, logger):
    new_discovery_servers = []
    """
    Si tenta di contattare il discovery server registrato
    per ottenere la porta su cui il servizio di Management è in
    ascolto. Se le chiamate dovesse fallire, si attendono 5
    secondi per poi eseguire nuovamente il tentativo di connessione.
    """
    ok = False
    while(True):
        # Itero sui discovery servers noti        
        for discovery_server in discovery_servers:
            try:
                # Provo a connettermi al server.
                channel = grpc.insecure_channel(discovery_server)
                stub = Discovery_pb2_grpc.DiscoveryServiceStub(channel)
                # Registrazione della porta del microservizio.
                res = stub.put(Discovery_pb2.PutRequest(serviceName="management" , port="50052"))
            except:
                # Si è verificato un problema nella connessione con il discovery server
                logger.info('[ PUT DISCOVERY MANAGEMENT ] Problema connessione con il discovery server ' + discovery_server + '.')
                time.sleep(2)
                continue
            if(not res.result):
                # Si è verificato un problema con DynamoDB
                logger.info('[ PUT DISCOVERY MANAGEMENT ] Problema DynamoDB con il discovery server ' + discovery_server + '.')
                time.sleep(2)
                continue
                
            for server in res.list_server.servers:
                new_discovery_servers.append(server)
            ok = True
            logger.info('[ PUT DISCOVERY MANAGEMENT ] Registrazione avvenuta con successo presso il discovery server ' + discovery_server + '.')
            break
        if(ok):
            break
        logger.info('[ PUT DISCOVERY MANAGEMENT ] Registrazione avvenuta con insuccesso presso tutti i discovery servers...')        
        time.sleep(5)       

    return new_discovery_servers
