#!/bin/sh

# Ottengo l'indrizzo IP del container
cat /etc/hosts | grep '^172.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' -o > /app/own_ip_address.txt

# Ottengo gli indirizzi IP dei due container che eseguono il servizio di Discovery
dig scale_prova_app_2 | grep '172.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' -o > /app/server2.txt
dig scale_prova_app_1 | grep '172.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' -o > /app/server1.txt

# L'indirizzo IP del container in esecuzione
export ARG1=$(cat /app/own_ip_address.txt)
#export ARG1

# L'indirizzo IP del primo server di Discovery
export ARG2=$(cat /app/server1.txt)
#export ARG2

# L'indirizzo IP del secondo server di Discovery
export ARG3=$(cat /app/server2.txt)
#export ARG3

rm /app/own_ip_address.txt
rm /app/server2.txt
rm /app/server1.txt

# Lancio il microservizio
python3 ./discovery_server.py $ARG1 $ARG2 $ARG3