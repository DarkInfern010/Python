from uuid import getnode as get_mac

def crypt (nom_fichier_clair, nom_fichier_crypt, key):
    file = open(nom_fichier_clair, "r")
    lines = file.readlines()
    file.close()
    for line in lines:
        fichier = open(nom_fichier_crypt, "w")
        s = ""
        for i in line:
            s += str(ord(i) + key) + "-"
        s = s[:-1]
        fichier.write(s)
        fichier.close()
    # endfor
#enddef

def uncrypt (nom_fichier_crypter, nom_fichier_res, key):
    file = open(nom_fichier_crypter, "r")
    lines = file.readlines()
    file.close()
    for line in lines:
        fichier = open(nom_fichier_res, "w")
        s = ""
        tab = line.split("-")
        for i in tab:
            s += chr(int(i)-key)
        fichier.write(s)
        fichier.close()
    # endfor
#enddef

def cryptDelete (nom_fichier, key):
    file = open(nom_fichier, "r")
    lines = file.readlines()
    file.close()
    for line in lines:
        fichier = open(nom_fichier, "w")
        s = ""
        for i in line:
            s += str(ord(i) + key) + "-"
        s = s[:-1]
        fichier.write(s)
        fichier.close()
    # endfor
#enddef

def uncryptDelete (nom_fichier, key):
    file = open(nom_fichier, "r")
    lines = file.readlines()
    file.close()
    for line in lines:
        fichier = open(nom_fichier, "w")
        s = ""
        tab = line.split("-")
        for i in tab:
            s += chr(int(i) - key)
        fichier.write(s)
        fichier.close()
    # endfor
#endfor

mac = get_mac()
crypt("Clair.txt", "Crypt.txt", mac)
uncrypt("Crypt.txt", "Uncrypt.txt", mac)
cryptDelete("Clair.txt", mac)
uncryptDelete("Clair.txt", mac)