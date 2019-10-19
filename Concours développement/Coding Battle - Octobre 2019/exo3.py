bombe = [float(x) for x in input().split()]
bombeX = bombe[0]
bombeY = bombe[1]

infoSuspect = [int(x) for x in input().split()]
nbSuspect = infoSuspect[0]
nbPos = infoSuspect[1]

suspect = []

for i in range (nbSuspect):
    perso = input()
    posx = []
    posy = []

    for j in range (nbPos):

        posSuspect = [float(x) for x in input().split()]
        print(posSuspect)
        posx.append(posSuspect[0])
        posy.append(posSuspect[1])

        if (j > 0):
            if (posx[j-1] <= bombeX and posx[j] >= bombeX):
                if (posy[j-1] >= bombeY and posy[j] <= bombeY):
                    suspect.append(perso)
                #endif
            #endif
            if (posx[j-1] >= bombeX and posx[j] <= bombeX):
                if (posy[j-1] <= bombeY and posy[j] >=bombeY):
                    suspect.append(perso)
                #endif
            #endif
        #endif
    #endfor
#endfor

print(suspect)