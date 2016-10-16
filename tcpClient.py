#  Simple socket client
import sys
from socket import *
serverHost = '127.0.0.1'
serverPort = 5000

message = ['test for network']

sockobj = socket( AF_INET, SOCK_STREAM)
sockobj.connect( (serverHost, serverPort) )

for line in message:
	line = line.encode("utf-8")
	sockobj.send(line)
#sockobj.send(b"5\n")
	data = sockobj.recv(1024)
	print( 'client received: ', data.decode("utf-8") )

sockobj.close()