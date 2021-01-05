from zipfile import ZipFile

# Boucle pour essayer les 999 999 combinaisons
for i in range (0,1000000):
    password = ""
    if (i < 10): # Ajout de 5 zéros pour faire un mot de passe de 6 chiffres
        password = "00000"+str(i)
    elif (i < 100): # Ajout de 4 zéros pour faire un mot de passe de 6 chiffres
        password = "0000"+str(i)
    elif (i < 1000): # Ajout de 3 zéros pour faire un mot de passe de 6 chiffres
        password = "000"+str(i)
    elif (i < 10000): # Ajout de 2 zéros pour faire un mot de passe de 6 chiffres
        password = "00" + str(i)
    elif (i < 100000): # Ajout de 1 zéros pour faire un mot de passe de 6 chiffres
        password = "0"+str(i)
    else:
        password = str(i)
    try:
        # Essaye de la combinaison sur le fichier pour l'ouvrir
        with ZipFile('document.zip') as myzip:
            with myzip.open('flag.txt', pwd=password.encode()) as myfile:
                print(myfile.read())
    except:
        continue