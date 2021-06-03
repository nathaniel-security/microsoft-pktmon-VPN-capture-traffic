import os 
import socket
import time


os.system('pktmon start --capture')
try:
	os.remove('ip')

domain_name = 'google.com'
ip_add = socket.gethostbyname(domain_name)

os.system("ping " + domain_name)
time.sleep(10)
os.system('pktmon stop')
time.sleep(10)
os.system('pktmon etl2txt PktMon.etl')
time.sleep(10)
os.system('echo ' + ip_add + " >> ip")
os.system("clip < ip")
