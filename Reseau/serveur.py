import socket
import time
import threading

class ClientThread(threading.Thread):
    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket

        print("\n[+] Nouveau thread pour %s %s" % (self.ip, self.port))
    #enddef

    def run(self):
        print("Connexion de %s %s" % (self.ip, self.port))
        response = self.clientsocket.recv(255)
        if response != "":
            print(response.decode('utf-8'))
        print("Client Déconnecté...")
    #enddef
#endclass

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("",15555))

while True:
    s.listen(10)
    print("J'écoute....")
    (clientsocket, (ip, port)) = s.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()
#endwhile

client.close()
stock.close()