#MODULE IMPORTS

import socket
import sys
import datetime
import termcolor

#GETTING THE IP

choice = input(termcolor.colored("Do you have the target IP? ",color='green'))
if ("y" in choice.lower()):
	target_ip = input(termcolor.colored("Enter IP address (IPv4): ",color="magenta"))
elif ("n" in choice.lower()):
	target_address = input(termcolor.colored("Enter target address: ",color="yellow"))
	target_ip = socket.gethostbyname(target_address)
else:
	print(termcolor.colored("IP or address is a must :( ",color='red'))
	sys.exit()

#OPEN PORT DETECTION

print(termcolor.colored(">>"*50,color="red",attrs=['blink']))
print(termcolor.colored("Scanning target: {}".format(target_ip),color='red',attrs=['reverse']))
print(termcolor.colored("Started At: {}".format(datetime.datetime.now()),color='green',attrs=['underline','bold']))
print(termcolor.colored("<<"*50,color='red',attrs=["blink"]))
try:
	for port in range(1,1024):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target_ip,port))
		if (result == 0):
			print(termcolor.colored("Port {} is open".format(port),color='blue',attrs=['bold']))
		s.close()
except KeyboardInterrupt:
	print(termcolor.colored("Closing the scanner",color='magenta'))
	sys.exit()
except socket.gaierror:
	print(termcolor.colored("unable to establish connection",color='red',attrs=['reverse','blink']))
print(termcolor.colored("-"*50,color='red',attrs=['red']))
print(termcolor.colored("Finished At: {}".format(datetime.datetime.now()),color='green',attrs=['underline','bold']))