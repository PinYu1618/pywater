import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery


def createDB():
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("./db/dev.db")
    if not db.open():
        print("Unable to connect to the database")
        sys.exit(1)

    # Create a query and execute it right away using .exec()
    createTableQuery = QSqlQuery()
    createTableQuery.exec(
        """
        CREATE TABLE records (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            date VARCHAR(40) NOT NULL,
            water VARCHAR(50),
            weight VARCHAR(40) NOT NULL
        )
        """
    )
    print(db.tables())

    # Creating a query for later execution using .prepare()
    insertDataQuery = QSqlQuery()
    insertDataQuery.prepare(
        """
        INSERT INTO records (
            date,
            water,
            weight
        )
        VALUES (?, ?, ?)
        """
    )

    # Sample data
    data = [
        ("Joe", "Senior Web Developer", "joe@example.com"),
        ("Lara", "Project Manager", "lara@example.com"),
        ("David", "Data Analyst", "david@example.com"),
        ("Jane", "Senior Python Developer", "jane@example.com"),
    ]

    # Use .addBindValue() to insert data
    for name, job, email in data:
        insertDataQuery.addBindValue(name)
        insertDataQuery.addBindValue(job)
        insertDataQuery.addBindValue(email)
        insertDataQuery.exec()


def connect():
    print("Hi from db.")
