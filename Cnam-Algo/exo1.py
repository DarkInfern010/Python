#Factoriel de A,B,C

a = int(input())
b = int(input())
c = int(input())

def facto(x):
    if(x == 0):
        return 1
    else:
        return facto(x-1)*x
    #endif
#endef

print(facto(a))
print(facto(b))
print(facto(c))