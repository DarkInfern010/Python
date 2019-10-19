personne = int(input())
barques = int(input())
ferry = int(input())

sauvable = (barques*4) + (ferry*500)

if (personne - sauvable > 0):
    print(personne - sauvable)
else:
    print(0)