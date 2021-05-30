import socket
from _thread import *
import sys
import pickle
from Player import Player
import random

MAX_CLIENTS = 5
server = "192.168.1.155"
port = 5555



players = []
IDs = []
for x in range(MAX_CLIENTS):
    IDs.append(x)
    color = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
    players.append(Player(color))



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

#connection count
s.listen(MAX_CLIENTS)
print("waiting for a conection, server started")


def read_pos(str):
	str = str.split(",")
	return int(str[0]), int(str[1])


def make_pos(tup):
	return str(tup[0]) + "," + str(tup[1])




def threaded_client_old(conn):
    conn.send(str.encode("Connected"))

    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                
                print("Received:  ", reply)
                print("Sending: ", reply)

            conn.sendall(str.encode("steven"))
        except:
            break
    
    print("Lost connection")
    conn.close()







def threaded_client(conn, ID):
    conn.send(pickle.dumps(players[ID]))
    while True:
        try:
            playerData = pickle.loads(conn.recv(2048))
            players[ID] = playerData

            if not playerData:
                print("Disconnected")
                break
            else:
                print("Received:  ", playerData)
            conn.sendall(pickle.dumps(players))
        except:
            break
    
    IDs.append(ID)
    IDs.sort()

    print("Lost connection")
    conn.close()



while True:
    conn, addr = s.accept()
    newId = IDs.pop(0)
    start_new_thread(threaded_client, (conn, newId,))
    print("Connected to: ", addr)