file_ages = None
file_result = None

try:
    file_ages = open("ages.txt", "r", encoding="utf8")
    file_result = open("result.txt", "x", encoding="utf8")
    # режим 'x' - это эксклюзивное создание, бросается исключение FileExistsError, если файл уже существует.
except (FileExistsError, PermissionError, IsADirectoryError) as exc:  # названия исключений можно группировать в кортежи
    print("Поймано исключение: ", exc, type(exc))

if file_result and file_ages:
    names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    count = 0
    for line in file_ages:
        try:
            clear_line = line.rstrip()
            int(clear_line)  # на всякий случай пытаемся преобразить данные в int, но не сохраняем это в переменную, т.к. записывать нам
            # в файл придётся именно строку
            file_result.write(names[count-1] + " - " + clear_line)
            count += 1
        except (ValueError, TypeError) as exc:
            print("Поймано исключение: ", exc, type(exc))

    file_ages.close()
    file_result.close()