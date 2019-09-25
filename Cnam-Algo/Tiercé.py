import math

n = int(input())
p = int(input())

x = math.factorial(n) / math.factorial(n-p)
y = math.factorial(n) / (math.factorial(p) * math.factorial(n-p))

print("Ordre => Une chance sur " + str(x) + " de gagner")
print("Désordre => Une chance sur " + str(y) + " de gagner")