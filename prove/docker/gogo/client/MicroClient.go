package main

import (
	"log"
	"context"
	"fmt"
	"time"

	"google.golang.org/grpc"
	pb "client/gen"
)

func main() {
	time.Sleep(1*time.Second)

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