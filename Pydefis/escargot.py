x = 1330
y = 300
final = 8500
position = 0
compteur = 0
anciennepos = 0

while compteur < 10:
    position += x
    print("Fin du jour : "+str(compteur)+" altitude = "+str(position)+"cm")
    position -= y

    if (compteur == 5):
        anciennepos = position
    #endif
    if (compteur % 8 == 0 and compteur != 0):
        position = anciennepos
    #endif
    print("Fin la nuit : " + str(compteur) + " altitude = " + str(position) + "cm\n")

    x -= 1
    compteur += 1
#endwhile

print(compteur)

