class Article:
    nom = ""
    prixHT = 0
    TVA = 0
    prixTTC = 0

    def __init__(self, nom, prixHT, TVA, prixTTC):
        self.__nom = nom
        self.__prixHT = prixHT
        self.__TVA = TVA
        self.__prixTTC = prixTTC
    #endef

    def _get_nom(self):
        return self.__nom
    #endef
    def _set_nom(self, v):
        self.__nom = v
    #enddef
    nom = property(_get_nom, _set_nom)

    def _get_prixHT(self):
        return self.__prixHT
    # endef
    def _set_prixHT(self, v):
        self.__prixHT = v
    # endef
    prixHT = property(_get_prixHT, _set_prixHT)


    def _get_prixTTC(self):
        return self.__prixTTC
    #endef
    def _set_prixTTC(self, v):
        self.__prixTTC = v
    # endef
    prixTTC = property(_get_prixTTC, _set_prixTTC)

    def _get_TVA(self):
        return self.__TVA
    #endef
    def _set_TVA(self, v):
        self.__TVA = v
    # endef
    TVA = property(_get_TVA, _set_TVA)
#endClass