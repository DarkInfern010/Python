tab = [1,3,5,7,9]

for i in range (1,10):
    if (i < 6):
        print(" "*int(tab[len(tab)-i]/2),end="")
        print(str(i)*tab[i-1],end="")
        print(" "*int(tab[len(tab)-i]/2))
    else:
        print(" "*int(tab[i-len(tab)]/2),end="")
        print(str(i)*tab[10-i-1],end="")
        print(" "*int(tab[i-len(tab)]/2))
