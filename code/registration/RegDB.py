import boto3

class LoggedUser:
    def __init__(self, username, storedType, isCorrect):
        self.username = username
        self.storedType = storedType
        self.isCorrect = isCorrect

def storeUser(email, username, password, userType, airline):
    if userType == 'Turista':
        typeToStore = userType
    else:
        typeToStore = airline

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Utente')
    
    #store an item in 'Utente' table in DynamoDB
    table.put_item(
        Item = {
            'Username': username,
            'Email': email,
            'Password': password,
            'Tipo': typeToStore
        }
    )

#this function returns true if there is no item with the specified email (i.e. the specified primary key); it returns false otherwise
def isNewUser(username):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Utente')

    #read from 'Utente' table in DynamoDB
    response = table.get_item(
        Key = {
            'Username': username,
        }
    )

    if 'Item' in response:
        return False
    else:
        return True

def retrieveUser(username, password):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Utente')

    #read from 'Utente' table in DynamoDB
    response = table.get_item(
        Key = {
            'Username': username,
        }
    )

    #if the specified email does not exist, the log in must fail
    if not ('Item' in response):
        user = LoggedUser(None, None, False)
        return user
    
    #if the specified password is incorrect, the log in must fail
    item = response['Item']
    actualPassword = item['Password']
    if actualPassword != password:
        user = LoggedUser(None, None, False)
        return user

    #else the log in is successful
    usernameField = item['Username']
    userType = item['Tipo']

    user = LoggedUser(usernameField, userType, True)
    return user
