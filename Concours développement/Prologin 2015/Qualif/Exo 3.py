rondPointX, rondPointY = input().split()
nbSortie = int(input())
persoX, persoY = input().split()

maxX = persoX
miniY = persoY
for i in range (nbSortie-1):
    sortieX, sortieY = input().split()
    if (sortieX >= maxX):
        maxX = sortieX
        if (sortieY <= miniY):
            miniY = sortieY
        miniY = sortieY
#endfor

print(str(maxX) + " " + str(miniY))
