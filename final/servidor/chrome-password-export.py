#!/usr/bin/env python

""" Exports Google Chrome passwords and password saving blacklist.  Only tested on Linux.  Output is formatted for use with the Password Exporter Firefox add-on (https://addons.mozilla.org/en-US/firefox/addon/2848/).

    Usage: chrome-password-export [options]

    Options:
      -h, --help            show a help message and exit
      -p, --passwords       export passwords (default)
      -b, --blacklist       export blacklist
      -i DBFILE, --input=DBFILE
                            Chrome password database file to use (default:
                            ./Login Data)
      -o OUTFILE, --output=OUTFILE
                            file to save passwords/blacklist to (default:
                            ./password-export.csv or ./blacklist-export.xml)

"""

# NOTES:
#  Passwords in Chrome are stored in <profile>/Login Data, a sqlite3 database,
#  in the table `logins`.  Here is the field mapping from chrome to
#  passwordexporter-CSV:
#  # Chrome field     -> passwordexporter field
#  0 origin_url       -> hostname (remove path, query, and fragment parts (e.g.
#                                  http://www.example.com))
#  3 username_value   -> username
#  5 password_value   -> password
#  (httpRealm is left blank, but may correspond to Chrome's signon_realm.)
#  1 action_url       -> formSubmitURL (just like in hostname, remove path,
#                                       query, and fragment parts)
#  2 username_element -> usernameField
#  4 password_element -> passwordField
#  At least on Linux, ***PASSWORDS ARE NOT ENCRYPTED OR OBFUSCATED.***
#
#  The blacklist in Chrome is stored in the same database, in the same table.
#  Only origin_url, signon_realm, and blacklisted_by_user will be populated and
#  blacklisted_by_user is 1 as opposed to the default 0.

import csv
import sqlite3
import StringIO
import urlparse
from optparse import OptionParser
from xml.sax.saxutils import quoteattr

parser = OptionParser(description = __doc__.splitlines()[0][1:])
parser.set_defaults(mode="passwords")
parser.add_option("-p", "--passwords", dest="mode", help="export passwords (default)", action="store_const", const="passwords")
parser.add_option("-b", "--blacklist", dest="mode", help="export blacklist", action="store_const", const="blacklist")
parser.add_option("-i", "--input", dest="dbfile", help="Chrome password database file to use (default: ./Login Data)", default="Login Data")
parser.add_option("-o", "--output", dest="outfile", help="file to save passwords/blacklist to (default: ./password-export.csv or ./blacklist-export.xml)", default=None)
options, args = parser.parse_args()
mode = options.mode

files = dict(passwords="password-export.csv", blacklist="blacklist-export.xml")
queries = dict(
 passwords="SELECT * FROM logins WHERE blacklisted_by_user = 0",
 blacklist="SELECT * FROM logins WHERE blacklisted_by_user = 1"
)

csv_top = "# Generated by Password Exporter; Export format 1.1; Encrypted: false\n"
csv_header = ["hostname", "username", "password", "formSubmitURL", "httpRealm", "usernameField", "passwordField"]

blacklist_skeleton = """<xml>
<entries ext="Password Exporter" extxmlversion="1.0.2" type="rejected">
%s
</entries>
</xml>"""
blacklist_entry = '<entry host=%s/>'

data_out = []

db = sqlite3.connect(options.dbfile if options.dbfile else "Login Data")
c = db.cursor()
c.execute(queries[mode])
data_in = c.fetchall()
c.close()
db.close()

for row in data_in:
 hostname_split = urlparse.urlsplit(row[0])
 hostname = urlparse.urlunsplit((hostname_split.scheme, hostname_split.netloc, "", "", ""))
 if mode == "passwords":
  username = row[3]
  password = row[5]
  formSubmitURL_split = urlparse.urlsplit(row[1])
  formSubmitURL = urlparse.urlunsplit((formSubmitURL_split.scheme, formSubmitURL_split.netloc, "", "", ""))
  httpRealm = ""
  usernameField = row[2]
  passwordField = row[4]
  if hostname_split.scheme != "chrome-extension" and formSubmitURL_split.scheme != "chrome-extension":
   row_out = [hostname, username, password, formSubmitURL, httpRealm, usernameField, passwordField]
   data_out.append(row_out)
 elif mode == "blacklist":
  if hostname_split.scheme != "chrome-extension" and hostname.strip() != "":
   data_out.append(hostname)

out_file = open(options.outfile if options.outfile else files[mode], "w")

if mode == "passwords":
 csv_strio = StringIO.StringIO()
 writer = csv.writer(csv_strio, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
 writer.writerow(csv_header)
 writer.writerows(data_out)
 out_file.write(csv_top)
 out_file.write(csv_strio.getvalue())
 csv_strio.close()
elif mode == "blacklist":
 out_file.write(blacklist_skeleton % "\n".join(map(lambda host: blacklist_entry % quoteattr(host), data_out)))

out_file.close()