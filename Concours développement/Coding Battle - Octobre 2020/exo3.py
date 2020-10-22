nbRang = int(input())
placeDispo = []
nombrePlace = 0
for i in range(nbRang):
    nbplace = int(input())
    nombrePlace += nbplace
    placeDispo.append(nbplace)
print(placeDispo)

nbPersonne = int(input())
tabAudition = dict()
for j in range(nbPersonne):
    audition = int(input())
    if (audition in tabAudition):
        tabAudition[audition] += 1
    else:
        tabAudition[audition] = 1
print(tabAudition)

possible = True

if (nbPersonne < nombrePlace):
    for i in range (len(placeDispo)):
        if (placeDispo[i] > tabAudition.get(i+1)):
            print(placeDispo[i])
            print(tabAudition.get(i + 1))
            possible = False
else:
    possible = False

if (possible):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
