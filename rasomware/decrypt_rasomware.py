#!/usr/bin/python

"""
Referencias
http://stackoverflow.com/questions/5000946/how-to-generate-strong-one-time-session-key-for-aes-in-python
http://stackoverflow.com/questions/20852664/python-pycrypto-encrypt-decrypt-text-files-with-aes
http://pycryptodome.readthedocs.org/en/latest/src/examples.html
https://www.dlitz.net/software/pycrypto/api/current/Crypto.PublicKey.RSA-module.html
http://stackoverflow.com/questions/6886240/python-pycrypto-sending-encrypted-data-over-network

Este script sirve para descirar la llave AES
"""
from base64 import b64encode
from base64 import b64decode

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP



p = open('privateKey.pem','r')
private_key = RSA.importKey(p.read())
p.close()
cipher_rsa = PKCS1_OAEP.new(private_key)
f = open('llave.txt','rb')
keyImport =  b64decode(f.readline())
f.close()
key3 = b64decode(cipher_rsa.decrypt(keyImport))
print b64encode(key3).decode('utf-8')
#decrypt_file('image.jpg.enc', key3)
