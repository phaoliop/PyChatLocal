import socket

#Recibe conexiones
escucha = socket.socket()

#Conexiones de multiples interfaces, por puerto 1234
escucha.bind(('',1234))

#Numero de conexiones a la espera
escucha.listen(3)
conexiones = {}

#Aceptar la conexion de cliente 1 y 2
conn, addr = escucha.accept()
print "Se ha conectado alguien desde la direccion: "+ addr[0]
conn2, addr2 = escucha.accept()
print "Se ha conectado alguien desde la direccion: "+ addr[0]

while True:
	#Intercambio de mensajes entre clientes
	recibido = conn.recv(1024)
	conn2.send(addr[0]+">"+recibido)

	recibido2 = conn2.recv(1024)
	conn.send(addr2[0]+">"+recibido2)

#Cerrar conexiones
conn.close()
conn2.close()
escucha.close()

