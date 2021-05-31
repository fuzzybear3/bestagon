import socket
from _thread import *
import sys
import pickle
from Player import Player
import random

MAX_CLIENTS = 5
MAX_BUFFER = 40
server = "192.168.1.155"
port = 5555



players = []
defaltPlayers = []
IDs = []
for x in range(MAX_CLIENTS):
    IDs.append(x)
    color = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
    temp = []
    temp.append(Player(color))
    players.append(temp)
    defaltPlayers.append(Player(color))



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

#connection count
s.listen(MAX_CLIENTS)
print("waiting for a conection, server started")






def ingresData(playerData):
    for x in range(0, MAX_CLIENTS):
        if len(players[x]) > MAX_BUFFER:
            players[x].pop()
        players[x].append(playerData)



def threaded_client(conn, ID):
    conn.send(pickle.dumps(defaltPlayers[ID]))
    #empty buffer
    players[ID].clear()
    while True:
        try:
            recivedData = conn.recv(2048)
            #print(recivedData)
            if recivedData != str.encode("ping"):
                playerData = pickle.loads(recivedData)
                ingresData(playerData)

            if not recivedData:
                print("Disconnected")
                break
            else:
                #print("Received:  ", playerData)
                pass
            conn.sendall(pickle.dumps(players[ID]))
            players[ID].clear()
            
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