def Trouve (phrase, recherche):
    find = False
    for i in range (len(phrase)):
        find = True
        for j in range (len(recherche)):
            if (phrase[i+j] != recherche[j]):
                find = False
            #endif
            if (find):
                return i
    return -1
#endef

demande = input("Saisir une phrase : ")
cherche = input("Saisir une recherche : ")

print(Trouve(demande,cherche))