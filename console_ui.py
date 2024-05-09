from data import Database

class Interface():
    def __init__(self):
        self.db = Database()

    def run(self):
        if self.log_in == True:
            self.main_menu()


    def log_in(self):
        current_user = self.db.get_user()
        if len(current_user) == 0:
            self.__registration()
        else:
            self.__authorization(current_user)

    def __registration(self):
        print('---Регистрация---')
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        print('Придумайте серкетный вопрос-ответ для вашего аккаунта: ')
        security_question = input('Вопрос: ')
        security_answer = input('Ответ: ')
        self.db.add_user((login, password, security_question, security_answer))

    def __authorization(self, current_user_data):
        print('---Авторизация---')
        login = input('Логин: ')
        password = input('Пароль: ')

        if login == current_user_data[0] and password == current_user_data[1]:
            return True
        else:
            return self.__reserve_authorization(current_user_data)
        
    def __reserve_authorization(self, current_user_data):
        print(current_user_data[2])
        answer = input(': ')

        if answer == current_user_data[3]:
            return True
        else:
            return False
        


    def main_menu(self):
        while True:
            print('---Главное меню---')
            print("""Выберите действие:
                  1 - Показать записи
                  2 - Добавить записи
                  3 - Удалить записи

                  5 - Изменить данные для авторизации
                  
                  0 - Выход
                  """)
            choice = input(': ')
            if choice == '0':
                return
            elif choice == '1':
                self.get_menu()
            elif choice == '2':
                self.add_menu()
            elif choice == '3':
                pass
            elif choice == '5':
                pass
            

    def get_menu(self):
        pass

    def add_menu(self):
        pass

    def delete_menu(self):
        pass

    def edit_user_menu(self):
        pass