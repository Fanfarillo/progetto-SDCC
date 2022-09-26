import boto3

class LoggedUser:
    def __init__(self, name, surname, storedType, isCorrect):
        self.name = name
        self.surname = surname
        self.storedType = storedType
        self.isCorrect = isCorrect

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

    if 'Item' in response:
        return False
    else:
        return True

def retrieveUser(email, password):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Utente')

    #read from 'Utente' table in DynamoDB
    response = table.get_item(
        Key = {
            'Email': email,
        }
    )

    #if the specified email does not exist, the log in must fail
    if not ('Item' in response):
        user = LoggedUser(None, None, None, False)
        return user
    
    #if the specified password is incorrect, the log in must fail
    item = response['Item']
    actualPassword = item['Password']
    if actualPassword != password:
        user = LoggedUser(None, None, None, False)
        return user

    #else the log in is successful
    name = item['Nome']
    surname = item['Cognome']
    userType = item['Tipo']

    user = LoggedUser(name, surname, userType, True)
    return user
