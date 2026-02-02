# '''Как мы помним, скрипты — это просто куча строк текста, хоть они и
# понятны только программисту. Таким образом, с ними можно работать точно
# так же, как и с обычными текстовыми файлами.
# Используя функцию поиска файла из предыдущего урока, реализуйте программу,
#  которая находит внутри указанного пути все файлы с искомым названием и
#  выводит на экран текст одного из них (выбор можно сгенерировать случайно).
# Подсказка: можно использовать, например, список для сохранения найденного пути.'''

import os


def find_files(cur_path, file_name):
    """Рекурсивно находит все файлы с заданным именем"""
    found_files = []

    # Проверяем все элементы в текущей папке
    for item in os.listdir(cur_path):
        full_path = os.path.join(cur_path, item)

        # Если это файл и имя совпадает - добавляем в список
        if os.path.isfile(full_path) and item == file_name:
            found_files.append(full_path)

        # Если это папка - рекурсивно ищем внутри
        elif os.path.isdir(full_path):
            found_files.extend(find_files(full_path, file_name))

    return found_files


def read_random_file(files_list):
    """Читает содержимое случайного файла из списка"""
    if not files_list:
        print("Файлы не найдены!")
        return

    # Выбираем случайный файл
    selected_file = random.choice(files_list)
    print(f"Выбран файл: {selected_file}")
    print("-" * 50)

    # Читаем и выводим содержимое файла
    try:
        with open(selected_file, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except UnicodeDecodeError:
        # Если не получается прочитать как текст, пробуем бинарный режим
        try:
            with open(selected_file, 'rb') as file:
                content = file.read()
                print(f"Файл содержит бинарные данные. Размер: {len(content)} байт")
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")


def main():
    # Получаем входные данные
    search_path = input("Введите путь для поиска (по умолчанию текущая папка): ").strip()
    if not search_path:
        search_path = '.'

    file_name = input("Введите имя файла для поиска: ").strip()

    if not file_name:
        print("Имя файла не указано!")
        return

    # Проверяем существование пути
    if not os.path.exists(search_path):
        print(f"Путь '{search_path}' не существует!")
        return

    # Ищем файлы
    print(f"\nПоиск файлов '{file_name}' в '{search_path}'...")
    found_files = find_files(search_path, file_name)

    # Выводим результаты
    print(f"Найдено файлов: {len(found_files)}")

    if found_files:
        for i, file_path in enumerate(found_files, 1):
            print(f"{i}. {file_path}")

        print("\n" + "=" * 50)
        read_random_file(found_files)


if __name__ == "__main__":
    main()