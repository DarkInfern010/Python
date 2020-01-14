fin = 1325
res = 0
for i in range (fin):
    if (i % 3 == 0 or i % 5 == 0):
        res += i
    #endif
#endfor
print(res)