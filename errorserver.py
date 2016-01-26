import socket, traceback, os
host = ''
port = 51423

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
print "waiting for connections..."
s.listen(1)

while 1:
	try:
		clientsock, clientaddr = s.accept()
	except KeyboardInterrupt:
		print "KeyboardInterrupt:"
		raise
	except:
		traceback.print_exc()
		print "traceback.print_exc()"	
		continue

	try:
		print "Got connection from", clientsock.getpeername()
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		traceback.print_exc()
		
	print clientaddr

	try:
		clientsock.close()
	except KeyboardInterrupt:
		raise
	except:
		traceback.print_exc()
		
		  
