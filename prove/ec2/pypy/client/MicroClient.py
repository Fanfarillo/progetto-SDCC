import grpc

from proto import ClientToServer_pb2
from proto import ClientToServer_pb2_grpc

def run():
    #open gRPC channel
    channel = grpc.insecure_channel('52.90.109.146:50051')  #server_IP_addr:port_num

    #create client stub
    stub = ClientToServer_pb2_grpc.GreeterStub(channel)

    #get response
    output = stub.GetServiceName(ClientToServer_pb2.Request(id = "1", name = "What's your name?"))
    print("Response: ", output)

run()
