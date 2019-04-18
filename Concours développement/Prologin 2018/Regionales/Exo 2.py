def joli_nom0(n, noms, tailles):
    for i in range (n):
        if (tailles[i] >= 5 and tailles[i] <= 15):
            if (noms[i][0].isupper() == True):
                for y in range (tailles[i]-2):
                    if (ord(noms[i][y]) == ord(noms[i][y + 1])):
                        if (ord(noms[i][y]) != ord(noms[i][y + 2])):
                            break
                        #endif
                        else:
                            print("".join(noms[i]))
                    #endif
                #endfor
            #endif
        #endif
    #endfor
pass

n = int(input())
tailles = [0] * n
noms = [None] * n
for j in range(0, n):
    s = int(input())
    tailles[j] = s
    w = list(input())
    noms[j] = w
joli_nom0(n, noms, tailles)

