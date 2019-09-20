x = 1694
y = 1546
nb = 50
ValeurX = [0] * nb
ValeurY = [0] * nb

ValeurX[0] = x
ValeurY[0] = y

for i in range (nb):
    if (i < nb-1):
        ValeurX[i+1] = (ValeurX[i] + 2 * ValeurY[i]) % 2018
        ValeurY[i+1] = (-3 * ValeurX[i] + ValeurY[i]) % 2018
    #endif
#endfor

declinaison = (ValeurX[-1] - 900) / 10
asce_droite = (ValeurY[-1] / 150) * 2

print(str(declinaison) + " , " + str(asce_droite))