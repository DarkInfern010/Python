import random

def isFirst(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    #endif
    i = 5
    d = 2
    while i * i <= n:
        if n % i == 0:
            return False
        #endIf
        i += d
        d = 6 - d
    return True
#enddef

def getfirstNumber (numEnd, numStart=0):
    tableau = []
    for i in range (numStart, numEnd):
        if (isFirst(i)):
            tableau.append(i)
        #endif
    #endfor
    return tableau
#endef

#Calcul nombre Premier
nombrePremier = getfirstNumber(100)

#Etape 1 (p & q)
p = random.choice(nombrePremier)
nombrePremier.remove(p)
q = random.choice(nombrePremier)

#Etape 2 (n)
n = p * q

#Etape 3 (phi)
phi = (p - 1) * (q - 1)

#Etape 4 (e)
un entier naturel e premier avec phi