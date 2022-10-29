import grpc
import sys

sys.path.append("..")
from cipher.security import Security

from proto import Registration_pb2
from proto import Registration_pb2_grpc




ADDR_PORT = 'localhost:50051'   #server_IP_addr:port_num




"""
Instanzia un canale di comunicazione con il
microservizio che gestisce le iscrizioni per
l'applicazione. Viene passato in input un
messaggio contenente tutte le informazioni
necessarie per l'iscrizione.
"""
def sendSignUpInfo(email, username, password, passwordConfirm, userType, airline, cartaDiCredito):

    channel = grpc.insecure_channel(ADDR_PORT)
    stub = Registration_pb2_grpc.UsersInfoStub(channel)

    dig = Registration_pb2.digestSignUpInfo()

    cipher = Security(b"mysecretpassword")

    digest = cipher.message_integrity(bytes(password, 'utf-8'))
    dig.password = digest
    print("[ DIGEST ]: " + str(digest))
    print("Lunghezza digest: " + str(len(digest)))
    ciphertextPassword, iv = cipher.encryptData(bytes(password, 'utf-8'), None)
    print("[ CIFRATO ]: " + str(ciphertextPassword))
    plaintext = cipher.decryptData(ciphertextPassword, iv)
    print("[ DECIFRATO ]: " + str(plaintext))

    iv_dec = iv


    digest = cipher.message_integrity(bytes(passwordConfirm, 'utf-8'))
    dig.passwordConfirm = digest
    print("[ DIGEST ]: " + str(digest))
    print("Lunghezza digest: " + str(len(digest)))
    ciphertextPasswordConf, iv = cipher.encryptData(bytes(passwordConfirm, 'utf-8'),iv_dec)
    print("[ CIFRATO ]: " + str(ciphertextPasswordConf))    
    plaintext = cipher.decryptData(ciphertextPasswordConf, iv)
    print("[ DECIFRATO ]: " + str(plaintext))


    digest = cipher.message_integrity(bytes(email, 'utf-8'))
    dig.email = digest
    print("[ DIGEST ]: " + str(digest))
    print("Lunghezza digest: " + str(len(digest)))
    ciphertextEmail, iv = cipher.encryptData(bytes(email, 'utf-8'),iv_dec)
    print("[ CIFRATO ]: " + str(ciphertextEmail))    
    plaintext = cipher.decryptData(ciphertextEmail, iv)
    print("[ DECIFRATO ]: " + str(plaintext))


    digest = cipher.message_integrity(bytes(username, 'utf-8'))
    dig.username = digest
    print("[ DIGEST ]: " + str(digest))
    print("Lunghezza digest: " + str(len(digest)))
    ciphertextUsername, iv = cipher.encryptData(bytes(username, 'utf-8'),iv_dec)
    print("[ CIFRATO ]: " + str(ciphertextUsername))    
    plaintext = cipher.decryptData(ciphertextUsername, iv)
    print("[ DECIFRATO ]: " + str(plaintext))
    

    digest = cipher.message_integrity(bytes(cartaDiCredito, 'utf-8'))
    dig.cartaDiCredito = digest
    print("[ DIGEST ]: " + str(digest))
    print("Lunghezza digest: " + str(len(digest)))
    ciphertextCartaDiCredito, iv = cipher.encryptData(bytes(cartaDiCredito, 'utf-8'),iv_dec)
    print("[ CIFRATO ]: " + str(ciphertextCartaDiCredito))    
    plaintext = cipher.decryptData(ciphertextCartaDiCredito, iv)
    print("[ DECIFRATO ]: " + str(plaintext))


    digest = cipher.message_integrity(bytes(userType, 'utf-8'))
    dig.userType = digest
    print("[ DIGEST ]: " + str(digest))
    print("Lunghezza digest: " + str(len(digest)))
    ciphertextUserType, iv = cipher.encryptData(bytes(userType, 'utf-8'),iv_dec)
    print("[ CIFRATO ]: " + str(ciphertextUserType))    
    plaintext = cipher.decryptData(ciphertextUserType, iv)
    print("[ DECIFRATO ]: " + str(plaintext))

    if airline is not None:
        digest = cipher.message_integrity(bytes(airline, 'utf-8'))
        dig.airline = digest
        print("[ DIGEST ]: " + str(digest))
        print("Lunghezza digest: " + str(len(digest)))
        ciphertextAirline, iv = cipher.encryptData(bytes(airline, 'utf-8'),iv_dec)
        print("[ CIFRATO ]: " + str(ciphertextAirline))    
        plaintext = cipher.decryptData(ciphertextAirline, iv)
        print("[ DECIFRATO ]: " + str(plaintext))
    else:
        ciphertextAirline = None

    """
    Invio della richiesta di iscrizione dell'utente.
    Il valore di output sarà TRUE se è andata a buon
    fine; altrimenti, sarà FALSE.
    """
    output = stub.SignUp(Registration_pb2.SignUpInfo(email=ciphertextEmail, username=ciphertextUsername, password=ciphertextPassword, passwordConfirm=ciphertextPasswordConf, userType=ciphertextUserType, airline=ciphertextAirline, cartaDiCredito=ciphertextCartaDiCredito, iv=iv_dec, dig = dig))

    return output.isOk

def sendCredentials(username, password):
    #open gRPC channel
    channel = grpc.insecure_channel(ADDR_PORT)  #server_IP_addr:port_num

    #create client stub
    stub = Registration_pb2_grpc.UsersInfoStub(channel)

    #get response from Registration service
    output = stub.SignIn(Registration_pb2.Credentials(username=username, password=password))
    #here we need to return the entire output (i.e. the entire received message)
    return output
