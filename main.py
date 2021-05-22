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

