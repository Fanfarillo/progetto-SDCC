import boto3

def storeUser(email, name, surname, password, userType, airline):
    if userType == 'Turista':
        typeToStore = userType
    else:
        typeToStore = airline

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Utente')
    
    #store an item in 'Utente' table in DynamoDB
    table.put_item(
        Item = {
            'Email': email,
            'Nome': name,
            'Cognome': surname,
            'Password': password,
            'Tipo': typeToStore
        }
    )

#this function returns true if there is no item with the specified email (i.e. the specified primary key); it returns false otherwise
def isNewUser(email):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Utente')

    #read from 'Utente' table in DynamoDB
    response = table.get_item(
        Key = {
            'Email': email,
        }
    )

    if response['Item'] == None:
        return True
    else:
        return False
