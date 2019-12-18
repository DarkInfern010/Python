class KeyValue:
    __key = None
    __value = None

    def __init__(self, key, value):
        self.__key=key
        self.__value=value
    #endef

    def getValue(self):
        return self.__value
    #endef

    def setValue(self, value):
        self.__value = value
    #endef

    def getKey(self):
        return self.__key
    #endef

#endclass