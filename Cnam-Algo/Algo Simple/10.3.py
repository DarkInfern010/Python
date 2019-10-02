def Crypt(phrase, key, alpha):
    res = ""
    for i in range(len(phrase)) :
        for j in range (len(alpha)):
            if (phrase[i] == alpha[j]):
                res += key[j]
            #endif
        #endfor
    #endfor
    return res
#enddef

key = "HYLUJPVREAKBNDOFSQZCWMGITX"
keyP = [str(c) for c in str(key)]

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphaP = [str(c) for c in str(alpha)]

phrase = input("Saisir une phrase : ")

print(Crypt(phrase.upper(),keyP, alphaP))