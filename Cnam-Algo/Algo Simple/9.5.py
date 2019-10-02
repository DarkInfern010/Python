def puissRecu(x,y):
    if (y == 0):
        return 1
    else:
        return puissRecu(x , y - 1) * x
#enddef

def puissIte(x,y):
    if (y == 0):
        return 1
    else:
        total = 1
        for i in range(y):
            total *= x
        return total
#enddef

nombre = int(input("Saisir une nombre : "))
puissance = int(input("Saisir une puissance : "))
print("Recusirve : " + str(puissRecu(nombre,puissance)))
print("Iterative : " + str(puissIte(nombre,puissance)))