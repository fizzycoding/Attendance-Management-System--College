import mysql.connector as mysql
from mysql.connector import Error


def getDB():
    db_name = "college_database"
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'port': 3306,
        'connection_timeout': 5  # 5 second timeout
    }

    try:
        print("Connecting to database....")
        connection = mysql.connect(**config)

        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Successfully connected to MySQL Server version {db_info}")

            cursor = connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            cursor.execute(f"USE {db_name}")
            print(f"Database '{db_name}' is ready")

            return connection

    except Error as e:
        raise Exception(f"Database connection failed: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")
        raise Exception(e)
