GeneraleVille = input()
div = GeneraleVille.split()
NombreVille = int(div[0])
NombreBusJoinVille = int(div[1])
NombreBusGoGare = int(div[2])

TempsAttenteParVille = [0] * NombreVille

for i in range (NombreVille):
    TempsAttenteParVille[i] = int(input())
#endfor

MatriceAdjacente = [[0 for col in range (NombreVille)] for lig in range (NombreVille)]
MatriceTemps = [[0 for col in range (NombreVille)] for lig in range (NombreVille)]

for y in range (NombreBusJoinVille):
    TempsBusJoinVille = input()
    div1 = TempsBusJoinVille.split()
    Origine = int(div1[0])
    Cible = int(div1[1])
    TempsOrigineCible = int(div1[2])
    
    MatriceAdjacente[Origine-1][Cible-1] = 1
    MatriceTemps[Origine-1][Cible-1] = TempsOrigineCible
#endfor

#for z in range (NombreBusGoGare):
    #TempsBusGoGare = input()
#endfor
