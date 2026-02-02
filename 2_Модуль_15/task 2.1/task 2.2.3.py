# # Задача 3. Собачьи бега
# # В собачьих бегах участвует N собак, у каждой из них есть определённое количество очков
# # за сезон. На огромном табло выводятся очки каждой собаки. Однако при выводе был обнаружен
# # баг: собаки с наибольшим и наименьшим количеством очков поменялись местами! Нужно это исправить.
# #
# # Дан список очков из N собак. Напишите программу, которая меняет местами наибольший и наименьший
# # элементы в списке.
#
nums_list = []

N = int(input('Кол-во чисел в списке: '))

for _ in range(N):
    num = int(input('Очередное число: '))
    nums_list.append(num)

if nums_list:
    maximum = nums_list[0]
    minimum = nums_list[0]

    minimum_index = 0
    maximum_index = 0
    for index, i in enumerate(nums_list):

        if maximum < i:
            maximum = i
            maximum_index = index

        if minimum > i:
            minimum = i
            minimum_index = index

    print('Максимальное число в списке:', maximum)
    print('Минимальное число в списке:', minimum)

    print(nums_list)
    nums_list[minimum_index], nums_list[maximum_index] = nums_list[maximum_index], nums_list[minimum_index]
    print(nums_list)
else:
    print('В списке нету чисел')

minimum = 1

for i in nums_list:

    if maximum < i:
        maximum = i

    if minimum > i:
        minimum = i

print(f'Наибольшее количество очков {maximum_index+1} собаки: {maximum}')

print('Наименьшее количество очков:', nums_list[maximum_index])


# scores = [10, 20, 30, 40, 50]
#
# min_score = min(scores)
# max_score = max(scores)
#
# min_index = scores.index(min_score)
# max_index = scores.index(max_score)
#
# scores[min_index], scores[max_index] = scores[max_index], scores[min_index]
#
# print(scores) # [50, 20, 30, 40, 10]