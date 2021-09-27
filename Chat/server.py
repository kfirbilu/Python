import threading
import socket

host = '127.0.0.1' # local host (ip of the server)
port = 55555

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port)) #bining the server to the host and port
server.listen() # server starts listening for new connections

clients = []
nicknames = []

def broadcast(message):  # broadcasts a message to all clients
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat!".encode('ascii'))
            nicknames.remove(nickname)
            break


def recieve():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}!")
        broadcast(f"{nickname} joined the chat!".encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))

        thread = threading.Thread(target=handle,args=(client,))
        thread.start()

print("Server is listening...")
recieve()


