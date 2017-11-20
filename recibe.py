import socket

#Recibe conexiones
escucha = socket.socket()

#Conexiones de cualquier direccion, por puerto 1234
escucha.bind(('',1234))

#Numero de conexiones a la espera
escucha.listen(3)
conexiones = {}

#Aceptar la conexion
conn, addr = escucha.accept()
print "Se ha conectado alguien desde la direccion: "+ addr[0]
conn2, addr2 = escucha.accept()
print "Se ha conectado alguien desde la direccion: "+ addr[0]

while True:
	recibido = conn.recv(1024)
	conn2.send(addr[0]+">"+recibido)

	recibido2 = conn2.recv(1024)
	conn.send(addr2[0]+">"+recibido2)

conn.close()
conn2.close()
escucha.close()

