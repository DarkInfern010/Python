import requests
from datetime import datetime
import urllib.request
import re

def RecupElementDuJour(jour):

    requete = requests.post("http://www.krosmoz.com/fr/almanax/"+jour)
    page = requete.text

    Offrande = page.split('<div class="mid">')[1].split('<div class="clear">')[0]

    print(Offrande)
    Image = Offrande.split('<img src="')[1].split('"/>')[0].strip()
    Bonus = Offrande.split('<div class="more">')[1].split('.')[0].strip()
    Objet = Offrande.split('Récupérer ')[1].split(' et rapporter')[0].strip()
    Nombre = ""
    Nom = ""
    for i in Objet:
        if i.isalpha() or i == " ":
            Nom += i
        if i.isdigit():
            Nombre += i
    #endfor

    return Image, Bonus, Nombre, Nom.strip()

#endDef

jour = datetime.today().strftime('%Y-%m-%d')

AlmaImage, AlmaBonus, AlmaNombre, AlmaNom = RecupElementDuJour(jour)

urllib.request.urlretrieve(AlmaImage, "imageObjet.jpg")
fichier = open("titreObjet.txt", "w")
fichier.flush()
fichier.write(AlmaBonus)
fichier.write('\n')
fichier.write(AlmaNombre)
fichier.write('\n')
fichier.write(AlmaNom)
fichier.close()