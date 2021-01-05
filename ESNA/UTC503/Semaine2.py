#Exercice 1 (Pair et Impair)
def estPair(n):
    if (n == 0):
        return "Le nombre est pair"
    elif (n == 1):
        return "Le nombre n'est pas pair"
    else:
        return estPair(n - 2)
#endef

def estImpair(n):
    if (n == 1):
        return "Le nombre est impair"
    elif (n == 0):
        return "Le nombre n'est pas impair"
    else:
        return estImpair(n - 2)
#endef

print("20", end=", ")
print(estPair(20))

print("21", end=", ")
print(estImpair(21) , end="\n\n")

#Exercice 2 (Tri séléction)
def plusPetitElement(liste):
    petit = 100
    for i in range(len(liste)):
        if (liste[i] < petit):
            petit = liste[i]
        #endif
    #endfor
    return petit
#enddef

def triSelection(liste):
    listeTriee = []
    for i in range (len(liste)):
        petit = plusPetitElement(liste)
        liste.remove(petit)
        listeTriee.append(petit)
    return listeTriee
#endef

liste = [14,5,7,12,3,4,5]
print("La liste est " + str(liste) + ", dont le plus petit element est " + str(plusPetitElement(liste)))

listeTriee = triSelection(liste)
print("La liste triée, par séléction, est " + str(listeTriee), end="\n\n")

#Bonus (tri à bulle)
def triBulle(liste):
    permutation = True
    passage = 0
    while (permutation == True) :
        permutation = False
        passage += 1
        for i in range (len(liste) - passage):
            if (liste[i] > liste[i+1]):
                permutation = True
                liste[i], liste[i+1] = liste[i+1], liste[i]
            #endif
        #endfor
    #endwhile
    return liste
#enddef

listeB = [14,5,4,12,3,4,2]
print("La liste est " + str(listeB))

listeTrieeB = triBulle(listeB)
print("La liste triée, par bulle, est " + str(listeTrieeB))
