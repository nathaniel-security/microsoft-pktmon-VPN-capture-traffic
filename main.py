import os 
import socket



os.system('pktmon start --capture')


domain_name = 'google.com'
ip_add = socket.gethostbyname(domain_name)

os.system("ping " + domain_name)

os.system('pktmon stop')
os.system('pktmon etl2txt PktMon.etl')

os.system('echo ' + ip_add + " >> ip")
os.system("clip < ip")





