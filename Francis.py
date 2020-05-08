class Proprio:
    nom = ""
    dateNaissance = "01/04/2020"
    vehicules = []
#endclass

class Vehicule:
    nom = ""
    marque = ""
    possesseur = Proprio()
#endclass

class Voiture(Vehicule):
    volumeCoffre = 0
#endclass

class Moto(Vehicule):
#endclass