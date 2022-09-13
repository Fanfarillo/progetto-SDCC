#!/bin/sh
gnome-terminal -- sh -c 'python3 ./server/MicroServer.py'
gnome-terminal -- sh -c 'python3 ./client/MicroClient.py'
