from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
import sys
import hashlib
import logging

"""
La dimensione del blocco è pari a 128 bits.
"""
BLOCK_SIZE = 16

class Security:
    


    def __init__(self, confidkey):

        if(len(confidkey)!=16):
            raise Exception("La dimensione della chiave deve essere  pari a BLOCK_SIZE bytes")

        """
        Trasformo la chiave in un array di bytes
        se già non lo fosse.
        """
        if(isinstance(confidkey, bytes)):
            self.confidkey = confidkey
        else:
            self.confidkey = bytes(confidkey, 'utf-8')



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
            """
            Suddivido il messaggio in blocchi di
            sottomessaggi composti da BLOCK_SIZE
            bytes.
            """
            print(str(plaintext))
            padding_plaintext = pad(plaintext, AES.block_size, style='pkcs7')
            print(len(padding_plaintext))
        else:
            padding_plaintext = plaintext

        cipher = AES.new(self.confidkey, AES.MODE_CBC, bytes([0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]))

        iv = cipher.iv
        ciphertext = cipher.encrypt(padding_plaintext)

        return ciphertext, iv
    


    def decryptData(self, ciphertext):
        try:            
            cipher = AES.new(self.confidkey, AES.MODE_CBC, bytes([0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]))
            plaintext = cipher.decrypt(ciphertext)
            padd_plaintext = unpad(plaintext,AES.block_size, style='pkcs7')
        except ValueError:
            return plaintext
        except Exception:
            raise Exception
        
        return padd_plaintext


    
    def message_integrity(self, message):
        """
        Faccio un controllo sul tipo del parametro
        di cui deve essere calcolato il digest.
        """
        if not isinstance(message, bytes):
            raise Exception("Il messaggio deve essere una sequenza di bytes.")

        """
        Inserisco il messaggio di cui devo
        calcolarmi il digest.
        """
        m = hashlib.sha256()
        m.update(message)

        """
        Mi calcolo il valore del digest del messaggio.
        """
        digest = m.digest()

        return digest
