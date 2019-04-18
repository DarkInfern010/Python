(n, m, g) = list(map(int, input().split()))
#n, le nombre de villes
#m, le nombre de lignes de bus joignant les villes
#g, le nombre de lignes de bus à directions de gares routières

villes = [None] * n
for i in range(n):
    villes[i] = int(input())
#endfor

lignes = [None] * m
for j in range(m):
    (departL, arriveeL, tempsL) = list(map(int,input().split()))
    trajetL = {"depart":departL, "arrivee":arriveeL, "temps":tempsL}
    lignes[j] = trajetL
#endfor

gares = [None] * g
for k in range(g):
    (departG, arriveeG, tempsG) = list(map(int,input().split()))
    trajetG = {"depart":departG, "arrivee":arriveeG, "temps":tempsG}
    lignes[j] = trajetG
#endfor

print(villes)
print(lignes)
print(gares)

#Sortie = le score de chaque ville
#Si impossible = -1
#Arrondi à l'entier inférieur