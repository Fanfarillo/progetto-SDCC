import grpc

from proto import FroReg_pb2
from proto import FroReg_pb2_grpc

ADDR_PORT = 'localhost:50051'   #server_IP_addr:port_num

def sendSignUpInfo(email, name, surname, password, passwordConfirm, userType, airline):
    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    #create client stub
    stub = FroReg_pb2_grpc.UsersInfoStub(channel)

    #get response from Registration service
    output = stub.SignUp(FroReg_pb2.SignUpInfo(email=email, name=name, surname=surname, password=password, passwordConfirm=passwordConfirm, userType=userType, airline=airline))
    #we need to return the boolean value
    return output.isCorrespondent
