compteur = 0
compteurE = 500
with open("ewoks", "r") as file:
	for line in file.readlines():
		nom = line.strip()
		for i in range (len(nom)):
			if (nom[i] == "a" or nom[i] == "A"):
				compteur = compteur + 1
				break
			#endif
		#endfor
	#endfor
#endwith
vraiCompteur = compteurE - compteur
print(vraiCompteur)