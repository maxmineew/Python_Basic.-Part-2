#
# n = int(input("Кол-во чисел в списке: "))
#
# nums_list = []
# for i in range(n):
#     num = int(input(f"Введите {i + 1} число: "))
#     nums_list.append(num)
#
# k = int(input("\nВведите делитель: "))
# print()
#
# sum_indexes = 0
# for i in range(n):
#     if nums_list[i] % k == 0:
#         print(f"Индекс числа {nums_list[i]}: {i}")
#         sum_indexes += i
# print(f"Сумма индексов: {sum_indexes}")

nums_list = []

N = int(input('Кол-во чисел в списке: '))

for i in range(1, N + 1):
    print("Введите ", i, "число: ")
    num = int(input())
    nums_list.append(num)

divider = int(input('Введите делитель: '))
index = 0
sum_indexes = 0
for index, number in enumerate(nums_list):  # enumerate в таких случаях очень полезен
    if number % divider == 0:
        print(f"Индекс числа {number}: {index}")
        sum_indexes += index