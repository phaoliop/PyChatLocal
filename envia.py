
import socket
import sys

#Prueba 1
host = sys.argv[1]

try:
	sock = socket.socket()
	sock.connect((host,1234))

	while True:
		mensaje = raw_input()
		sock.send(mensaje+"\n")
		data = sock.recv(1024)
		print data
except:
	print "Host no disponible"
sock.close()
