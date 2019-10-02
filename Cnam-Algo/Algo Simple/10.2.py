def Crypt(phrase, decalage):
    res = ""
    for i in range(len(phrase)):
        if (ord(phrase[i]) < 90 - decalage):
            res += chr(ord(phrase[i]) + decalage)
        else:
            res += chr(ord(phrase[i]) - 25 + decalage)
    #endfor
    return res
#endef

phrase = input("Saisir une phrase : ")
decalage = int(input("Saisir un décalage : "))
print(Crypt(phrase.upper(),decalage))