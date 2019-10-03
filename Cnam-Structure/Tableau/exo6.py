def palindrome(mot):
    palindrome = True
    i = 0
    while (palindrome == True and i < len(mot)/2):
        if (mot[i] != mot[len(mot)-i-1]):
            palindrome = False
        #endif
        i += 1
    #endfor
    return palindrome
#endef

motUser = input("Rentrer un mot : ")
if (len(motUser) > 0):
    print(palindrome(motUser))
else:
    print("Le mot ne peux pas etre vide")

print("La comlexpité est de O(n)/2")