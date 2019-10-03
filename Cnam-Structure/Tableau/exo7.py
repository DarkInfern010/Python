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

n = int(input("Entrer la taille du tableau : "))
tab = [random.randint(0,1) for i in range(n)]
print(tab)

print (PlusLongueCoupeIte(tab))