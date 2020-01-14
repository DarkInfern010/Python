from Exo5.ListeCourse import *

class Facture(ListeCourse):

    def obtenirTotal(self):
        res = 0
        for i in range (len(self.articles)):
            res += self.articles[i].prixTTC
        #endfor
        return res
    #endef


#endclass