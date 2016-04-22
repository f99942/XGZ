#!/usr/bin/python

"""Referencias
http://stackoverflow.com/questions/5000946/how-to-generate-strong-one-time-session-key-for-aes-in-python
http://stackoverflow.com/questions/20852664/python-pycrypto-encrypt-decrypt-text-files-with-aes

Este script genera las llaves publicas y privadas y las exporta
a un archivo PEM, por lo tanto se ejecuta de lado del C&C 

Instalar 
pip install crypto
"""
import Crypto
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from base64 import b64encode
from base64 import b64decode
import os
import binascii

KEY_LENGTH = 1024  # Key size (in bits)
random_gen = Random.new().read  
keypair_snowden = RSA.generate(KEY_LENGTH, random_gen)
pubkey_snowden  = keypair_snowden.publickey()
public_key = keypair_snowden.publickey().exportKey("PEM") 
private_key = keypair_snowden.exportKey("PEM") 
f = open('privateKey.pem','w')
f.write(private_key)
f.close()

p = open('publicKey.pem','w')
p.write(public_key)
p.close()

print public_key
print
print
print
print private_key

