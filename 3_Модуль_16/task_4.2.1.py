'''Пользователь вводит числа A и B. Напишите программу, которая генерирует два списка: в первом лежат кубы чисел в диапазоне от А до В, во втором — квадраты чисел в этом же диапазоне. Выведите списки на экран. Для генерации используйте list comprehensions (как и в следующих задачах).
 
Пример:
Левая граница: 5
Правая граница: 10
 
Список кубов чисел в диапазоне от 5 до 10: [125, 216, 343, 512, 729, 1000]
Список квадратов чисел в диапазоне от 5 до 10: [25, 36, 49, 64, 81, 100]'''

cube_list = []
square_list = []

left_border = int(input('Левая граница: '))
right_border = int(input('Правая граница: '))
cube_list = [left_border ** 3 for left_border in range(left_border, right_border + 1)]
square_list = [right_border ** 2 for right_border in range(left_border, right_border + 1)]

print(f'\nСписок кубов чисел в диапазоне от {left_border} до {right_border}: {cube_list}')
print(f'Сисок квадратов чисел в диапазоне от {left_border} до {right_border}: {square_list}')