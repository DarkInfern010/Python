totalPrixHT = 0
totalPrixTVA = 0
tva = [5,10,20]
partTVA = [0,0,0]
continuer = True

while (continuer):
    prix = int(input("Rentrez un prix : "))
    totalPrixHT += prix

    for i in range (len(tva)):
        print("- " + str(i+1) + " pour la TVA à " + str(tva[i]) + "%")
    #endfor
    choixTva = int(input())

    if (choixTva == 1):
        totalPrixTVA += prix * 1.05
        partTVA[0] += (prix * 5 / (100))
    elif (choixTva == 2):
        totalPrixTVA += prix * 1.10
        partTVA[1] += (prix * 10 / (100))
    else:
        totalPrixTVA += prix * 1.20
        partTVA[2] += (prix * 20 / (100))
    #endif

    choixNext = input("Voulez-vous continuer à saisir des articles? V/F \n")
    if (choixNext == "F" or choixNext == "f"):
        continuer = False
#endwhile

print("Prix Hors Taxe = " + str(totalPrixHT) + "€")
print("Prix Avec Taxe = " + str(totalPrixTVA) + "€")

for i in range (len(partTVA)):
    print("La part de " + str(tva[i]) + "% est de " + str(partTVA[i]) + "€")