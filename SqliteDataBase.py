import sqlite3
from sqlite3 import Error, IntegrityError, Connection


def create_SqlLite_connection(path: str) -> Connection:
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(conector: Connection, query: str) -> None:
    cursor = conector.cursor()
    try:
        cursor.execute(query)
        conector.commit()
        print("Query executed successfully")
        return cursor
    except IntegrityError:
        print('Вы добавили уже такую запись!')
        print('Это поле уникально.')
    except Error as e:
        print(f"The error '{e}' occurred")
