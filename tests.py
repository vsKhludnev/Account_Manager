def test(test_name, expected_result, actual_result):
    if expected_result == actual_result:
        print(f'{test_name}: \033[32mPassed\033[0m')
    else:
        print(f'{test_name}: \033[31mFailed\033[0m')
        print(f'\texpected result - {expected_result}')
        print(f'\tactual result - {actual_result}')