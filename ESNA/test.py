test = '\x04\x17\x1f$-6\x16\n\x16+*$\x11'
print(type(test))
test = list(test)
print(test)
print(len(test))
for i in range (len(test)):
    test[i] = bin(ord(test[i]))
#endfor
print(test)

for j in range (len(test)):
    t1 = bin(int(test[j], 2) ^ int(bin(ord('e')),2))
    t2 = hex(int(t1,2))
    t3 = bytes.fromhex(t2[2:]).decode("ASCII")
    test[j] = t3
#endofr
print(len(test))
print(test)

# - + e = H
# '\x48' + '\x2D' = '\x65'

#a + CLE = '\x04'
#'\x04' + a = cle

#ENTREE + CLE = RES
#RES + ENTREE = CLE
