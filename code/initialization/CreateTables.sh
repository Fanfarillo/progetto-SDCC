#create all the tables
aws dynamodb create-table \
--table-name Utente \
--attribute-definitions AttributeName=Username,AttributeType=B \
--key-schema AttributeName=Username,KeyType=HASH \
--billing-mode PAY_PER_REQUEST

aws dynamodb create-table \
--table-name Volo \
--attribute-definitions AttributeName=Id,AttributeType=S \
--key-schema AttributeName=Id,KeyType=HASH \
--billing-mode PAY_PER_REQUEST

aws dynamodb create-table \
--table-name PostiOccupati \
--attribute-definitions AttributeName=IdVolo,AttributeType=S \
--key-schema AttributeName=IdVolo,KeyType=HASH \
--billing-mode PAY_PER_REQUEST

aws dynamodb create-table \
--table-name StoricoVolo \
--attribute-definitions AttributeName=IdVolo,AttributeType=S AttributeName=Prenotazione,AttributeType=S \
--key-schema AttributeName=IdVolo,KeyType=HASH AttributeName=Prenotazione,KeyType=RANGE \
--billing-mode PAY_PER_REQUEST

aws dynamodb create-table \
--table-name PrezzoPosti \
--attribute-definitions AttributeName=Compagnia,AttributeType=S \
--key-schema AttributeName=Compagnia,KeyType=HASH \
--billing-mode PAY_PER_REQUEST

aws dynamodb create-table \
--table-name Servizi \
--attribute-definitions AttributeName=Compagnia,AttributeType=S \
--key-schema AttributeName=Compagnia,KeyType=HASH \
--billing-mode PAY_PER_REQUEST

aws dynamodb create-table \
--table-name Pagamento \
--attribute-definitions AttributeName=IdVolo,AttributeType=S AttributeName=Posti,AttributeType=S \
--key-schema AttributeName=IdVolo,KeyType=HASH AttributeName=Posti,KeyType=RANGE \
--billing-mode PAY_PER_REQUEST

aws dynamodb create-table \
--table-name Microservizi \
--attribute-definitions AttributeName=Id,AttributeType=S \
--key-schema AttributeName=Id,KeyType=HASH \
--billing-mode PAY_PER_REQUEST

#populate the tables
python3 PopulateTables.py
