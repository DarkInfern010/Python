from turtle import *
from math import *
from random import *

def Init(): #Génération des carre de base et du carre cible
    #General
    speed(0)
    color('red')
    forward(300)
    right(90)
    forward(300)
    right(90)
    forward(300)
    right(90)
    forward(300)
    
    #Cible
    color('green')
    up()
    right(90)
    forward(100)
    right(90)
    forward(10)
    down()
    forward(280)
    left(90)
    forward(100)
    left(90)
    forward(280)
    left(90)
    forward(100)
    up()
#enddef
    
def Projectile (nbRep): #Génération des projectile n fois
    compteurCible = 0
    
    for i in range (0,nbRep): #Boucle pour chaque projectile
        
        x = randint(0,300)  #Aléatoire de la coordonnée x pour chaque projectile
        y = randint(-300,0) #Aléatoire de la coordonnée y pour chaque projectile
        
        if(x >= 100 and x <= 200 and y >= -290 and y <= -10): #Vérification si le projectile est dans le carré cible
            compteurCible += 1
        #endif
            
        goto(x,y)
        down()
        circle(1)
        up()
        
    #endfor
    Calcul(compteurCible,nbRep) #Envoie a la fonction calcul le nombre de projectile atteignant la cible
#enddef

def Calcul (nbCible,nbTotal): #Calcul des différent valeurs
    print(str(nbCible)+" projectiles ayant atteint la cible")
    print(str(nbTotal)+" étant le nombre de projectile lancé")
    
    proba = nbCible / nbTotal
    print(str(proba)+" est la probabilité de projectile atteignant la cible")
    
    aire = 300**2 #Surface du carré total
    estimation = (aire*nbCible)/nbTotal #Méthode Monte-Carlo pour estimation de la surface du carre cible
    print(str(estimation)+ " estimation de la surface du lac")
#enddef

#PROGRAMME
Init()
Projectile(1000)
