crypter = "EPCQFBXKWURQCTXOIPMNV"                    
manip = crypter.upper()                         

for i in range (1,26):                          
    decrypter = ""                              
    for car in manip:                        
        if (ord(car) + i > 65 and ord(car) + i < 91) :                 
            decrypter += chr(ord(car) + i)               
        elif (ord(car) + i > 90) :                     
            decrypter += chr(65 + ord(car) + i - 91)                  
        elif (ord(car) + i < 65):                      
            decrypter += " "                    
        #endif
    #endfor
    if (i < 10):                                
        print(i,' =>',decrypter)
    else :                                      
        print(i,'=>',decrypter)
#endfor
print('Décryptage réussi')                      
