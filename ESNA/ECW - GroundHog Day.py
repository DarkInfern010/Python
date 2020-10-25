import socket
import re
import hashlib

#Variables de solution des missions
morse_alphabet = dict()
destroy_alphabet = dict()
unicode_alphabet = dict()
polybe_alphabet = dict()

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

donneeT = donnee[indiceDeb+4:indiceFin]

for i in range (len(alphabet)):
    unicode_alphabet[donneeT.split('\\')[i]] = alphabet[i]
#endfor
print(unicode_alphabet)

client.send(b" ")
donnee = str(client.recv(1024))

for j in range (20):
    #Reception de l'eniglme en morse
    donnee = str(client.recv(1024))
    print(donnee)

    indiceDeb = donnee.find("is ")
    indiceFin = donnee.find(" decyphered")

    enigme = donnee[indiceDeb+4:indiceFin].split("\\")
    reponse = ""
    for i in range (len(enigme)):
        reponse += unicode_alphabet.get(enigme[i])
    #endfor
    print(reponse)
    client.send(reponse.encode())
#endfor

print(client.recv(1024))
print(client.recv(1024))
client.send(b"\\n")
print(client.recv(1024))

#-----Polybe-----

client.send(alphabet.encode())
donnee = str(client.recv(1024))
print(donnee)

indiceDeb = donnee.find("is ")
indiceFin = donnee.find("\\n")

donneeT = re.findall('..',donnee[indiceDeb+3:indiceFin])

for i in range (len(alphabet) - 5):
    polybe_alphabet[donneeT[i]] = alphabet[i]
#endfor
polybe_alphabet['52'] = 'v'
polybe_alphabet['5252'] = 'w'
polybe_alphabet['53'] = 'x'
polybe_alphabet['54'] = 'y'
polybe_alphabet['55'] = 'z'
print(polybe_alphabet)

client.send(b" ")
donnee = str(client.recv(1024))
print(donnee)

for j in range (20):
    #Reception de l'eniglme en morse
    donnee = str(client.recv(1024))
    print(donnee)
    indiceDeb = donnee.find("is ")
    indiceFin = donnee.find(" decyphered")

    enigme = re.findall('..',donnee[indiceDeb+3:indiceFin])
    print(enigme)
    for i in range(len(enigme) - 1):
        if enigme[i] == '52' and enigme[i + 1] == '52':
            enigme[i] = '5252'
            del enigme[i + 1]
        #endif
    #endfor

    reponse = ""
    for i in range (len(enigme)):
        reponse += polybe_alphabet.get(enigme[i])
    #endfor
    print(reponse)
    client.send(reponse.encode())
#endfor

print(client.recv(1024))
print(client.recv(1024))
client.send(b"\\n")
print(client.recv(1024))

#-----XOR-----

client.send(b"a")
donnee = str(client.recv(1024))
print(donnee)

client.send(b"a")
donnee = str(client.recv(1024))
print(donnee)

donnee = str(client.recv(1024))
print(donnee)

indiceDeb = donnee.find("is ")
indiceFin = donnee.find(" decyphered")

enigme = donnee[indiceDeb+3:indiceFin]
print(enigme)
print(list(enigme))

test = '\x04\x17\x1f$-6\x16\n\x16+*$\x11'
print(test)
print(list(test))

print(len(enigme))
for i in range (len(enigme)):
    enigme[i] = bin(ord(enigme[i]))
#endfor
print(enigme)

client.close()
