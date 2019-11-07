import random

class Tamagoshi:
    age = 0
    maxEnergy = 0
    energy = 0
    name = ""
    lifeTime = 10

    def __init__(self, nom):
        self.__age = 0
        self.__maxEnergy = random.randint(5, 9)
        self.__energy = random.randint(3, 7)
        self.__name = nom
        self.__lifeTime = 10
    #endef

    def parle(self):
        print("Je m'appel " + self.__name, end=" : ")
        if (self.__energy >= 4):
            return True
        else:
            return False
    #endef

    def mange(self):
        if (self.__energy < self.__maxEnergy):
            self.__energy += random.randint(1, 3)
            print("Je suis un TamaGoSushi Heureux")
            return True
        else:
            print("J'ai PAS FAIM !")
            return False
    #endef

    def consommeEnergie(self):
        self.__energy -= 1
        if (self.__energy <= 0):
            print(self.__name+" est mort ce soir !")
            return False
        else:
            return True
    #endef

    def _get_name(self):
        return self.__name
    #endef
    def _set_name(self, v):
        self.__name = v
    #endef
    name = property(_get_name, _set_name)

    def _get_age(self):
        return self.__age
    #endef
    def _set_age(self, v):
        self.__age = v
    #endef
    age = property(_get_age, _set_age)

#endClass