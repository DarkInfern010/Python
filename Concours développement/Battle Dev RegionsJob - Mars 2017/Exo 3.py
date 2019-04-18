#local_print (variable );
import sys
longueur = int(input())
niveau = input()
trou1 = 0
div = ""
saut = 0

#Si il n'y a pas de trou
if (niveau.count("-") == longueur):
    print("1")
#Sinon on calcul le minimum de saut a faire
else :
    trou1 = niveau.find("_")
    div = niveau.split("-")
    for i in range (0, len(div)) :
        if (len(div[i]) > saut) :
            saut = len(div[i]) + 1
        #endif
    #endfor
#endif

print(saut)

#local_print(longueur)
local_print(niveau)
#local_print(trou1)
local_print(div)
