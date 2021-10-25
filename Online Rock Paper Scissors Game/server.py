import pickle
import socket
from _thread import *
from game import Game
from player import Player
import pickle

serverIP = "192.168.183.128"  # local ip address
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((serverIP, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for connection, Server Started")

connected = set()
games = {}
idCount = 0


def threaded_client(connection, p, gameId):
    global idCount
    connection.send(str.encode(str(p)))
    reply = ""

    while True:
        try:
            data = connection.recv(4069).decode()
            if gameId in games:
                game = games[gameId]

                if not data:
                    break

                else:
                    if data == "reset":
                        game.resetWent()

                    elif data != "get":
                        game.play(p, data)
                    reply = game
                    connection.sendall(pickle.dumps(reply))

            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)

    except:
        pass
    idCount-=1
    connection.close()


while True:
    connection, addr = s.accept()
    print("Connected to: ", addr)
    idCount += 1
    p = 0
    gameId = (idCount - 1) // 2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1

    start_new_thread(threaded_client, (connection, p, gameId))
