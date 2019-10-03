find = False
inf = 0
tab = [2,5,6,10,15,20,30,40,41]
e = 10
if (len(tab) > 0):
    sup = len(tab)
compteur = 0

while (inf <= sup and find == False):
    m=int((inf+sup)/2)
    if (tab[m] == e):
        find = True
    else:
        if(tab[m] < e):
            inf=m+1
        else:
            sup=m-1
        #endif
    #endif
    compteur += 1
#endwhile

print(str(e)+" trouvé en : "+str(compteur)+" itérations")
print("La compléxité est de log2(n) au lieu de O(n) en recherche linéaire")