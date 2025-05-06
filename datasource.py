import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self, dbconfig):
        try:
            self.connection = mysql.connector.connect(**dbconfig)
            if self.connection.is_connected():
                print("Connection established / Verbindung hergestellt")
                self.cursor = self.connection.cursor()
        except Error as e:
            print(f"Connection error/ Verbindungsfehler: {e}")
            self.connection = None
            self.cursor = None

    def close(self):
        self.cursor.close()
        self.connection.close()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def insert_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
        except Error as e:
            print(e)
            self.connection.rollback()


if __name__ == '__main__':
    pass
