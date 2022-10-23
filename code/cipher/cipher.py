from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
import sys
import hashlib

"""
La dimensione del blocco è pari a 128 bits.
"""
BLOCK_SIZE = 16

class MyCipher:
    


    def __init__(self, key):

        if(len(key)!=16):
            raise Exception("La dimensione della chiave deve essere  pari a BLOCK_SIZE bytes")

        """
        Trasformo la chiave in un array di bytes
        se già non lo fosse.
        """
        if(isinstance(key, bytes)):
            self.key = key
        else:
            self.key = bytes(key, 'utf-8')



    def encryptData(self, plaintext):

        """
        Eseguo un check per verificare il
        tipo del parametro passato al metodo.
        """
        if(not isinstance(plaintext, bytes)):
            raise Exception("Il parametro deve essere un oggetto di tipo bytes.")

        """
        La dimensione del parametro plaintext deve
        essere un multiplo intero di BLOCK_SIZE per
        poter essere cifrato in modo corretto.
        Nel caso in cui la dimensione non fosse un
        multiplo intero di BLOCK_SIZE, vengono
        aggiunti dei bytes di padding.
        """
        
        length = len(plaintext)

        if length % 16 != 0:
            #print("IF")
            """
            Suddivido il messaggio in blocchi di
            sottomessaggi composti da BLOCK_SIZE
            bytes.
            """
            padding_plaintext = pad(plaintext, AES.block_size)
        else:
            padding_plaintext = plaintext
        print(padding_plaintext)

        cipher = AES.new(self.key, AES.MODE_CBC)
        iv = cipher.iv
        ciphertext = cipher.encrypt(padding_plaintext)

        return ciphertext, iv
    


    def decryptData(self, ciphertext, iv):
        try:
            
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            plaintext = cipher.decrypt(ciphertext)
            padd_plaintext = unpad(plaintext,AES.block_size)
        except ValueError:
            return plaintext
        except Exception:
            raise Exception
        
        return padd_plaintext


m = hashlib.sha256()
m.update(b"cias")
print(m.digest())
for line in sys.stdin:
    #print(type(line))
    cipher = MyCipher(b"mysecretpassword")
    if 'quit' == line.rstrip:
        break
    ciphertext, iv = cipher.encryptData(bytes(line, 'utf-8'))
    print("[ CIFRATO ]: " + str(ciphertext))
    newCipher = MyCipher(b"mysecretpassword")
    plaintext = cipher.decryptData(ciphertext, iv)
    print("[ DECIFRATO ]: " + str(plaintext))

"""  
cipher = MyCipher(b"mysecretpassword")
ciphertext, iv = cipher.encryptData(b"ajcnjnvren qcni")
print(ciphertext)
newCipher = MyCipher(b"mysecretpassword")
plaintext = cipher.decryptData(ciphertext, iv)
print(plaintext)
"""
