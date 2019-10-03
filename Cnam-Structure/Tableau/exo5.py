import random

def estCreuse (matrice, nbL, nbC):
    total = 0
    for i in range (nbL):
        for j in range (nbC):
            if (matrice[i][j] == 0):
                total += 1
            #endif
        #endfor
    #endfor
    if ((total / (nbL * nbC)) >= 0.9):
        return "Matrice est creuse"
    else:
        return "Matrice non creuse"
#endef

nbLignes = int(input("Saisir le nb de lignes : "))
nbColonnes = int(input("Saisir le nb de colonnes : "))

tab = [[random.randint(0,1) for i in range(nbColonnes)] for j in range(nbLignes)]

if (nbLignes > 0 and nbColonnes > 0):
    print(estCreuse(tab,nbLignes,nbColonnes))
else:
    print("La matrice ne peut pas avoir de ligne = 0 ou colonne = 0")

print("La complexité est de n²")