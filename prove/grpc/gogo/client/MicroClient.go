package main

import (
	"log"
	"context"
	"fmt"

	"google.golang.org/grpc"
	pb "gogo/gen/proto"
)

func main() {
	conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure())
	if err != nil {
		log.Println(err)
	}

	client := pb.NewGreeterClient(conn)

	resp, err := client.GetServiceName(context.Background(), &pb.Request{Id: "1", Name: "What's your name?"})
	if err != nil {
		log.Println(err)
	}

	fmt.Println(resp.ServiceName)

}