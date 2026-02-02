# Ввод списка и преобразование в целые числа
input_list = [int(x) for x in input("Введите целые числа через пробел: ").split()]

# Проход по списку в обратном порядке
for i in range(len(input_list) - 1, -1, -1):
    if input_list[i] % 2 == 0:  # Если число четное
        print(input_list[i])  # Вывод четного числаt(input_list[i])  # Вывод четного числачисла