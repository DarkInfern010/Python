PxJoseph = int(input()) #Prix du billet de Joseph
nombreBillet = int(input()) #Nombre de billet trouvé par Haruhi
PxHaruhi = list(map(int, input().split())) #Liste des Prix trouvé par Haruhi

arnaque = 0 #Init du compteur d'arnaque
for i in range (nombreBillet): #Vérification de chaque billets de Haruhi
    if (int(PxHaruhi[i]) < PxJoseph): #Compteur Arnaque
        arnaque += 1 #Compteur Arnaque
    #endif
#endfor

if (arnaque >= 3): print("ARNAQUE !") #Résultat
else: print("Ok bon voyage, bisous, n'oublie pas de m'envoyer des photos !") #Résultat
