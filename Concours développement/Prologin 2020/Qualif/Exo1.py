nbPerso = int(input())
poids = list(map(int, input().split()))
fuel = 0
for i in range (len(poids)):
    if (poids[i] > 90):
        fuel += 20
    fuel += 60
print(fuel)