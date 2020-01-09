nb = int(input())

mini = 1000
res = ""

for i in range (nb):
    perso = input().split(" ")
    nom = perso[0]
    taille = perso[1]

    if (taille < mini):
        mini = taille
        res = nom

print(res)
