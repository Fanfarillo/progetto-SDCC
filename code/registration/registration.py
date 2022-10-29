import grpc
import time
import logging
import sys
sys.path.append("..")

from cipher.security import Security
from concurrent import futures
from proto import Registration_pb2
from proto import Registration_pb2_grpc
from RegDB import *




class UsersInfoServicer(Registration_pb2_grpc.UsersInfoServicer):




    """
    Implementa le procedura di iscrizione.
    """
    def SignUp(self, SignUpInfo, context):

        airline = None
        cipher = Security(b"mysecretpassword")
        
        """
        Ottengo una rappresentazione a stringa
        dei dati binari per poterla scrivere
        all'interno del Database. In questo modo
        evito che i dati siano comprensibili nel
        caso in cui venissero rubati.
        """
        username = str(SignUpInfo.username)
        password = str(SignUpInfo.password)
        passwordConfirm = str(SignUpInfo.passwordConfirm)
        email = str(SignUpInfo.email)
        userType = str(SignUpInfo.userType)
        if SignUpInfo.airline is not None:
            airline = str(SignUpInfo.airline)
        cartaDiCredito = str(SignUpInfo.cartaDiCredito)

        """
        Ottengo una rappresentazione a stringa dei dati
        decifrati.
        """
        username_d = (cipher.decryptData(SignUpInfo.username, SignUpInfo.iv)).decode()
        password_d = (cipher.decryptData(SignUpInfo.password, SignUpInfo.iv)).decode()
        passwordConfirm_d = (cipher.decryptData(SignUpInfo.passwordConfirm, SignUpInfo.iv)).decode()
        email_d = (cipher.decryptData(SignUpInfo.email, SignUpInfo.iv)).decode()
        userType_d = (cipher.decryptData(SignUpInfo.userType, SignUpInfo.iv)).decode()
        airline_d = (cipher.decryptData(SignUpInfo.airline, SignUpInfo.iv)).decode()
        cartaDiCredito_d = (cipher.decryptData(SignUpInfo.cartaDiCredito, SignUpInfo.iv)).decode()

        """
        Verifica se la password e la conferma della password
        sono lo stesso valore. Inoltre, verifica un utente
        con lo stesso username è gà iscritto all'applicazione.
        """
        isOk = (password == passwordConfirm) and isNewUser(username)

        logger.info("Richiesta procedura di iscrizione: [" + email_d + "," + username_d + "," + password_d + "," + passwordConfirm_d + "," + userType_d + "," + cartaDiCredito_d + "]")
        
        if isOk:
            """
            Poiché le informazioni di iscrizione sono valide
            e non esiste alcun utente che ha già quello
            username, allora è possibile completare l'iscrizione.
            """
            ret = storeUser(email, username, password, userType_d, airline, cartaDiCredito, userType)

            logger.info("Procedura di iscrizione conclusa con successo: [" + email_d + "," + username_d + "," + password_d + "," + passwordConfirm_d + "," + userType_d + "]")
        else:
            ret = isOk
            logger_warnings.warning("Procedura di iscrizione conclusa senza successo: [" + email_d + "," + username_d + "," + password_d + "," + passwordConfirm_d + "," + userType_d + "]")
        output = Registration_pb2.SignUpResponse(isOk=ret)
        return output



    """

    """
    def SignIn(self, Credentials, context):
        #read the database (DynamoDB) and check if the log in is successful
        logger.info("Richiesta procedura di accesso: [" + Credentials.username + "," + Credentials.password + "]")
        user = retrieveUser(Credentials.username, Credentials.password)
        if user.isCorrect:
            logger.info("Procedura di accesso conclusa con successo: [" + Credentials.username + "," + Credentials.password + "]")
        else:
            logger_warnings.warning("Procedura di accesso conclusa senza successo: [" + Credentials.username + "," + Credentials.password + "]")
        output = Registration_pb2.SignInResponse(storedType=user.storedType, isCorrect=user.isCorrect)
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
logger.info('Server avviato con successo...')




try:
    while True:
        time.sleep(86400)   #86400 seconds == 24 hours
except KeyboardInterrupt:
    server.stop(0)
