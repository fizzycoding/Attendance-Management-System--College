import sqlite3

db_name = "college_database"


def getDB():
    try:
        print("Connecting to database....")
        connection = sqlite3.connect(db_name)

        connection.execute("PRAGMA foreign_keys = ON;")
        connection.row_factory = sqlite3.Row
        print("SQLite database connected successfully")
        return connection

    except Exception as e:
        print(f"Unexpected error: {e}")
        raise Exception(e)
