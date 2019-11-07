import random

def PlusLongueCoupeIte(tab):
    res = []
    indice = []
    i = 0
    while (i < len(tab)):
        total = 0
        if (tab[i] == 1):
            for j in range (i,len(tab)):
                if (tab[j] == 0):
                    break
                else:
                    total += 1
                #endif
            #endfor
            res.append(total)
            indice.append(str(i) + " : " + str(i + total - 1))
            i += total
        else:
            i += 1
    #endfor
    indiceMaxRes = res.index(max(res))
    print("Le nombre de 1 max dans une coupe est " + str(max(res)))
    return indice[indiceMaxRes]
#enddef

def PlusLongueCoupeRec(tab, nbO):
    pivot = round(len(tab)/2)
    foundi = False
    foundj = False
    i = 0
    j = 0
    indiceDeb = 0
    indiceFin = 0

    while(foundi == False and foundj == False):
        i += 1
        j += 1

        if(tab[pivot - i] == 1):
            indiceDeb = len(tab) - pivot - i
        else:
            foundi = True

        if (tab[pivot + j] == 1):
            indiceFin = len(tab) - pivot + j
        else:
            foundj = True
        #endif
    #endwhile
    nbO.append(indiceFin-indiceDeb)

    if (len(tab[:indiceDeb]) > 2):
        PlusLongueCoupeRec(tab[:indiceDeb],nbO)
    if (len(tab[indiceFin+1:]) > 2):
        PlusLongueCoupeRec(tab[indiceFin+1:],nbO)
    if (len(tab[indiceFin+1:]) == 1 or len(tab[:indiceDeb]) == 1):
        nbO.append(1)
    return max(nbO)
#endef

n = int(input("Entrer la taille du tableau : "))
tab = [random.randint(0,1) for i in range(n)]
nbO = []

print(tab)

#print (PlusLongueCoupeIte(tab))
print (PlusLongueCoupeRec(tab,nbO))
