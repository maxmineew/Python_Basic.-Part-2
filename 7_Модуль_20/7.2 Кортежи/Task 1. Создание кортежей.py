'''Заполните один кортеж десятью случайными целыми
 числами от 0 до 5 включительно. Также заполните второй
  кортеж числами от −5 до 0. Объедините два кортежа,
  создав тем самым третий кортеж. С помощью
 метода кортежа определите в нём количество нулей.
Выведите на экран третий кортеж и количество нулей в
нём.'''
import math
import random

def create_random_tuple(a, b, n):
    return tuple([random.randint(a, b) for _ in range(n)])

first = create_random_tuple(0, 5, 10)
second = create_random_tuple(-5, 0, 10)
third = first + second
nuls_count = third.count(0)
print(first)
print(second)
print(third, nuls_count)