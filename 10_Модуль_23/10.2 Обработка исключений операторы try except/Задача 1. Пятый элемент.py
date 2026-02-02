try:
    BRUCE_WILLIS = 42
    input_str= input('Введите строку: ')
    input_data = int(input_str)
    leeloo = int(input_str[4])
    result = BRUCE_WILLIS * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')
except ValueError:
    print('Невозможно преобразовать к числу')
except IndexError:
    print('Выход за границы списка.')
except TypeError:
    print('Ошибка типа данных')