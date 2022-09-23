import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('FanfaProva')

#Storing an item
table.put_item(
    Item = {
        'FanfaChiave': 'this is the key',
        'Animale': 'gallina',
        'tags': ['tag1', 'tag2']
    }
)

#Reading from DynamoDB
key = 'this is the key'
response = table.get_item(
    Key={
        'FanfaChiave': key,
    }
)

item = response['Item']
print(item)
