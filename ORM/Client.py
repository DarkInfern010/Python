from ORM.Record import *
from ORM.Database import *
from ORM.SQLField import *

class Client(Record):
    def __init__(self):
        super(self, "CLIENT")
        self._connect_field("numero", SQLField(0, "numero", int, True))
        self._connect_field("nom", SQLField(1, "nom", str))
        self._connect_field("adresse", SQLField(2, "adresse", str, False, 30))
        self._connect_field("telephone", SQLField(3, "telephone", str, False, 12))
        #on parcourt tous les clients de la base de donnée
        for client in Database.get_records("orm.Client"):
            print(str(client.numero) + " ; " + str(client.nom) + " ; " + str(client.adresse) + " ; " + str(client.telephone))