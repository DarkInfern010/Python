nbMinerai = int(input())
prix = input()
argent = int(input())

d = prix.split(" ")
res = []

for i in range (nbMinerai):
    compte = int(d[i])
    mini = [d[i]]

    for j in range (i+1, nbMinerai):
        if (compte+int(d[j]) <= argent):
            compte+=int(d[j])
            mini.append(d[j])
        else:
            break

    if (compte == argent):
        res.append(len(mini))

if (len(res) == 0):
    print("-1")
else:
    print(min(res))