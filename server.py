import socket
import json

s = socket.socket()
print("Socket creaated successfully")
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8080       # The port used by the server
s.bind((HOST,PORT))
print("Socket binded to port %s"%(PORT))
s.listen(5)
print("Socket is listening")
conn, addr = s.accept()
ret = {}
with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        data = data.decode()
        dict = json.loads(data)
        for x in dict:
            rollnum = x
            value = dict[x]
            for y in value:
                if y == "coins":
                    num = value[y]
                    ret[rollnum] = num
        val = json.dumps(ret)
        conn.send(val.encode('utf-8'))

