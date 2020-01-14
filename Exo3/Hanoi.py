from Exo3.Tower import *
from Exo3.Disk import *

class Hanoi:
    tourA = None
    tourB = None
    tourC = None
    nbDisk = 0

    def __init__(self, nbDisk):
        if (nbDisk < 2):
            print(ValueError)
        else:
            self.nbDisk = nbDisk
            self.tourA = Tower()
            self.tourB = Tower()
            self.tourC = Tower()

            for i in range (1,nbDisk+1):
                self.tourA.push(Disk(nbDisk+1-i))
            #endfor
        #endif
    #endef

    def _get_max_tower_size(self):
        tab = [self.tourA.height,self.tourB.height,self.tourC.height]
        return max(tab)
    #enddef

    def resolve(self):
        self.__hanoi(self.tourA.height, self.tourA, self.tourB, self.tourC)
    #endef

    def __hanoi(self, n:int, TourA:Tower, TourB:Tower, TourC:Tower):
        if (n == 1):
            TourC.push(TourA.pop())
        else:
            self.__hanoi(n-1,TourA,TourB,TourC)
            TourC.push(TourA.pop())
            self.__hanoi(n-1, TourB, TourA, TourC)
        #enddef
    #endef

    def __str__(self) -> str:
        res = ""
        for i in range (self.nbDisk):
            res += self.tourA.get_str_line(i)
            res += self.tourB.get_str_line(i)
            res += self.tourC.get_str_line(i)
            res += "\n"
        #enddef
        return res
    #endef

#endclass