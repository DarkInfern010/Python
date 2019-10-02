import random

def Magie(borne_inf, borne_sup):
    magie = random.uniform(borne_inf, borne_sup)
    return magie
#enddef

inf = float(input("Saisir la borne inférieur : "))
sup = float(input("Saisir la borne supérieur : "))

print(Magie(inf,sup))