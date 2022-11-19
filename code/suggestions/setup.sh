#!/bin/sh

# Ottengo l'indrizzo IP del container
cat /etc/hosts | grep '^172.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' -o > /app/own_address.txt

# Ottengo gli indirizzi IP dei due container che eseguono il servizio di Discovery
dig code_suggestions_2 | grep '172.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' -o > /app/suggestions2.txt
dig code_suggestions_1 | grep '172.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' -o > /app/suggestions1.txt

# L'indirizzo IP del container in esecuzione
export ARG1=$(cat /app/own_address.txt)

# L'indirizzo IP del primo server di Discovery
export ARG2=$(cat /app/suggestions1.txt)

# L'indirizzo IP del secondo server di Discovery
export ARG3=$(cat /app/suggestions2.txt)

# rm /app/own_address.txt
# rm /app/suggestions2.txt
# rm /app/suggestions1.txt

# Compilo e lancio il microservizio
mvn clean verify
mvn exec:java -Dexec.mainClass="control.Suggestions" -Dexec.args="$ARG1 $ARG2 $ARG3"
