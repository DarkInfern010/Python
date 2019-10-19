from math import *

heureLocal = input()
m = int(input())
h = int(input())
div = heureLocal.split(":")

nbMinuteET = (int(div[0])*h)+int(div[1])
nbMinuteTE = floor(int(nbMinuteET) / m)

heureT = floor((nbMinuteTE / 60) % 24)
minT = floor(nbMinuteTE - (floor(nbMinuteTE / 60)*60))

finale = str(heureT)+":"+str(minT)
print(finale)