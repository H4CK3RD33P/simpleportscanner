#MODULE IMPORTS

import socket
import sys
import datetime

#GETTING THE IP

choice = input("Do you have the target IP? ")
if ("y" in choice.lower()):
	target_ip = input("Enter IP address (IPv4): ")
elif ("n" in choice.lower()):
	target_address = input("Enter target address: ")
	target_ip = socket.gethostbyname(target_address)
else:
	print("IP or address is a must :( ")
	sys.exit()

#OPEN PORT DETECTION

print(">>"*50)
print("Scanning target: {}".format(target_ip))
print("Started At: {}".format(datetime.datetime.now()))
print("<<"*50)
try:
	for port in range(1,1024):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target_ip,port))
		if (result == 0):
			print("Port {} is open".format(port))
		s.close()
except KeyboardInterrupt:
	print("Closing the scanner")
	sys.exit()
except socket.gaierror:
	print("unable to establish connection")
print("-"*50)
print("Scanning finished at {}".format(datetime.datetime.now()))
