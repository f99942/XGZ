#!/bin/python
# -*- coding: utf-8 -*-

import sqlite3

print "MOZILLA-FIREFOX"
con =sqlite3.connect("/home/manu/.mozilla/firefox/zo5lgjok.default/cookies.sqlite")
#coneccion=sqlite3.connect(':memory:')
cur=con.cursor()
print u"La base de datos se abrió correctamente"

cur.execute("select host, path, baseDomain, lastAccessed, expiry, name, value from moz_cookies")

for i in cur:
	print "Host = ", i[0]
	print "Ruta = ", i[1]
	print "Dominio Base = ", i[2]
	print "Ultimo Acceso = ", i[3]
	print "Expira = ", i[4]
	print "Nombre = ", i[5]
	print "Value =  ", i[6], "\n"

con.close()
	

print "GOOGLE-CHROME"
con=sqlite3.connect("/home/manu/.config/google-chrome/Default/Cookies")
cur=con.cursor()

cur.execute("select host_key, name, value, path, httponly, last_access_utc from cookies")

for i in cur:
        print "Host = ", i[0]
        print "Nombre = ", i[1]
        print "Value = ", i[2]
        print "Ruta = ", i[3]
        print "httponly = ", i[4]
        print "Ultimo acceso = ", i[5], "\n"

con.close()
