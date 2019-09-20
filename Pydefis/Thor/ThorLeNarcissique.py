compteur = 0
nbMots = 336532
with open("mots", "r") as file:
	for line in file.readlines():
		nom = line.strip()
		verificationT = 0
		verificationH = 0
		verificationO = 0
		verificationR = 0
		for i in range (len(nom)):
			if (nom[i] == "t"):
				verificationT = verificationT + 1
			#endif
			elif (nom[i] == "h"):
				verificationH = verificationH + 1
			#endif
			elif (nom[i] == "o"):
				verificationO = verificationO + 1
			#endif
			elif (nom[i] == "r"):
				verificationR = verificationR + 1
			#endif
		#endfor
		if (verificationT == 1 and verificationH == 1 and verificationO == 1 and verificationR == 1):
			compteur = compteur + 1 
		#endif
	#endfor
#endith
print(compteur)