import grpc

from proto import ClientToServer_pb2
from proto import ClientToServer_pb2_grpc

ADDR_PORT = 'localhost:50051'   #server_IP_addr:port_num

def run():
    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num
    #channel = grpc.insecure_channel('172.30.160.1:50051', options=(('grpc.enable_http_proxy', 0),))

    #create client stub
    stub = ClientToServer_pb2_grpc.GreeterStub(channel)

    #get response
    output = stub.GetServiceName(ClientToServer_pb2.Request(id = "1", name = "What's your name?"))
    print("Response: ", output)

run()
