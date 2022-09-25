import grpc
import time

from concurrent import futures
from proto import FroReg_pb2
from proto import FroReg_pb2_grpc
from RegDB import *

class UsersInfoServicer(FroReg_pb2_grpc.UsersInfoServicer):

    def SignUp(self, SignUpInfo, context):
        #check if 'password' and 'conferma password' fields were filled with the same password
        isOk = (SignUpInfo.password == SignUpInfo.passwordConfirm) and isNewUser(SignUpInfo.email)
        #if the two fields correspond, then save user info into remote database (DynamoDB)
        if isOk:
            storeUser(SignUpInfo.email, SignUpInfo.name, SignUpInfo.surname, SignUpInfo.password, SignUpInfo.userType, SignUpInfo.airline)

        output = FroReg_pb2.SignUpResponse(isOk=isOk)
        return output

    def SignIn(self, Credentials, context):
        #TODO

#create gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
FroReg_pb2_grpc.add_UsersInfoServicer_to_server(UsersInfoServicer(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)   #86400 seconds == 24 hours
except KeyboardInterrupt:
    server.stop(0)
