class Disk:
    max_size = 9

    def __init__(self, tailleparam):
        if (tailleparam <= 0 or tailleparam > self.max_size):
            print(ValueError)
        else:
            self.__size = (tailleparam*2)-(1)
    #endef

    def _get_size(self) -> int:
        return self.__size
    #endef
    size = property(_get_size)

    def __str__(self) -> str:
        return "-"*self.size
    #endef

#endclass