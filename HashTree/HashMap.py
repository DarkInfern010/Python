from HashTree.KeyValue import KeyValue
from HashTree.Node import Node

class HashMap:

    def __init__(self, order):
        self.__root = Node(order, None)
        self.__size = 0
    #endef

    def put(self, key, value):
        res = self.__root.put(KeyValue(key, value), self)
        if (res == None):
            self.__size += 1
        #endif
        return res
    #endef

    def get(self, key):
        return self.__root.get(key)
    #endef

    def remove(self, key):
        res = self.__root.remove(key)
        if (res != None):
            self.__size -= 1
        #endif
        return res
    #endef

    def size(self):
        return self.__size
    #endef

#endclass