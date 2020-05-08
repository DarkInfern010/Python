from Exo3.Disk import *

class Tower:

    def __init__(self):
        self.__ListDisk = []
    #enddef

    def push(self, disk: Disk):
        if (disk == None):
            return (TypeError)
        elif (len(self.__ListDisk) != 0):
            if (disk.size >= self.__ListDisk[-1].size):
                return (ValueError)
        else:
            self.__ListDisk.append(disk)
    #endef

    def pop(self):
        if (len(self.__ListDisk) == 0):
            return (ValueError)
        else:
            temp = self.__ListDisk[-1]
            self.__ListDisk.pop()
            return temp
    #endef

    def _get_height(self):
        return len(self.__ListDisk)
    #endef
    height = property(_get_height)

    def get_str_line(self, indice:int) -> str:
        if (indice >= len(self.__ListDisk)):
            return ("    |    ")
        else:
            return (self.__ListDisk[indice].__str__())
    #enddef

#endclass