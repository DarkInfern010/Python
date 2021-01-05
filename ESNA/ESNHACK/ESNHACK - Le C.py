#function permet de XOR deux chaîne de caractère
def xor_two_str(a,b):
    xored = []
    for i in range(max(len(a), len(b))):
        xored_value = ord(a[i%len(a)]) ^ ord(b[i%len(b)])
        xored.append(hex(xored_value)[2:])
    return ''.join(xored)

#ENTREE xor CLE = RES
#RES xor ENTREE = CLE
#aw/5P0a:q2*73Av xor      ENTREE     = K9w_!_1[$ZIcV&0
#K9w_!_1[$ZIcV&0 xor aw/5P0a:q2*73Av =      ENTREE

#Récupération de ce que doit être l'entrée pour que le résultat soit correcte
cle = xor_two_str("aw/5P0a:q2*73Av","K9w_!_1[$ZIcV&0")
bytes_object = bytes.fromhex(cle)
print(cle)
print(bytes_object.decode("ASCII"))

#Vérification si l'entrée trouvée est la bonne
test = xor_two_str("aw/5P0a:q2*73Av",bytes_object.decode("ASCII"))
bytes_object2 = bytes.fromhex(test)
print(test)
print(bytes_object2.decode("ASCII"))