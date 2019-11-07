import math


def factorielle(n):
    if (n == 0):
        return 1
    else:
        return factorielle(n - 1) * n


# endef

def equationSecondDegre(a, b, c):
    if (a == 0 and b == 0 and c == 0):
        return ("L'équation a pour solution l'ensemble des réels")

    if (a == 0 and b == 0 and c != 0):
        return ("L'équation n'a pas de solution")

    if (a == 0 and b != 0 and c == 0):
        return ("L'équation a pour solution 0")

    if (a == 0 and b != 0 and c != 0):
        solution = -c / b
        return ("L'équation a pour solution " + str(solution))

    if (a != 0):

        delta = b * b - (4 * a * c)

        if (delta < 0):
            return ("L'équation n'a pas de solution réelle")

        if (delta == 0):
            solution = (b * b) / (2 * a)
            return ("L'équation a pour solution")

        if (delta > 0):
            solution1 = (-b - math.sqrt(delta)) / (2 * a)
            solution2 = (-b + math.sqrt(delta)) / (2 * a)
            return ("L'équation a pour solution " + str(solution1) + " et " + str(solution2))


# endef

a = int(input("Entrer un nombre A : "))
b = int(input("Entrer un nombre B : "))
c = int(input("Entrer un nombre C : "))

# exo 1 partie factorielle
print("Factorielle de A : " + str(factorielle(a)))
print("Factorielle de B : " + str(factorielle(b)))
print("Factorielle de C : " + str(factorielle(c)))

# exo 1 partie équation premier degré
inconnue = -b / a
print("La solution de " + str(a) + "x + " + str(b) + " = 0 vaut " + str(inconnue))

inconnue = -c / b
print("La solution de " + str(b) + "x + " + str(c) + " = 0 vaut " + str(inconnue))

inconnue = -a / c
print("La solution de " + str(c) + "x + " + str(a) + " = 0 vaut " + str(inconnue))

# exo 1 partie équation second degré

print(equationSecondDegre(a, b, c))
print(equationSecondDegre(b, c, a))
print(equationSecondDegre(c, a, b))
