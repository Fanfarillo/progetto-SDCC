#remove all the tables
aws dynamodb delete-table --table-name Utente
aws dynamodb delete-table --table-name Volo
aws dynamodb delete-table --table-name PostiOccupati
aws dynamodb delete-table --table-name PrezzoPosti
aws dynamodb delete-table --table-name Servizi
aws dynamodb delete-table --table-name Pagamento
