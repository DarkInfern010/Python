import sys

planche = []
for i in range(4):
    planche.append(int(input()))

mini = min(planche)

res = 0
for i in range(4):
    res += planche[i] - mini

print(res)