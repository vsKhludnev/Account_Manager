def test(test_name, expected_result, actual_result):
    if expected_result == actual_result:
        print(f'{test_name}: \033[32mPassed\033[0m')
    else:
        print(f'{test_name}: \033[31mFailed\033[0m')
        print(f'\texpected result - {expected_result}')
        print(f'\tactual result - {actual_result}')

from data import Database
test_db = Database('Test_database.db')

# Удаление пользователя
test_db.delete_user()
test('Delete user', [], test_db.get_user())

# Создание пользователя
input_user_data = ('Slava', 'password', 'Are you?', 'Yes')
test_db.add_user(input_user_data)
test('Add user', [input_user_data], test_db.get_user())


# Добавление записей
input_account_1 = ('Social', 'Vkontakte', 'Slavanew', '11021998', 'tel.number +79786513546')
input_account_2 = ('Social', 'Telegram', '+79786513546', 'code', '')
input_account_3 = ('Finance', 'Tinkoff', 'Slavanew', '1590', '1590')
test_db.add_account(input_account_1)
test_db.add_account(input_account_2)
test_db.add_account(input_account_3)
test('Add tree accounts', [input_account_1, input_account_2, input_account_3], test_db.get_account_all())

# Вывод записей по поиску
test('Search by category', [input_account_1, input_account_2], test_db.get_account_bycategory(input_account_1[0]))
test('Search by name', [input_account_1], test_db.get_account_byname(input_account_1[1]))

# Удаление записей по имени
test_db.delete_account_byname(input_account_1[1])
test(f'Delete {input_account_1[1]} account', [input_account_2,input_account_3], test_db.get_account_all())

# Удаление всех записей
test_db.delete_account_all()
test('Delete all accounts', [], test_db.get_account_all())


test_db.delete_user()


# Тестирование интерфейса
from console_ui import Interface
class TestInterface(Interface):
    def __init__(self):
        super().__init__()
        self.db = Database('Test_database.db')

test_interface = TestInterface()

# Тестирование регистрации и авторизации
test_interface.log_in()
test_interface.log_in()