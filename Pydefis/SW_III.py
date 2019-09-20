for i in range (1000, 10000):
	nombre = [int(c) for c in str(i)]
	if (nombre[0] % 2 != 0 and nombre[1] % 2 != 0 and nombre[2] % 2 != 0 and nombre[3] % 2 != 0):
		if (nombre[0] < nombre [1] and nombre[0] < nombre [2] and nombre[0] < nombre [3]):
			if (nombre[1] < nombre [2] and nombre[1] < nombre [3]):
				if (nombre[2] < nombre[3]):
					
					produit = nombre[0] * nombre[1] * nombre[2] * nombre[3]
					somme = nombre[0] + nombre[1] + nombre[2] + nombre[3]

					produitC = [int(c) for c in str(produit)]
					sommeC = [int(c) for c in str(somme)]

					if (produitC[0] % 2 != 0 and produitC[1] % 2 != 0 and produitC[2] % 2 != 0):
						if (sommeC[0] % 2 == 0 and sommeC[1] % 2 == 0):
							print(nombre)
						#endif
					#endif
				#endif
			#endif
		#endif
	#endif
#endfor