from HashTree.KeyValue import KeyValue

class Node:

    def __init__(self, order, parent, *keyValues):
        self.__order = order
        self.__parent = parent
        self.__hachedKeys = []
        self.__keyValues = []
        self.__childs = []
        for i in keyValues:
            self.put(i)
    #endef

    def __checkNodeSplit(self, hashMap):
        if (len(self.__hachedKeys) > self.__order):
        #math.ceil
        else:
            pass
        '''
        TODO on détermine le nœud médian, et on crée deux nœud fils gauche et droite
        TODO S’il existe un nœud parent, on fait remonter le nœud médian dans le nœud parent, puis on teste le nœud parent de la même façon:
        parent.checkNodeSplit(HashMap)

        S’il n’y a pas de nœud parent, on en crée un, on change le nœud racine de hashMap avec le nouveau parent, puis on fait remonter
        le nœud médian dans le nœud parent

        TODO Mettre à jour la liste des deux nœuds fils
        '''
        return None
    #enddef

    def put(self, keyValue, hashmap):
        n = self.findNearestNode(keyValue.getKey())
        return n.putKeyValueHere(keyValue, hashmap)
    #endef

    # TODO retourner le noeud le plus proche, correspondant à la clé hachée de keyValue
    def findNearestNode(self, key):
        hachedKey = hash(key)
        if (hachedKey in self.__hachedKeys or len(self.__childs) == 0 or len(self.__hachedKeys) == 0):
            return self
        else:
            for i in range (len(self.__hachedKeys)):
                if (i < len(self.__hachedKeys)):
                    if (self.__hachedKeys[i] < hachedKey and self.__hachedKeys[i+1] > hachedKey):
                        self.__childs[i+1].findNearestNode(key)
                    if (hachedKey < self.__hachedKeys[0]):
                        self.__childs[0].findNearestNode(key)
                    if (hachedKey > self.__hachedKeys[len(self.__hachedKeys)-1]):
                        self.__childs[len(self.__hachedKeys)-1].findNearestNode(key)
                    #endif
                #endif
            #endfor
        #endif
    #enddef

    def putKeyValueHere(self, keyValue, hashmap):

        hachedKey = hash(keyValue.getKey())

        if (hachedKey not in self.__hachedKeys):
            if (len(self.__hachedKeys) > 1):
                for i in range (len(self.__hachedKeys)):
                    if (i < len(self.__hachedKeys)):
                        if (self.__hachedKeys[i] < hachedKey and self.__hachedKeys[i + 1] > hachedKey):
                            self.__hachedKeys.insert(i, hachedKey)
                            self.__keyValues.insert(i, KeyValue(keyValue.getKey(), keyValue.getValue()))
                        if (hachedKey < self.__hachedKeys[0]):
                            self.__hachedKeys.insert(0, hachedKey)
                            self.__keyValues.insert(0, KeyValue(keyValue.getKey(), keyValue.getValue()))
                        if (hachedKey > self.__hachedKeys[len(self.__hachedKeys) - 1]):
                            self.__hachedKeys.append(hachedKey)
                            self.__keyValues.append(KeyValue(keyValue.getKey(), keyValue.getValue()))
                        # endif
                    #endif
                #endfor
            else:
                self.__hachedKeys.append(hachedKey)
                self.__keyValues.append(KeyValue(keyValue.getKey(), keyValue.getValue()))
            #endif
        else:
            for i in range (len(self.__hachedKeys)):
                if (self.__hachedKeys[i] == hachedKey):
                    self.__keyValues.insert(i, KeyValue(keyValue.getKey(), keyValue.getValue()))
        #endif

        self.__checkNodeSplit(hashmap)
        '''
        TODO Si nécéssaire, ajouter la clée hachée correspondant à la clé/valeur dans le tableau hachedKeys
        créer des noeuds fils en conséquence, et mettre à jour le noeud courrant.
        
        TODO ajouter la clé/valeur au tableau keyValues,
        dans le même ordre correspondant au tableau de clés hachées.
        Si la clé existe déjà, remplacer la valeur associée à cette clé
        
        TODO Mettre à jour la liste de nœuds fils
        
        TODO retourner la valeur précédente, associée à la même clée
        S'il n'y avait pas de valeurs associées, retourner null
        '''
        return None
    #endef

    def get(self, key):
        n = self.findNearestNode(key)
        return n.__getHere(key)
    #endef

    def __getHere(self, key):
        hachedKey = hash(key)
        if (hachedKey in self.__hachedKeys):
            for i in range (len(self.__keyValues)):
                if (hash(self.__keyValues[i].getKey()) == hachedKey):
                    return self.__keyValues[i]
                #endif
            #endfor
        #endif
    #endef

    def remove(self, key):
        n = self.findNearestNode(key)
        return n.removeHere(key)
    #endef

    def __removeHere(self, key):
        hachedKey = hash(key)
        '''
        TODO supprimer la clé/valeur qui correspond à la clé donnée.
        
        Si la clé haschée n'est plus associée à aucune paire clé/valeur,
        supprimer la clé hachée et mettre à jour le noeud
        
        Si le noeud ne contient plus aucune donnée,
        supprimer le noeud dans le noeud parent s'il y a un noeud parent.
        
        TODO Mettre à jour la liste de nœuds fils
        
        TODO retourner la valeur précédente, associée à la même clée
        S'il n'y avait pas de valeurs associées, retourner null
        
        '''
        return None
    #endef

#endclass