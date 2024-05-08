import sqlite3

class Database():
    def __init__(self, database_name='Database.db'):
        self.connect = sqlite3.connect(database_name)
        self.cursor = self.connect.cursor()

        self.cursor.execute('CREATE TABLE IF NOT EXISTS Users (login text, password text, security_question text, security_answer text)')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Accounts (category text, name text, login text, password text, addit text)')


    def add_user(self, input_data):
        self.cursor.execute(f'INSERT INTO Users (login, password, security_question, security_answer) VALUES (?, ?, ?, ?)', (input_data))
        self.connect.commit()

    def get_user(self):
        self.cursor.execute('SELECT * FROM Users')
        return self.cursor.fetchall()

    def delete_user(self):
        self.cursor.execute('DELETE FROM Users')
        self.connect.commit()