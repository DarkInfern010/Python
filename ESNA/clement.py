string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range (5):
    res = string[i]
    for j in range (1,int(len(string)/5)):
        res += string[i+5*j]
    print(res)
#res = AFKP, BGLQ, CHMR, DINS, EJOT