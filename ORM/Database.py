import sqlite3
class Database:

    con = None

    @staticmethod
    def get_sqlite_singleton():
        global con
        con = sqlite3.connect(':memory:')
        f = open('ventes.sql', 'r')
        str = f.read()
        con.executescript(str)
        pass

    @staticmethod
    def get_records(record_type):
        global con
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM """+record_type)
        return cursor.fetchall()
        # retourne la liste de tous les enregistrements dans la base de donnée, en fonction du type en paramètre
        #pour avoir une instance de record_type : record = __get_class(str)()
        pass

    @staticmethod
    def __get_class( kls ):
        parts = kls.split('.')
        module = ".".join(parts[:-1])
        m = __import__( module )
        for comp in parts[1:]:
            m = getattr(m, comp)
        return m