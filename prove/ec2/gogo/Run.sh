#!/bin/sh
gnome-terminal -- sh -c 'go run ./server/MicroServer.go'
gnome-terminal -- sh -c 'go run ./client/MicroClient.go'
