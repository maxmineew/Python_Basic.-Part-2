try:
    user_input = input("Введите строку для записи в файл: ")
    number = int(user_input)   # ValueError, если не число
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(str(number))
except ValueError:
    print("Нельзя преобразовать данные в целое.")
except OSError:
    print("Проблема при открытии файла.")
except Exception as e:
    print("Неожиданная ошибка:", e)
else:
    print("Запись прошла успешно.")
finally:
    print("Программа завершена.")