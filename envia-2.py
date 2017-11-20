
import socket
import sys

#Prueba cliente
host = sys.argv[1]

#try:
sock = socket.socket()
sock.connect((host,1234))
while True:
    
    mensaje = input()
    mensaje += "\n"
    sock.send(mensaje.encode())
    data = sock.recv(1024)
    print (data.decode())
#except:
#    print ("Ha ocurrido un error.")

sock.close()
