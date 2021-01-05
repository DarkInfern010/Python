from socket import socket
import hashlib
from word2number import w2n

host = "ctf.esnhack.fr"
port = 3004

sock = socket()
sock.connect(("ctf.esnhack.fr", 3004))
print(sock.recv(1024).decode())
sock.send("yes".encode())
sock.send("\n".encode())

for i in range (20):
    donnee = sock.recv(1024).decode()
    print(str(i) + " : " + donnee)

    data = donnee.split()
    donneeT = data[6]
    protocole = data[3]

    if (protocole == "md5"):
        result = hashlib.md5(donneeT.encode())
        sock.send(result.hexdigest().encode())
        sock.send("\n".encode())
    #endif

    elif (protocole == "sha1"):
        result = hashlib.sha1(donneeT.encode())
        sock.send(result.hexdigest().encode())
        sock.send("\n".encode())
    # endif

#endfor

for h in range (100):
    # Reception de l'eniglme en morse
    donnee = str(sock.recv(1024))
    print(str(h+20) + " : " + donnee)
    indiceDeb = donnee.find("of ")
    indiceFin = donnee.find(" ?")

    enigme = donnee[indiceDeb + 3:indiceFin]
    enigme = enigme.replace("one hundred", "100")
    string1 = enigme.split(" ")
    res = ""

    for i in range(len(string1)):
        if (i % 2 == 0):
            res += str(w2n.word_to_num(string1[i]))
        else:
            res += string1[i]
    sock.send(str(eval(res)).encode())
    sock.send("\n".encode())
#endfor