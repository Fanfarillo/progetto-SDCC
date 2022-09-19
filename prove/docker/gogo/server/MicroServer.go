package main

import (
	"context"
	"log"
	"net"
	"fmt"

	"google.golang.org/grpc"
	pb "server/gen"
)

type GreeterServer struct {
	pb.UnimplementedGreeterServer
}

func (s *GreeterServer) GetServiceName(ctx context.Context, req *pb.Request) (*pb.Response, error) {
	log.Println("Request: ", req.Name)
	return &pb.Response{ServiceName: "M2"}, nil
}

func main() {
	listener, err := net.Listen("tcp", "localhost:50051")
	if err != nil {
		log.Fatalln(err)
	}
	fmt.Println("Starting server. Listening on port 50051.")

	//create gRPC server
	grpcServer := grpc.NewServer()

	pb.RegisterGreeterServer(grpcServer, &GreeterServer{})

	grpcServer.Serve(listener)
	if err != nil {
		log.Println(err)
	}

}
