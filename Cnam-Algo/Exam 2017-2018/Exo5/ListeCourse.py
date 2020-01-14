class ListeCourse:
    articles = []

    def __init__(self, article):
        self.articles = article
    #endef

    def obtenirTotal(self):
        res = 0
        for i in range (len(self.articles)):
            res += self.articles[i].prixHT
        #endfor
        return res
    #endef

#endclass