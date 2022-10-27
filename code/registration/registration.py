import grpc
import time
import logging

from concurrent import futures
from proto import Registration_pb2
from proto import Registration_pb2_grpc
from RegDB import *




class UsersInfoServicer(Registration_pb2_grpc.UsersInfoServicer):

    def SignUp(self, SignUpInfo, context):
        #check if 'password' and 'conferma password' fields were filled with the same password; check also if the email was not used by someone else
        isOk = (SignUpInfo.password == SignUpInfo.passwordConfirm) and isNewUser(SignUpInfo.username)
        logger.info("Richiesta procedura di iscrizione: [" + SignUpInfo.email + "," + SignUpInfo.username + "," + SignUpInfo.password + "," + SignUpInfo.passwordConfirm + "," + SignUpInfo.userType + "]")
        #if the two fields correspond, then save user info into remote database (DynamoDB)
        if isOk:
            storeUser(SignUpInfo.email, SignUpInfo.username, SignUpInfo.password, SignUpInfo.userType, SignUpInfo.airline)
            logger.info("Procedura di iscrizione conclusa con successo: [" + SignUpInfo.email + "," + SignUpInfo.username + "," + SignUpInfo.password + "," + SignUpInfo.passwordConfirm + "," + SignUpInfo.userType + "]")
        else:
            logger_warnings.warning("Procedura di iscrizione conclusa senza successo: [" + SignUpInfo.email + "," + SignUpInfo.username + "," + SignUpInfo.password + "," + SignUpInfo.passwordConfirm + "," + SignUpInfo.userType + "]")
        output = Registration_pb2.SignUpResponse(isOk=isOk)
        return output

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
