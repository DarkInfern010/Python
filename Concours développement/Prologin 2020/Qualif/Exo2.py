longeur = int(input())
chaine = input()
res = ""
tmp = ""
i = 0

d = chaine.split('*')
for i in range(len(d)):
    if (i % 2 == 0):
        tmp += d[i]
    #endif
#endfor

for j in range(len(tmp)):
    if (tmp[j] == "."):
        j += 1
    else:
        res += tmp[j]
        j += 1
#endwhile

print(res)