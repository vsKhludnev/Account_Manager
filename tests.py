def test(test_name, expected_result, actual_result):
    if expected_result == actual_result:
        print(f'{test_name}: \033[32mPassed\033[0m')
    else:
        print(f'{test_name}: \033[31mFailed\033[0m')
        print(f'\texpected result - {expected_result}')
        print(f'\tactual result - {actual_result}')

from data import Database
test_db = Database('Test_database.db')

# Создание пользователя
input_user_data = ('Slava', 'password', 'Are you?', 'Yes')
test_db.add_user(input_user_data)
test('Add user', [input_user_data], test_db.get_user())

# Удаление пользователя
test_db.delete_user()
test('Delete user', [], test_db.get_user())