import requests, pgrep, os, time

nombreRequete = 0

while nombreRequete < 1000: #Boucle faisant le nombre de requete
    openvpnProcessus = pgrep.pgrep("openvpn") #Permet de savoir si il y a un processus openvpn qui tourne

    if (len(openvpnProcessus) == 0): #Verification si il n'y a aucun processus openvpn ouvert
        os.system('nohup openpyn uk &') #Lancement de script VPN sans affichage et caché
        time.sleep(10) #Attente de 10sec pour que le VPN s'active
        nombreRequete += 1 #Incrémentation de la variable du nombre de requete
        print(nombreRequete) #Affichage du nombre de boucle

    else:
        url = "https://www.cnam-grandest.fr/le-cnamathon/431" #URL de l'article

        s = requests.sessions() #Ouverture d'une session
        response = s.get(url) #Récupération du code HTML de la page (GET)
        div = response.text.split('ittoken " value="1" name="') #Localisation du token
        div1 = div[1].split('"') #Split du token
        token = div1[0] #Récupération du token seul

        #Objet a envoyer dans la requete pour le vote
        params = {
            "user_rating":5, #Montant du vote 1-5
            "task":"article.vote", #Tache effectuer par la requete
            "hitcount":0, #PFFFF
            "submit_vote":"val", #PFFFF
            "url":url+"?hitcount=0", #Renvoie de l'URL
            token:1 #Passage du token
        }

        response2 = s.post(url+"?hitcount=0", data=params) #Envoie de la requete avec URL et params (POST)
        print(token) #Affichage du token pour voir si different
        os.system('sudo kill ' + str(openvpnProcessus[0])) #Kill du VPN
        time.sleep(3) #Attente de 3sec pour pas planter le VPN
        nombreRequete += 1  # Incrémentation de la variable du nombre de requete
        print(nombreRequete)  # Affichage du nombre de boucle
    #endif
#endwhile