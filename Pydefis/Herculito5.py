salle = 49
compteurEau = 2
bleue = 2
rouge = 0
vert = 0
compteurSalle = 0

while (compteurSalle < salle-1):
    rouge = bleue * 7
    compteurEau += rouge
    compteurSalle += 1

    vert = bleue * 5
    compteurEau += vert
    compteurSalle += 1

    bleue = rouge + vert
    temp = str(bleue)
    if (bleue > 100):
        bleue = int(temp[-2:])
    compteurEau += bleue
    compteurSalle += 1
#endwhile

print(compteurEau)