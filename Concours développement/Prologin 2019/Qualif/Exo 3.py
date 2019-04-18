(nombreAmi, sejourH) = list(map(int, input().split()))
DiffPassage = list(map(int, input().split()))
ValeurMax = max(DiffPassage) + 1

PassageAmi = [0] * ValeurMax
for i in range (len(DiffPassage)):
	PassageAmi[int(DiffPassage[i])] += 1
#endfor

compteurTotal = []
tour = ValeurMax-sejourH

for z in range (tour):
	compteur = 0
	if (PassageAmi[z] != 0 or z == tour-1):
		for y in range (z,z+sejourH+1):
			compteur += PassageAmi[y]
		#endfor
		compteurTotal.append(compteur)
	#endif
#endfor

print(max(compteurTotal))
