import grpc
import sys

from security import Security
from proto import Registration_pb2
from proto import Registration_pb2_grpc


ADDR_PORT = 'registration:50051'


class Output:
    def __init__(self, storedType, isCorrect):
        self.isCorrect = isCorrect
        self.storedType = storedType



"""
Instanzia un canale di comunicazione con il
microservizio che gestisce le iscrizioni per
l'applicazione. Viene passato in input un
messaggio contenente tutte le informazioni
necessarie per l'iscrizione.
"""
def sendSignUpInfo(username, password, passwordConfirm, userType, airline, cartaDiCredito):

    channel = grpc.insecure_channel(ADDR_PORT)
    stub = Registration_pb2_grpc.UsersInfoStub(channel)

    dig = Registration_pb2.digestSignUpInfo()

    """
    Implemento meccanismi di sicurezza:
    - Integrità del messaggio
    - Cifratura
    
    1. Calcolo del digest del messaggio utilizando SHA-256
    2. Cifratura dei dati utilizzando AES-128
    """
    cipher = Security(b"mysecretpassword")

    # Password
    digest = cipher.message_integrity(bytes(password, 'utf-8'))
    dig.password = digest
    ciphertextPassword, iv = cipher.encryptData(bytes(password, 'utf-8'))

    # Password conferma
    digest = cipher.message_integrity(bytes(passwordConfirm, 'utf-8'))
    dig.passwordConfirm = digest
    ciphertextPasswordConf, iv = cipher.encryptData(bytes(passwordConfirm, 'utf-8'))

    # Username
    digest = cipher.message_integrity(bytes(username, 'utf-8'))
    dig.username = digest
    ciphertextUsername, iv = cipher.encryptData(bytes(username, 'utf-8'))

    # Carta di credito
    digest = cipher.message_integrity(bytes(cartaDiCredito, 'utf-8'))
    dig.cartaDiCredito = digest
    ciphertextCartaDiCredito, iv = cipher.encryptData(bytes(cartaDiCredito, 'utf-8'))

    # Tipologia utente
    digest = cipher.message_integrity(bytes(userType, 'utf-8'))
    dig.userType = digest
    ciphertextUserType, iv = cipher.encryptData(bytes(userType, 'utf-8'))

    if airline is not None:
        """
        L'utente ha specificato una compagnia
        aerea. Ossia, non sarà un utente di tipo
        Turista.
        """
        digest = cipher.message_integrity(bytes(airline, 'utf-8'))
        dig.airline = digest
        ciphertextAirline, iv = cipher.encryptData(bytes(airline, 'utf-8'))
    else:
        ciphertextAirline = None

    """
    Invio della richiesta di iscrizione dell'utente.
    Il valore di output sarà TRUE se è andata a buon
    fine; altrimenti, sarà FALSE.

    I parametri di input sono dati cifrati. Poiché
    queste informazioni sono sensibili, esse viaggiano
    cifrate tra i microservizi. Inoltre, abbiamo anche
    i vari digest per controllare l'integrità dei messaggi.
    """

    output = stub.SignUp(Registration_pb2.SignUpInfo(username=ciphertextUsername, password=ciphertextPassword, passwordConfirm=ciphertextPasswordConf, userType=ciphertextUserType, airline=ciphertextAirline, cartaDiCredito=ciphertextCartaDiCredito, dig = dig))

    return output



"""
Instanzia un canale di comunicazione con il
microservizio che gestisce il login per
l'applicazione. Viene passato in input un
messaggio contenente tutte le informazioni
necessarie per effettuare il login.
"""
def sendCredentials(username, password):

    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num
    stub = Registration_pb2_grpc.UsersInfoStub(channel)

    dig = Registration_pb2.digestCredentials()

    """
    Implemento meccanismi di sicurezza:
    - Integrità del messaggio
    - Cifratura
    
    1. Calcolo del digest del messaggio utilizando SHA-256
    2. Cifratura dei dati utilizzando AES-128
    """
    cipher = Security(b"mysecretpassword")

    # Username
    digest = cipher.message_integrity(bytes(username, 'utf-8'))
    dig.username = digest
    ciphertextUsername, iv = cipher.encryptData(bytes(username, 'utf-8')) 

    # Password
    digest = cipher.message_integrity(bytes(password, 'utf-8'))
    dig.password = digest
    ciphertextPassword, iv = cipher.encryptData(bytes(password, 'utf-8'))
    
    output = stub.SignIn(Registration_pb2.Credentials(username=ciphertextUsername, password=ciphertextPassword, dig=dig))


    storedTypeString = cipher.decryptData(output.storedType).decode()

    out = Output(storedTypeString, output.isCorrect)
    
    return out
