import sqlite3

class Database():
    def __init__(self, database_name='Database.db'):
        self.connect = sqlite3.connect(database_name)
        self.cursor = self.connect.cursor()

        self.cursor.execute('CREATE TABLE IF NOT EXISTS Users (login text, password text, security_question text, security_answer text)')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Accounts (category text, name text, login text, password text, addit text)')

    def close_database(self):
        self.connect.commit()
        self.connect.close()

    # Блок Users
    def add_user(self, input_data):
        self.cursor.execute(f'INSERT INTO Users (login, password, security_question, security_answer) VALUES (?, ?, ?, ?)', (input_data))
        self.connect.commit()

    def get_user(self):
        self.cursor.execute('SELECT * FROM Users')
        return self.cursor.fetchall()

    def delete_user(self):
        self.cursor.execute('DELETE FROM Users')
        self.cursor.execute('DELETE FROM Accounts')
        self.connect.commit()

    # Блок Accounts
    def __search_account(self, search_criteria, search_value):
        self.cursor.execute(f'SELECT * FROM Accounts WHERE {search_criteria} = ?', (search_value,))
        return self.cursor.fetchall()

    def get_account_all(self):
        self.cursor.execute('SELECT * FROM Accounts')
        return self.cursor.fetchall()
    
    def get_account_byname(self, name):
        return self.__search_account('name', name)
        
    def get_account_bycategory(self, category):
        return self.__search_account('category', category)
    
    def add_account(self, input_data):
        self.cursor.execute(f'INSERT INTO Accounts (category, name, login, password, addit) VALUES (?, ?, ?, ?, ?)', (input_data))
        self.connect.commit()

    def delete_account_all(self):
        self.cursor.execute('DELETE FROM Accounts')
        self.connect.commit()

    def delete_account_byname(self, name):
        if self.__search_account('name', name) != []:
            self.cursor.execute('DELETE FROM Accounts WHERE name = ?', (name,))
            self.connect.commit()
        else:
            print('Запись c таким именем не найдена')

    def edit_account(self, input_data):
        self.delete_account_byname(input_data[1])
        self.add_account(input_data)
        self.connect.commit()
