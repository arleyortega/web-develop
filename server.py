import socket
import threading

host ='localhost'
port ='5000'
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM ) #SF_INET indica socket tipo internet, sock_stream significa que se utiliza el protocolo tcp
server.bind((host,port)) # el bind es la funcion con la cual seleccionamos los parametros de host y puerto
server.listen()
print("server  runs on {host} : puerto {port}")

clients = []
usernames =[]

def broadcast(message, _client):# este es el brodcast y enviara un mensaje a cada uno de los client  en la lista cliente , excepto a _cliente el cual es el cliente que envia el mensaje
    for client in cliente:
        if client != _client:
             client.send(message)

def handle_messages(client):
    try:
    message = client.recv(1024)
    broadcast(message,client)
    except:

