from TamaGoSushi.Tamagoshi import *

class TamaGame:
    invasionTama = []
    lifeTama = []
    mortTama = []

    CycleMax = 0
    CycleScore = 0
    nbCycle = 0

    def __init__(self):
        nb = int(input("Saisir le nombre de TamaGoSushi : "))
        for i in range (nb):
            nom = input("Saisir le nom du TamaGoSushi : ")
            self.invasionTama.append(Tamagoshi(nom))
        #endfor
        self.nbCycle = int(input("Saisir le nombre de cycle : "))
        self.lifeTama = self.invasionTama
        self.CycleMax = self.nbCycle * nb
        self.play()
    #enddef
    def play(self):
        i = 0
        while i < self.nbCycle:
            print("------------Cycle N°"+str(i+1)+"------------")
            for j in range (len(self.lifeTama)):
                if (self.lifeTama[j].parle()):
                    print("tout va bien ! ")
                else:
                    print("je suis affamé ! ")
            #endfor

            print("Selectionner le TamaGoSushi a faire manger : ")
            for k in range (len(self.lifeTama)):
                print("("+str(k)+")" + self.lifeTama[k].name, end=" ")
            #endfor
            faireManger = int(input())
            print(self.lifeTama[faireManger].name, end=" ")
            self.lifeTama[faireManger].mange()

            for l in self.lifeTama:
                l.age = l.age + 1
                if (l.consommeEnergie() == False):
                    self.lifeTama.remove(l)
                #endif
            #endfor

            self.CycleScore += len(self.lifeTama)
            i += 1
        #endwhile
        print("------------BILAN------------")
        print("Vous avez un score de "+str(self.score())+" %")
        self.resultat()
    #endef

    def score(self):
        return (self.CycleScore / self.CycleMax) * 100
    #endef

    def resultat(self):
        for i in range (len(self.invasionTama)):
            if (self.invasionTama[i] in self.lifeTama):
                print(self.invasionTama[i].name + " vie encore, Bravo !")

        print("------------Fin du jeu------------")
    #endef

#endclass

t = TamaGame()