numeroSerie = "449149"
u = numeroSerie[0:3]
n = numeroSerie[3:6]

for i in range (int(n)):
    u = int(u) * 13
    u = str(u)[-3:]
#endfor

print(u)