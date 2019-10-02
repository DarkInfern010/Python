def Purge (phrase, suppr):
    return phrase.replace(suppr,'')
#enddef

demande = input("Saisir une phrase : ")

recherche = input("Saisir une suppresion : ")
rechercheP = [str(c) for c in str(recherche)]

for i in range (len(rechercheP)):
    demande = Purge(demande, rechercheP[i])
#endofr

print(demande)
