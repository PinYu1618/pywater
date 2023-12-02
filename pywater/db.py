import sys

from PyQt5.QtSql import QSqlDatabase


def createDB():
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("./db/hello.db")
    if not db.open():
        print("Unable to connect to the database")
        sys.exit(1)


def connect():
    print("Hi from db.")
