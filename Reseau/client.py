import socket
import socket, sys, os
import time

hote = ["localhost"]
port = 15555 #11111

for i in hote:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((i, port))

    print("Connection on {}".format(port))

    s.send("Hello".encode())

    print("Close")
    s.close()
#endfor
