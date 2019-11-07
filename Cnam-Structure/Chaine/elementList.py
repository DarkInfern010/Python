class ElementListe:
    def __init__(self, value, *suivant):
        self.valeur = value
        if (suivant):
            self.suivant = suivant
        else:
            self.suivant = None
    #enddef

    def _get_valeur(self):
        return self.valeur
    #enddef

    def _set_valeur(self,v):
        self.valeur

#endclass