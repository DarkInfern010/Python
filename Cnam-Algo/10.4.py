def CreateAlpha(debut, indice):
    premier = ord(debut)
    res = []
    for i in range (26):
        if (premier <= 90 - i):
            res.append(chr(premier+i))
        else:
            res.append(chr(premier-26+i))
    print(res)
    return res[indice-1]
#enddef

def Crypt(phrase, key):
    res = ""
    j=0
    for i in range (len(phrase)):
        if (ord(phrase[i]) != 32):
            res += CreateAlpha(key[j],ord(phrase[i])-64)
            if (j == len(key)-1):
                j = 0
            else:
                j += 1
            #endif
        #endif
        else:
            res += " "
    #endfor
    return res
#endef

phrase = input("Saisir une phrase : ")
key = input("Saisir une clé : ")
keyP = [str(c) for c in str(key.upper())]

print(Crypt(phrase.upper(),keyP))