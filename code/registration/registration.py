import grpc
import time
import logging
import sys

from security import Security
from concurrent import futures
from proto import Registration_pb2
from proto import Registration_pb2_grpc
from RegDB import *
from regUtils import *


# ------------------------------------------------------ DISCOVERY -----------------------------------------------------
"""
La seguente lista contiene inizialmente solo il
default discovery server per il microservizio di booking.
Tuttavia, nel momento in cui si registra, all'interno possono
essere inserite le informazioni relative all'altro
discovery server.
"""
all_discovery_servers = ['code_discovery_2:50060']
# ------------------------------------------------------ DISCOVERY -----------------------------------------------------


class UsersInfoServicer(Registration_pb2_grpc.UsersInfoServicer):


    """
    Implementa le procedura di iscrizione.
    """
    def SignUp(self, SignUpInfo, context):
        
        cipher = Security(b"mysecretpassword")

        """
        Ottengo una rappresentazione a stringa dei dati
        decifrati.
        """
        username_d = (cipher.decryptData(SignUpInfo.username)).decode('utf-8')
        password_d = (cipher.decryptData(SignUpInfo.password)).decode('utf-8')
        passwordConfirm_d = (cipher.decryptData(SignUpInfo.passwordConfirm)).decode('utf-8')
        userType_d = (cipher.decryptData(SignUpInfo.userType)).decode('utf-8')
        cartaDiCredito_d = (cipher.decryptData(SignUpInfo.cartaDiCredito)).decode('utf-8')

        if SignUpInfo.airline is not None:
            airline_d = (cipher.decryptData(SignUpInfo.airline)).decode('utf-8')
        else:
            airline_d = 'Non abbiamo nessuna compagnia aerea'

        """
        Verifica se la password e la conferma della password
        sono lo stesso valore. Inoltre, verifica se un utente
        con lo stesso username è gà iscritto all'applicazione.
        """
        if SignUpInfo.password != SignUpInfo.passwordConfirm:
            isOk = False
            err = "PASSWORD E CONFERMA PASSWORD NON CORRISPONDONO.\nPROVA A INSERIRE NUOVAMENTE I DATI DELL'ISCRIZIONE."
        elif not isNewUser(SignUpInfo.username):
            isOk = False
            err = "ESISTE GIÀ UN UTENTE CON QUESTO USERNAME.\nPROVA A INSERIRE NUOVAMENTE I DATI DELL'ISCRIZIONE."
        else:
            isOk = True
            err = None

        logger.info("Richiesta procedura di iscrizione: [" + username_d + "," + password_d + "," + passwordConfirm_d + "," + userType_d + "," + cartaDiCredito_d + "]")
        
        if isOk:
            """
            Poiché le informazioni di iscrizione sono valide
            e non esiste alcun utente che ha già quello
            username, allora è possibile completare l'iscrizione.
            """
            ret = storeUser(SignUpInfo.username, SignUpInfo.password, userType_d, SignUpInfo.airline, SignUpInfo.cartaDiCredito, SignUpInfo.userType)

            if ret == False:
                err = "SI È VERIFICATO UN PROBLEMA INTERNO AL SERVER DURANTE LA REGISTRAZIONE.\nRIPROVARE PIÙ TARDI."
                logger_warnings.warning("Procedura di iscrizione conclusa senza successo: [" + username_d + "," + password_d + "," + passwordConfirm_d + "," + userType_d + "]")
            else:
                logger.info("Procedura di iscrizione conclusa con successo: [" + username_d + "," + password_d + "," + passwordConfirm_d + "," + userType_d + "]")
        
        else:
            ret = False
            logger_warnings.warning("Procedura di iscrizione conclusa senza successo: [" + username_d + "," + password_d + "," + passwordConfirm_d + "," + userType_d + "]")
        
        output = Registration_pb2.SignUpResponse(isOk=ret, error=err)
        return output



    """
    Implementa la procedura di Login.
    """
    def SignIn(self, Credentials, context):

        """
        Ottengo una rappresentazione a stringa dei dati
        decifrati.
        """
        cipher = Security(b"mysecretpassword")
        username_d = (cipher.decryptData(Credentials.username)).decode()
        password_d = (cipher.decryptData(Credentials.password)).decode()

        logger.info("Richiesta procedura di accesso: [" + username_d + "," + password_d + "]")

        """
        Verifico se l'utente che sta tentando di eseguire
        il Login effettivamente è presente all'interno del
        sistema. I parametri passati sono dati cifrati.
        """
        user = retrieveUser(Credentials.username, Credentials.password)

        if user.isCorrect:
            logger.info("Procedura di accesso conclusa con successo: [" + username_d + "," + password_d + "]")
            value = user.storedType.__bytes__()
            output = Registration_pb2.SignInResponse(storedType=value, isCorrect=user.isCorrect)
        else:
            logger_warnings.warning("Procedura di accesso conclusa senza successo: [" + username_d + "," + password_d + "]")
            output = Registration_pb2.SignInResponse(storedType=bytes(0), isCorrect=False)
        
        return output



"""
Costruisco un file di LOG in cui andare ad
inserire le richieste che giungono dagli altri
microservizi. Inoltre, inserisco delle informazioni
di warnings nel momento in cui le richieste falliscono.
"""
logging.basicConfig(filename="registration.log", format=f'%(levelname)s - %(asctime)s - %(message)s')
logger = logging.getLogger("registrationInfo")
logger_warnings = logging.getLogger("registrationWarnings")
logger.setLevel(logging.INFO)
logger_warnings.setLevel(logging.WARNING)



#create gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
Registration_pb2_grpc.add_UsersInfoServicer_to_server(UsersInfoServicer(), server)



logger.info('Avvio del server in ascolto sulla porta 50051...')
server.add_insecure_port('[::]:50051')
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
    all_discovery_servers.append(item)

# ------------------------------------------- DISCOVERY -------------------------------------------------------------------------------------------



try:
    while True:
        time.sleep(86400)   #86400 seconds == 24 hours
except KeyboardInterrupt:
    server.stop(0)
