def factoRecu (x):
    if (x == 0):
        return 1
    else:
        return factoRecu(x - 1) * x
    #endif
#enddef

def factoIte (x):
    total = 1
    if (x == 0):
        return 1
    else:
        for i in range (1,x+1):
            total *= i
        #endfor
        return total
#enddef

demande = int(input("Saisir une nombre : "))
print("Recusirve : " + str(factoRecu(demande)))
print("Iterative : " + str(factoIte(demande)))