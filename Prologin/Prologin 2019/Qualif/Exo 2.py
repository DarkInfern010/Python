N = int(input()) #Nombre de Pays Visiter
Liste_p = [None] * N
for i in range (N):
    (id, decalage) = list(map(int, input().split()))
    Lieux_i = {"id": id, "decalage": decalage}
    Liste_p[i] = Lieux_i
#endfor

V = int(input()) #Nombre de Voyage
Liste_d = [None] * V
for j in range (V):
    (voyageur, destination) = list(map(int, input().split()))
    Etape_i = {"voyageur":voyageur, "destination":destination}
    Liste_d[j] = Etape_i
#endfor

Haruhi = 0
Joseph = 0
for h in range (V):
    if(Liste_d[h]['voyageur'] == 1):
        Haruhi = Liste_p[Liste_d[h]['destination']-1]['decalage']
    else:
        Joseph = Liste_p[Liste_d[h]['destination']-1]['decalage']
    #endif
    Horaire = Joseph - Haruhi
    print(abs(Horaire))
#endfor

