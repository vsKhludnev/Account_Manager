from data import Database

class Interface():
    def __init__(self):
        self.db = Database()

    def run(self):
        if self.log_in() == True:
            self.main_menu()


    def log_in(self):
        current_user = self.db.get_user()
        if len(current_user) == 0:
            self.__registration()
            return True
        else:
            return self.__authorization(current_user)

    def __registration(self):
        print('\n---Регистрация---')
        login = self.__input_login()
        password = self.__input_password()
        print('Придумайте серкетный вопрос-ответ для вашего аккаунта: ')
        security_question = self.__input_security_question()
        security_answer = self.__input_security_answer()
        self.db.add_user((login, password, security_question, security_answer))

    def __input_login(self):
        while True:
            login = input('Логин: ')
            if len(login) >= 3:
               return login
            else:
                print('Логин не должен быть короче трех символов')

    def __input_password(self):
        while True:
            password = input('Пароль: ')
            if len(password) >= 5:
                return password
            else:
                print('Пароль не должен быть короче пяти символов')

    def __input_security_question(self):
        while True:
            security_question = input('Вопрос: ')
            if len(security_question) >= 5:
                return security_question
            else:
                print('Пожалуйста придумайте адекватный впорос, вам же будет проще')

    def __input_security_answer(self):
        while True:
            security_answer = input('Ответ: ')
            if len(security_answer) > 0:
                return security_answer
            else:
                print('Отвечайте на заданный вопрос!')
        

    def __authorization(self, current_user_data):
        count = 3
        print('\n---Авторизация---')
        while True:
            login = input('Логин: ')
            password = input('Пароль: ')
            
            if login == current_user_data[0][0] and password == current_user_data[0][1]:
                return True
            elif count > 1:
                print('\033[31m Некорректный ввод\033[0m, попробуйте еще раз')
                count -= 1
            else:
                print('\033[31m Неккореткный ввод\033[0m, попробуйте авторизоваться через "вопрос-ответ"')
                return self.__reserve_authorization(current_user_data)
        
    def __reserve_authorization(self, current_user_data):
        count = 2
        while True:
            print(current_user_data[0][2])
            answer = input(': ')

        
            if answer == current_user_data[0][3]:
                return True
            elif count > 1:
                print('\033[31m Некорреткный ввод\033[0m, попробуйте еще раз')
                count -= 1
            else:
                return False
        


    def main_menu(self):
        while True:
            print('\n\n---Главное меню---')
            print('Выберите действие:' + 
                  '\n 1 - Показать записи' + 
                  '\n 2 - Добавить записи' + 
                  '\n 3 - Удалить записи' + 
                  '\n\n 5 - Изменить данные для авторизации' + 
                  '\n\n 0 - Выход')
            choice = input(': ')
            if choice == '0':
                self.db.close_database()
                return
            elif choice == '1':
                self.get_menu()
            elif choice == '2':
                self.add_menu()
            elif choice == '3':
                pass
            elif choice == '5':
                pass
            elif choice == '/delete':
                self.db.delete_user()
            

    def get_menu(self):
        while True:
            print("""Выберите действие:
                  1 - Показать все записи
                  2 - По имени
                  3 - По категории

                  0 - Назад
                  """)
            choice = input(': ')
            if choice == 1:
                self.db.get_account_all()
            elif choice == 2:
                name = input('Введите название: ')
                self.db.get_account_byname(name)
            elif choice == 3:
                category = input('Введите категорию: ')
                self.db.get_account_bycategory(category)
            elif choice == 0:
                return

    def add_menu(self):
        category = input('Введите категорию: ')
        name = input('Введите название: ')
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        addit = input('Введите прочую информацию (если необходимо): ')
        self.db.add_account((category, name, login, password, addit))

    def delete_menu(self):
        while True:
            print("""Выберите действие:
                  1 - Удалить все записи
                  2 - Удалить по имени

                  0 - Назад
                  """)
            choice = input(': ')
            if choice == 1:
                self.db.delete_account_all()
            elif choice == 2:
                name = input('Введите название: ')
                self.db.delete_account_byname(name)
            elif choice == 0:
                return

    def edit_user_menu(self):
        pass