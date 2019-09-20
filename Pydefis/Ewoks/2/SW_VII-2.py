compteur = 0
with open("ewoks2", "r") as file:
	for line in file.readlines():
		nom = line.strip()
		compteurV = 0
		compteurC = 0
		for i in range (len(nom)):
			if (nom[i] == "a" or nom[i] == "A" or nom[i] == "e" or nom[i] == "E" or nom[i] == "i" or nom[i] == "I" or nom[i] == "o" or nom[i] == "O" or nom[i] == "u" or nom[i] == "U" or nom[i] == "y" or nom[i] == "Y"):
				compteurV += 1
			else:
				compteurC +=1
			#endif
		#endfor
		if (compteurV * 2 == compteurC):
			compteur += 1
		#endif
	#endfor
#endwith
print(compteur)