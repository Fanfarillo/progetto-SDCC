import grpc
import time

from concurrent import futures

from proto import ClientToServer_pb2
from proto import ClientToServer_pb2_grpc

class GreeterServicer(ClientToServer_pb2_grpc.GreeterServicer):

    def GetServiceName(self, Request, context):
        print("Request: ", Request.name)
        output = ClientToServer_pb2.Response(serviceName = "M2")
        return output

#create gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
ClientToServer_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)   #86400 seconds == 24 hours
except KeyboardInterrupt:
    server.stop(0)
