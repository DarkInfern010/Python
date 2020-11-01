crypter = "tm bcsv qolfp f'dmvd xuhm exl tgak hlrkiv sydg hxm qiswzzwf qrf oqdueqe dpae resd wndo liva bu vgtokx sjzk hmb rqch fqwbg fmmft seront sntsdr pmsecq"
manip = crypter.upper()                         

for i in range (1,27):
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
