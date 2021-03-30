#client dj4e
import socket

sckt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=80
url="data.pr4e.org"
sckt.connect((url,port))
cmd = "GET http://"+srv+" HTTP/1.0\r\n\r\n".encode()
sckt.send(cmd)

while True:
    data = sckt.recv(512)
    if(len(data)<1) :
        break
    print(data.decode(),end="")

sckt.close()