from TamaGoSushi.Tamagoshi import *

class GrosMangeur (Tamagoshi):
    def consommeEnergie(self):
        self.__energy -= 2
        if (self.__energy <= 0):
            print(self.__name+" est mort ce soir !")
            return False
        else:
            return True
    #endef
#endclass