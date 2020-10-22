nbbillet = int(input())
centPremBillet = int(input())
centSuivantBillet = int(input())
derBillet = int(input())

Somme = 0

for i in range (1, nbbillet+1):
    if (i <= 100):
        Somme += centPremBillet
    elif (i > 100 and i <= 200):
        Somme += centSuivantBillet
    else:
        Somme += derBillet

print(Somme)