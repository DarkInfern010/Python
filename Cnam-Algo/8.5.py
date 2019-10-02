demande = input("Saisir une phrase : ")
voyelle = 0
for i in range (len(demande)):
    if (demande[i] == "a" or
            demande[i] == "e" or
            demande[i] == "i" or
            demande[i] == "o" or
            demande[i] == "u" or
            demande[i] == "y"):
        voyelle += 1
#endfor
print(voyelle)