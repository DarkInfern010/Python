age = int(input())
tempsPermis = int(input())
nbAccident = int(input())
nbClients = int(input())

tarif = ["rouge","orange","vert","bleu"]
client = 0

if (nbAccident >= 2):
    client = "REFUSE"
elif (nbAccident == 0):
    if (age >= 25):
        if (tempsPermis >= 2):
            client = 2
        else:
            client = 1
        #endif*
    else:
        client = 0
elif (nbAccident == 1):
    if (age < 25):
        client = 0
    else:
        client = 1
else:
    client = 0

if (nbClients >= 5):
    client += 1;

print(tarif.pop(client))