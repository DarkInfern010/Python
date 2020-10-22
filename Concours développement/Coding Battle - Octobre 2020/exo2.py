from math import *

nom = input()
voyelle = ['a','e','i','o','u','y']
nbvoyelle = 0
nbconsone = 0
findKER = False
palindrome = True

score = 0

for i in nom:
    if i in voyelle:
        nbvoyelle += 1
    else:
        nbconsone += 1
diff = (nbvoyelle * 2) - nbconsone
score += diff

verifKER = nom.split('ker')
if (len(verifKER) > 1):
    score += 5

for i in range((int(len(nom)/2))-1):
    if (nom[i] != nom[len(nom)-i-1]):
        palindrome = False

if (palindrome and score > 0):
    score = score * 2
print(score)
