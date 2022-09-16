package main

import (
	"log"
	"context"
	"fmt"

	"google.golang.org/grpc"
	pb "gogo/gen/proto"
)

func main() {
	//open gRPC channel
	conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure())
	if err != nil {
		log.Println(err)
	}

	//create client stub
	client := pb.NewGreeterClient(conn)

	//get response
	resp, err := client.GetServiceName(context.Background(), &pb.Request{Id: "1", Name: "What's your name?"})
	if err != nil {
		log.Println(err)
	}

	fmt.Println(resp.ServiceName)

}
