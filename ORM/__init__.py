from ORM.Database import *
import sqlite3

Database.get_sqlite_singleton()

for row in Database.get_records("client"):
    print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))
