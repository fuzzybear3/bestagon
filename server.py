import socket
from _thread import *
import sys
import pickle



MAX_CLIENTS = 5
server = "192.168.1.155"
port = 5555



lastPos = []
IDs = []
for x in range(MAX_CLIENTS):
    IDs.append(x)
    lastPos.append((0,0))
clients = []
gameStatBuffer = []

print(lastPos)


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

    posData = ""
    while True:
        try:
            data = conn.recv(2048)
            posData = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                if posData != "ping":
                    print("Received:  ", posData)
                    lastPos[ID] = read_pos(posData)
            conn.sendall(pickle.dumps(lastPos))
        except:
            break
    
    IDs.append(ID)
    IDs.sort()

    print("Lost connection")
    conn.close()


def distributer():
    mesg = ""
    while True:
        try:
            Datlist = ["yousuck","dick","andvagina"]
            print(clients[0])
            for x in clients:
                print("bob")
                data = x.recv(2048)
                print("fuuuuck")
                mesg = data.decode("utf-8")
                print("Received:  ", mesg)

            if not data:
                print("Disconnected")
            else:
                print("Received:  ", mesg)
                
            #conn.sendall(str.encode(clients[0]))
        except:
            print("Lost connection")
            conn.close()
    
    
#conn, addr = s.accept()
#conn.send(str.encode("Connected"))
#print("Connected to: ", addr)
#clients.append(conn)
#start_new_thread(distributer, ())


while True:
    conn, addr = s.accept()
    newId = IDs.pop(0)
    conn.send(str.encode(str(newId)))
    start_new_thread(threaded_client, (conn, newId,))
    print("Connected to: ", addr)