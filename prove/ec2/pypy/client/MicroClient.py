import grpc

from proto import ClientToServer_pb2
from proto import ClientToServer_pb2_grpc

ADDR_PORT = '18.215.175.86:50051'   #server_IP_addr:port_num

def run():
    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  

    #create client stub
    stub = ClientToServer_pb2_grpc.GreeterStub(channel)

    #get response
    output = stub.GetServiceName(ClientToServer_pb2.Request(id = "1", name = "What's your name?"))
    print("Response: ", output)

run()
