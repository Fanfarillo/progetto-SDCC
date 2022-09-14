package main

import (
  "log"

  amqp "github.com/rabbitmq/amqp091-go"
)

func failOnError(err error, msg string) {
  if err != nil {
    log.Panicf("%s: %s", msg, err)
  }
}

func main() {

	//connect to RabbitMQ server
	conn, err := amqp.Dial("amqp://guest:guest@localhost:5672/")
	failOnError(err, "Failed to connect to RabbitMQ")
	defer conn.Close()

	//create channel
	ch, err := conn.Channel()
	failOnError(err, "Failed to open a channel")
	defer ch.Close()

	//declare the queue to hold messages and deliver to consumers
	q, err := ch.QueueDeclare(
  		"hello", // name
  		false,   // durable
  		false,   // delete when unused
  		false,   // exclusive
  		false,   // no-wait
  		nil,     // arguments
	)
	failOnError(err, "Failed to declare a queue")

	//consume queued messages
	msgs, err := ch.Consume(
		q.Name, // queue
		"",     // consumer
		true,   // auto-ack
		false,  // exclusive
		false,  // no-local
		false,  // no-wait
		nil,    // args
	  )
	  failOnError(err, "Failed to register a consumer")
	  
	  var forever chan struct{}
	  
	  //goroutine for reading the messages
	  go func() {
		for d := range msgs {
		  log.Printf("Received a message: %s", d.Body)
		}
	  }()
	  
	  log.Printf(" [*] Waiting for messages. To exit press CTRL+C")
	  <-forever

}
