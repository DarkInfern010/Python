#0x3+1x1
#0 = Blanc
#1 = Noir

chaine1 = str(input("Première ligne : "))
chaine2 = str(input("Deuxième ligne : "))
chaine3 = str(input("Troisième ligne : "))
chaine4 = str(input("Quatrième ligne : "))
chaine5 = str(input("Cinquième ligne : "))
chaine6 = str(input("Sixième ligne : "))
chaine7 = str(input("Septième ligne : "))
chaine8 = str(input("Huitième ligne : "))
chaine9 = str(input("Neuvième ligne : "))
chaine10 = str(input("Dizième ligne : "))
chaine11 = str(input("Onzième ligne : "))
chaine12 = str(input("Douzièeme ligne : "))
chaine13 = str(input("Treizième ligne : "))
chaine14 = str(input("Quatorzième ligne : "))

chaineTotal = chaine1 + ',' + chaine2 + ',' + chaine3 + ',' + chaine4 + ',' + chaine5 + ',' + chaine6 + ',' + chaine7 + ',' + chaine8 + ',' + chaine9 + ',' + chaine10 + ',' + chaine11 + ',' + chaine12  + ',' + chaine13 + ',' + chaine14
for i in range (0, len(chaineTotal.split(","))):
    resultat = " "
    pixel = chaineTotal.split(",")[i].split("+");
    for i in range (0,len(chaineTotal.split(",")[i].split("+"))):
        if (pixel[i].split("x")[0] == '0') :
            for i in range (0,int(pixel[i].split("x")[1])):
                resultat += '□'
            #endfor
        else :
            for i in range (0, int(pixel[i].split("x")[1])):
                resultat += '■'
            #endfor
        #endif
    #endfor
    print(resultat)
#endfor
