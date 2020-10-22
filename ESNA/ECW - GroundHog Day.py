import socket

#Variables de solution des missions
morse_alphabet = dict()
destroy_alphabet = dict()
unicode_alphabet = dict()

#Fonction permettant de split les chaines par caractères
def splitP(string):
    return [char for char in string]
#endef

#Variables de connexion Telnet
HOST = "challenge-ecw.fr"
PORT = 10007

#Connexion au serveur TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

#Message pour naviguer dans le menu
donnee = client.recv(1024)
print(donnee)
client.send(b"\n")

donnee1 = client.recv(1024)
print(donnee1)

#Variable permettant la récuperation les différents alphabets (avec son split)
alphabet = "abcdefghijklmnopqrstuvwxyz"

#-----MORSE-----

#Reception des données avec remplissage du dico morse
client.send(alphabet.encode())
donnee = str(client.recv(1024))

indiceDeb = donnee.find("is ")
indiceFin = donnee.find("\\n")

donneeT = donnee[indiceDeb+3:indiceFin].split(" ")
print(donneeT)
for i in range (len(donneeT)):
    morse_alphabet[donneeT[i]] = alphabet[i]
#endfor
print(morse_alphabet)

#Envoie d'une message vide pour passer
client.send(b" ")
donnee = client.recv(1024)

for j in range (20):
    #Reception de l'eniglme en morse
    donnee = str(client.recv(1024))
    print(donnee)
    indiceDeb = donnee.find("is ")
    indiceFin = donnee.find(" decyphered")

    enigme = donnee[indiceDeb+3:indiceFin].split(" ")
    reponse = ""
    for i in range (len(enigme)):
        reponse += morse_alphabet.get(enigme[i])
    #endfor
    print(reponse)
    client.send(reponse.encode())
#endfor

print(client.recv(1024))
print(client.recv(1024))
client.send(b"\\n")
print(client.recv(1024))


#-----REVERSE-----

#Reception des données
client.send(b" ")
client.send(b" ")
print(client.recv(1024))
print(client.recv(1024))

for j in range (20):
    donnee = str(client.recv(1024))
    print(donnee)
    indiceDeb = donnee.find("is ")
    indiceFin = donnee.find(" decyphered")

    enigme = splitP(donnee[indiceDeb + 3:indiceFin])
    reponse = ""
    for i in range(len(enigme)):
        reponse += enigme[len(enigme) - 1 - i]
    # endfor
    client.send(reponse.encode())
    print(reponse)
#endfor

print(client.recv(1024))
print(client.recv(1024))
client.send(b"\\n")
print(client.recv(1024))

#-----Destroy alphabet-----

#Reception des données avec remplissage du dico destroy
client.send(alphabet.encode())
donnee = str(client.recv(1024))

indiceDeb = donnee.find("is ")
indiceFin = donnee.find("\\n")

donneeT = splitP(donnee[indiceDeb+3:indiceFin])
for i in range (len(donneeT)):
    destroy_alphabet[donneeT[i]] = alphabet[i]
#endfor
print(destroy_alphabet)

#Envoie d'une message vide pour passer
client.send(b" ")
donnee = client.recv(1024)

for j in range (20):
    #Reception de l'eniglme en morse
    donnee = str(client.recv(1024))
    print(donnee)
    indiceDeb = donnee.find("is ")
    indiceFin = donnee.find(" decyphered")

    enigme = splitP(donnee[indiceDeb+3:indiceFin])
    reponse = ""
    for i in range (len(enigme)):
        reponse += destroy_alphabet.get(enigme[i])
    #endfor
    print(reponse)
    client.send(reponse.encode())
#endfor

print(client.recv(1024))
print(client.recv(1024))
client.send(b"\\n")
print(client.recv(1024))

#-----Unicode alphabet-----

#Reception des données avec remplissage du dico destroy
client.send(alphabet.encode())
donnee = str(client.recv(1024))

indiceDeb = donnee.find("is ")
indiceFin = donnee.find("\\n")

donneeT = donnee[indiceDeb+3:indiceFin]
str = "\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea"

for i in range (len(donneeT)-3):
    unicode_alphabet[donneeT[i:i+3]] = alphabet[i]
#endfor
print(unicode_alphabet)

for i in range (len(donneeT)):
    morse_alphabet[donneeT[i]] = alphabet[i]
#endfor
print(morse_alphabet)

client.send(b" ")
donnee = str(client.recv(1024))


client.close()
