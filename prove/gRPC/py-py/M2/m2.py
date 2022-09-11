import grpc
import time

from concurrent import futures

from proto import m1_to_m2_pb2
from proto import m1_to_m2_pb2_grpc

class GreeterServicer(m1_to_m2_pb2_grpc.GreeterServicer):

    def getServiceName(self, request, context):
        print("REQUEST: ", request.name)
        response = m1_to_m2_pb2.response(serviceName = "M2")
        return response

#create gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
m1_to_m2_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)   #exactly 24 hours
except KeyboardInterrupt:
    server.stop(0)
