monnaieUser = float(input()) * 100
montantItem = float(input()) * 100
rendu = monnaieUser - montantItem

renduTab = []
euros = [50000,20000,10000,5000,2000,1000,500,200,100,50,20,10,5,2,1]

for i in range (len(euros)):
    if (euros[i] <= rendu):
        while (rendu >= euros[i]):
            rendu -= euros[i]
            renduTab.append(euros[i]/100)
        #endwhile
    #endif
#endfor

print(renduTab)