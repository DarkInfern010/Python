nombre = []
for i in range (1000 + 1):
    if (i % 7 == 0):
        if (i > 9):
            chiffreDeI = [int(c) for c in str(i)]
            somme = 0
            for j in range (len(chiffreDeI)):
                somme += chiffreDeI[j]
            #endfor
            if (somme == 11):
                nombre.append(i)
            #endif
        #endif
    #endif
#endfor    

print(nombre)
