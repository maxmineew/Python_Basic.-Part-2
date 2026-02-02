# '''В уроке мы написали функцию, которая ищет нужный нам файл во всех
# подкаталогах указанной директории. Однако, как мы понимаем, файлов с
# таким названием может быть несколько.
#    Напишите функцию, которая принимает на вход абсолютный путь до директории
#  и имя файла, проходит по всем вложенным файлам и папкам и выводит на экран все абсолютные пути с этим именем.
#
# Пример:
# Ищем в: C:/Users/Roman/PycharmProjects/Skillbox
# Имя файла: lesson2
# Найдены следующие пути:
# C:/Users/Roman/PycharmProjects/Skillbox\Module15\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module16\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module17\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module18\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module19\lesson2.py
# C:/Users/Roman/PycarmProjects/Skillbox\Module20\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module21\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module22\lesson2.py'''
import os

def find_file(cur_path, file_name):
    print("Запуск поиска в папке", os.path.join(os.path.abspath(cur_path)))
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        print("Проверяется путь", path)
        if file_name == i_elem:
            print(os.path.abspath(path))
        elif os.path.isdir(path):
            result = find_file(path, file_name)
            if result:
                break
    else:
        result = None

    return result

find_file('..', 'test.py')