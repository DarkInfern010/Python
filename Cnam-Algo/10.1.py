def Crypt(phrase):
    res = ""
    for i in range (len(phrase)):
        if (ord(phrase[i]) != 90):
            res += chr(ord(phrase[i]) + 1)
        else:
            res += chr(ord(phrase[i]) - 25)
    #endfor
    return res
#enddef

phrase = input("Saisir une phrase : ")
print(Crypt(phrase.upper()))