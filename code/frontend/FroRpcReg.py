import grpc

from proto import Registration_pb2
from proto import Registration_pb2_grpc

ADDR_PORT = 'localhost:50051'   #server_IP_addr:port_num

def sendSignUpInfo(email, username, password, passwordConfirm, userType, airline):
    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    #create client stub
    stub = Registration_pb2_grpc.UsersInfoStub(channel)

    #get response from Registration service
    output = stub.SignUp(Registration_pb2.SignUpInfo(email=email, username=username, password=password, passwordConfirm=passwordConfirm, userType=userType, airline=airline))
    #we need to return the boolean value
    return output.isOk

def sendCredentials(username, password):
    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    #create client stub
    stub = Registration_pb2_grpc.UsersInfoStub(channel)

    #get response from Registration service
    output = stub.SignIn(Registration_pb2.Credentials(username=username, password=password))
    #here we need to return the entire output (i.e. the entire received message)
    return output
