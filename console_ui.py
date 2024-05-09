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
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        print('Придумайте серкетный вопрос-ответ для вашего аккаунта: ')
        security_question = input('Вопрос: ')
        security_answer = input('Ответ: ')
        self.db.add_user((login, password, security_question, security_answer))

    def __authorization(self, current_user_data):
        count = 3
        print('\n---Авторизация---')
        while True:
            login = input('Логин: ')
            password = input('Пароль: ')
            
            if login == current_user_data[0][0] and password == current_user_data[0][1]:
                return True
            elif count > 1:
                print('Неккореткный ввод, попробуйте еще раз')
                count -= 1
            else:
                print('Неккореткный ввод, попробуйте атворизоваться через "вопрос-ответ"')
                return self.__reserve_authorization(current_user_data)
        
    def __reserve_authorization(self, current_user_data):
        count = 2
        while True:
            print(current_user_data[0][2])
            answer = input(': ')

        
            if answer == current_user_data[0][3]:
                return True
            elif count > 1:
                print('Неккореткный ввод, попробуйте еще раз')
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