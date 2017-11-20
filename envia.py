
import socket
import sys

#Prueba cliente
host = sys.argv[1]

try:
	#Conectar
	sock = socket.socket()
	sock.connect((host,1234))

	while True:
		#Intercambio de mensajes
		mensaje = raw_input()
		sock.send(mensaje+"\n")
		data = sock.recv(1024)
		print data
except:
	print "Host no disponible"

#Cerrar conexion
sock.close()
