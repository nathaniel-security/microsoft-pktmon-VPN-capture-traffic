import os 
import socket
import time

def check_admin():
	import ctypes, os
	try:
		is_admin = os.getuid() == 0
	except AttributeError:
		is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

	#print (is_admin)
	return is_admin

if(check_admin()):
	os.system('pktmon start --capture')
	domain_name = 'wehost.co.in'

	ip_add = socket.gethostbyname(domain_name)
	
	os.system("ping " + domain_name)
	time.sleep(10)
	os.system('pktmon stop')
	time.sleep(10)
	os.system('pktmon etl2txt PktMon.etl')
	time.sleep(10)
	os.system('echo ' + ip_add + " >> ip")
	os.system("clip < ip")
   
else:
	print("Need admin privileges")