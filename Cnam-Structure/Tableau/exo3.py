find = False
inf = 0
tab = [1,2,3,4,5,6,7,8,9,10]
e = 8
if (len(tab) > 0):
    sup = len(tab)
compteur = 0
print(tab)
while (inf <= sup and find == False):
    m=int((inf+sup)/2)
    if (tab[m] == e):
        find = True
        tab.remove(tab[e-1])
    else:
        if(tab[m] < e):
            inf=m+1
        else:
            sup=m-1
        #endif
    #endif
    compteur += 1
#endwhile

print("Suppresion de " + str(e))
print(tab)

print("La compléxité est de log2(n)")