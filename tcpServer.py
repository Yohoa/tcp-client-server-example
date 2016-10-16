#  Simple socket server
from socket import *
myHost = ''
myPort = 5000

sockobj = socket( AF_INET, SOCK_STREAM)
sockobj.bind( (myHost, myPort) )
sockobj.listen(5)

while(1):
	connection, address = sockobj.accept()
	print( 'server connected by ', address  )
	while(1):
		data = connection.recv(1024)
		if not data: break
		connection.send(b'Echo => '+data)
	connection.close()