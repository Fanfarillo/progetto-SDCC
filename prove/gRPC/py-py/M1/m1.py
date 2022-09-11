import grpc

from proto import m1_to_m2_pb2
from proto import m1_to_m2_pb2_grpc

def run():
    #open gRPC channel
    channel = grpc.insecure_channel('localhost:50051')  #server_IP_addr:port_num
    #channel = grpc.insecure_channel('172.30.160.1:50051', options=(('grpc.enable_http_proxy', 0),))

    #create client stub
    stub = m1_to_m2_pb2_grpc.GreeterStub(channel)

    #get response
    response = stub.getServiceName(m1_to_m2_pb2.request(id = "1", name = "What's your name?"))
    print("RESPONSE: ", response)

run()
