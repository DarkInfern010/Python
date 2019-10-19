energieTotal = int(input())
nbAste = int(input())

jaune = []
bleu = []

for i in range (nbAste):
    asteroide = [int(x) for x in input().split()]
    if(asteroide[0] == 1):
        jaune.append(asteroide[1])
    else:
        bleu.append(asteroide[1])
    #endif
#endfor

asteroideOk = ""
maxi = 0
for i in range (len(jaune)):
    for j in range (len(bleu)):
        if (jaune[i] + bleu[j] <= energieTotal and jaune[i] + bleu[j] > maxi):
            asteroideOk = str(i) + str(j)
            maxi = jaune[i] + bleu[j]
    #endfor
#endif

if (asteroideOk != ""):
    print(int(jaune[int(asteroideOk[0])])+int(bleu[int(asteroideOk[1])]))
else:
    print(0)