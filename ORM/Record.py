from ORM.SQLField import *

class Record:
    def __init__(self, table_name=None):
        if table_name is None :
            table_name = type(self).__name__
            self.table_name = table_name
            self.fields = {}

    def __add_attribute(self, python_field_name):
        setattr(self, python_field_name, None)

    def _connect_field(self, python_field_name, sql_field : SQLField):
        self.__add_attribute(python_field_name)

        # Compléter en associant le champ sql au champ python à travers le tableau associatif(self.fields)
        self.fields[python_field_name] = sql_field
        pass

    def save(self):
        pass # compléter en sauvegardant le champ dans la base de donnée SQLite.

    # Il faut choisir entre un INSERT et un UPDATE en fonction des cas
    def delete(self):
        pass # Compléter : supprimer le champ dans la base de donnée