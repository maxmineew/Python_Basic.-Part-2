summa = 0
diff = 0
count = 0
compose = 1
try:
    file = open('D:/task/group_1.txt', 'r', encoding = 'UTF-8')
    for i_line in file:
        info = i_line.split()
        summa += int(info[2])
    file.close()
    file = open('D:/task/group_1.txt', 'r', encoding='UTF-8')
    for i_line in file:
        info = i_line.split()
        diff -= int(info[2])
    file.close()

    file_2 = open(r'D:\task\Additional_info\group_2.txt', 'r', encoding='UTF-8')
    for i_line in file_2:
        info = i_line.split()
        compose *= int(info[2])
    file_2.close()
except FileNotFoundError:
    print('Файл не найден')
except TypeError:
    print('Ошибка типа данных')
except ValueError:
    print('Нельзя преобразовать данные в целое.')
else:
    print("Запись прошла успешно.")
finally:
    print("Программа завершена.")
    print('Сумма очков первой группы:', summa)
    print('Разность очков первой группы:', diff)
    print('Произведение очков второй группы:', compose)