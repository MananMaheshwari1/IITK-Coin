import socket
import json

dict = {"180001" : {"name" : "A", "coins" : "2"}, "180002" : {"name" : "B", "coins" : "3"}, "180003" : {"name" : "C", "coins" : "4"}, "180004" : {"name" : "D", "coins" : "5"} , "180005" : {"name" : "E", "coins" : "6"}}
data_string = json.dumps(dict) #data serialized
res = bytes(data_string, 'utf-8')
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8080       # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(res)
    data = s.recv(1024)
    data = data.decode()
    dict = json.loads(data)
    print('Received: ', repr(data))

