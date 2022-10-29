import boto3
import sys
sys.path.append("..")

from cipher.security import Security




DYNAMODB = 'dynamodb'
TABELLA_UTENTE = 'Utente'



class LoggedUser:
    def __init__(self, username, storedType, isCorrect):
        # Username dell'utente
        self.username = username
        # Tipologia dell'utente
        self.storedType = storedType
        # Esito del processo di iscrizione
        self.isCorrect = isCorrect




"""
Registra il nuovo utente con le informazioni passate
come parametri.
"""
def storeUser(email, username, password, userType_d, airline, cartaDiCredito, userType):
    print(userType)
    if userType_d == 'Turista':
        """
        Il check viene fatto sul valore decodficato
        mentre la scrittura nel DB è codificata.
        """
        typeToStore = userType
    else:
        """
        Se l'utente che richiede l'iscrizione
        non è un Turista, allora il suo tipo
        corrisponde alla compagnia aerea.
        """
        typeToStore = airline
    
    try:
        dynamodb = boto3.resource(DYNAMODB)
        table = dynamodb.Table(TABELLA_UTENTE)
        table.put_item(
            Item = {
                'Username': username,
                'Email': email,
                'Password': password,
                'Tipo': typeToStore,
                'cartaDiCredito': cartaDiCredito
            }
        )
    except Exception:
        return False
    
    return True



#this function returns true if there is no item with the specified email (i.e. the specified primary key); it returns false otherwise
"""
Verifica se esiste già un utente iscritto nel
sistema che ha lo username inserito per il
processo di iscrizione.

Ritorna TRUE se non c'è già alcun utente
che ha lo username richiest; altrimenti,
ritorna FALSE.
"""
def isNewUser(username):
    cipher = Security(b"mysecretpassword")
    print("VALORE DA CONFRONTARE: " + username)
    try:
        dynamodb = boto3.resource(DYNAMODB)
        table = dynamodb.Table(TABELLA_UTENTE)
        response = table.get_item(
            Key = {
                'Username': username,
            }
        )
    except Exception:
        return False

    if 'Item' in response:
        return False
    else:
        return True




"""

"""
def retrieveUser(username, password):
    dynamodb = boto3.resource(DYNAMODB)
    table = dynamodb.Table(TABELLA_UTENTE)

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
