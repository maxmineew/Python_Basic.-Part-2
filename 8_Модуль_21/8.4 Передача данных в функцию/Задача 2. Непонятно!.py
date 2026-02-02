'''Друг никак не может понять эту тему с изменяемыми и неизменяемыми типами, ссылками, объектами и их id.
Видя, как он мучается, вы решили помочь ему и объяснить эту тему наглядно.
    Пользователь вводит любой объект. Напишите программу, которая выводит на экран тип введённых данных,
информацию о его изменяемости, а также id этого объекта.
    Помните, что через input можно получить только строку, что бы вы ни вводили.
В данном случае ввод можно выполнить вручную, просто вписав нужный объект в переменную,
 без использования функции input.
    Пример 1:
data_input = "привет"
Тип данных: <class 'str'> (строка)
Неизменяемый (immutable)
id объекта: 140013695242560
    Пример 2:
data_input  = {"a": 10, "b": 20}
Тип данных: <class 'dict'> (словарь)
Изменяемый (mutable)
id объекта: 140005763835136'''

# Вместо input() можно просто вручную присвоить значение переменной data_input
# Пользователь (или вы, объясняя тему) можете менять эту строчку для разных примеров:

# ПРИМЕРЫ ДЛЯ ТЕСТИРОВАНИЯ (раскомментируйте одну строку):

# 1. Неизменяемые типы
# data_input = "привет"                    # строка
# data_input = 42                          # целое число
# data_input = 3.14                        # число с плавающей точкой
# data_input = True                        # булево значение
data_input = (1, 2, 3)                   # кортеж
# data_input = frozenset([1, 2, 3])        # неизменяемое множество

# 2. Изменяемые типы
# data_input = {"a": 10, "b": 20}  # словарь
# data_input = [1, 2, 3]                   # список
# data_input = {1, 2, 3}                   # множество
# data_input = bytearray(b"hello")         # массив байт

# Определяем тип объекта
obj_type = type(data_input)
type_name = obj_type.__name__

# Создаем словарь с читаемыми именами типов
type_translations = {
    'str': 'строка',
    'int': 'целое число',
    'float': 'число с плавающей точкой',
    'bool': 'булево значение',
    'tuple': 'кортеж',
    'frozenset': 'неизменяемое множество',
    'dict': 'словарь',
    'list': 'список',
    'set': 'множество',
    'bytearray': 'массив байт'
}

# Получаем человеко-читаемое имя типа
readable_type = type_translations.get(type_name, type_name)

# Определяем, изменяемый ли тип
# Основные неизменяемые типы в Python
immutable_types = (int, float, str, tuple, bool, frozenset, bytes)

if isinstance(data_input, immutable_types):
    mutability = "Неизменяемый (immutable)"
else:
    mutability = "Изменяемый (mutable)"

# Получаем id объекта
obj_id = id(data_input)

# Выводим результат
print(f"Тип данных: {obj_type} ({readable_type})")
print(mutability)
print(f"id объекта: {obj_id}")

# ДОПОЛНИТЕЛЬНАЯ ДЕМОНСТРАЦИЯ (для объяснения)
print("\n" + "=" * 50)
print("ДЕМОНСТРАЦИЯ РАЗНИЦЫ МЕЖДУ ИЗМЕНЯЕМЫМИ И НЕИЗМЕНЯЕМЫМИ ТИПАМИ:")
print("=" * 50)

# Создаем копии для демонстрации
print(f"\n1. Создаем переменную copy_var и присваиваем ей тот же объект:")
copy_var = data_input
print(f"   data_input id: {id(data_input)}")
print(f"   copy_var id: {id(copy_var)}")
print(f"   id совпадают? {id(data_input) == id(copy_var)}")

print(f"\n2. Пробуем 'изменить' объект (операция зависит от типа):")

if isinstance(data_input, immutable_types):
    print(f"   До изменения: data_input = {data_input}")
    print(f"   Пытаемся изменить data_input...")

    if isinstance(data_input, str):
        # Для строк покажем конкатенацию
        print(f"   data_input += '!' (конкатенация)")
        data_input += '!'
    elif isinstance(data_input, (int, float)):
        # Для чисел - арифметическую операцию
        print(f"   data_input += 1")
        data_input += 1
    elif isinstance(data_input, tuple):
        # Для кортежей - попытку конкатенации
        print(f"   data_input += (4,)")
        data_input += (4,)

    print(f"   После 'изменения': data_input = {data_input}")
    print(f"   id data_input теперь: {id(data_input)}")
    print(f"   id copy_var: {id(copy_var)}")
    print(f"   Вывод: Создался НОВЫЙ объект, copy_var остался прежним!")

else:
    print(f"   До изменения: data_input = {data_input}")
    print(f"   Пытаемся изменить data_input...")

    if isinstance(data_input, dict):
        print(f"   data_input['c'] = 30 (добавляем новый ключ)")
        data_input['c'] = 30
    elif isinstance(data_input, list):
        print(f"   data_input.append(4) (добавляем элемент)")
        data_input.append(4)
    elif isinstance(data_input, set):
        print(f"   data_input.add(4) (добавляем элемент)")
        data_input.add(4)

    print(f"   После изменения: data_input = {data_input}")
    print(f"   id data_input теперь: {id(data_input)}")
    print(f"   id copy_var: {id(copy_var)}")
    print(f"   copy_var = {copy_var}")
    print(f"   Вывод: Изменился СУЩЕСТВУЮЩИЙ объект, copy_var тоже изменился!")