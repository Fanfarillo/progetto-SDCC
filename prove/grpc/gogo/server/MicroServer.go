package main

import (
	"context"
	"log"
	"net"

	"google.golang.org/grpc"
	pb "gogo/gen/proto"
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

	grpcServer := grpc.NewServer()

	pb.RegisterGreeterServer(grpcServer, &GreeterServer{})

	grpcServer.Serve(listener)
	if err != nil {
		log.Println(err)
	}

}