import codecs

test = '\x1c\x1f'
test = list(test)

test = ' '.join(format(ord(x), 'b') for x in test)
test = test.split(" ")

for j in range (len(test)):
    t1 = bin(int(test[j], 2) ^ int(bin(ord('e')),2))
    t2 = hex(int(t1, 2))
    t3 = codecs.decode(t2[2:], "hex").decode('utf-8')
    test[j] = t3
#endfor
print(test)

#'abc' XOR cle = '\x04\x01\x14'
#'\x04\x01\x14' XOR 'abc' = cle

#'a' XOR 'e' = '\x04'
#'\x04' XOR 'a' = 'e'

#'v' XOR 'e' = '\x13'
#'\x13' XOR 'v' = 'e'

entree = list("abcdef")
res = list("\x04\x01\x14!&1")

for i in range (len(entree)):
    entree[i] = int(bin(ord(entree[i])), 2)
    res[i] = int(bin(ord(res[i])), 2)

soluce = ""
for i in range (len(entree)):
    t1 = bin(entree[i] ^ res[i])
    t2 = hex(int(t1,2))
    t3 = bytes.fromhex(t2[2:]).decode("ASCII")
    soluce += t3

print(soluce)

#ENTREE + CLE = RES
#RES + ENTREE = CLE
