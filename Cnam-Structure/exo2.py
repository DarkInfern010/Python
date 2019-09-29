find = False
inf = 1
tab = [1,2,3,4,5,7,8,9,10]
tab1 = []
e = 6
sup = len(tab)
compteur = 0

while (inf <= sup and find == False):
    m=int((inf+sup)/2)
    if (tab[m] < e and tab[m+1] > e):
        find = True
        print(str(m) + " " + str(m + 1))
        for i in range (len(tab)):
            if (i < m+1):
                tab1.append(tab[i])
            elif (i == m+1):
                tab1.append(e)
                tab1.append(tab[i])
            else:
                tab1.append(tab[i])
    else:
        if(tab[m] < e):
            inf=m+1
        else:
            sup=m-1
        #endif
    #endif
    compteur += 1
#endwhile

print(tab)
print(tab1)