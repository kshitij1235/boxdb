# An example script to connect to Google using socket
# programming in Python
import socket # for socket
import sys

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print ("Socket successfully created")
except socket.error as err:
	print ("socket creation failed with error %s" %(err))

# default port for socket
port = 8080


host_ip = "192.168.1.100"


# connecting to the server
s.connect((host_ip, port))
while True : 
    input_cmd=input(">> ")
    s.send(input_cmd.encode())
    print("recived_byte - > " , s.recv(1028).decode())

