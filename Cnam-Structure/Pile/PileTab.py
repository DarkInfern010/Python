import random

def EstVide(tab):
    if (len(tab) == 0):
        return True
    else:
        return False
#enddef

#Complexité de O(n)
def Empiler(tab, v):
    newTab = [None] * int(len(tab)+1)
    for i in range (len(tab)):
        newTab[i] = tab[i]
    #endfor
    newTab[-1] = v
    return newTab

#enddef

#Complexité de O(n)
def Depiler(tab):
    newTab = [None] * int(len(tab)-1)
    for i in range (len(newTab)):
        newTab[i] = tab[i]
    #endfor
    return newTab
#enddef

def Afficher(tab):
    print(tab)
#enddef

#Complexité O(n²)
def GardePair(tab):
    compteur = 0
    for i in range (len(tab)):
        if (tab[i] % 2 == 0):
            compteur += 1
        #endif
    #enfor
    newTab = [None] * compteur
    dernierPairIndice = 0

    for j in range (len(newTab)):
        for k in range (dernierPairIndice,len(tab)):
            if (tab[k] % 2 == 0):
                newTab[j] = tab[k]
                dernierPairIndice = k+1
                break
            #endif
        #endfor
    #enfor

    return newTab
#endef

#Complexite O(n)
def Random():
    tab = [None] * 20
    for i in range (20):
        tab[i] = random.randrange(0,100)
    return tab
#enddef

tab = Random()

tab = Empiler(tab, 5)
print(Afficher(tab))

tab = Depiler(tab)
print(Afficher(tab))

tab = GardePair(tab)
print(Afficher(tab))