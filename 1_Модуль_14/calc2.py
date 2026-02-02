print("Калькулятор 2")

# while True:
#     try:
#         a = float(input("Введите первое число: "))
#         b = float(input("Введите второе число: "))
#         break
#     except ValueError:
#         print("Вы ввели не число, попробуйте еще раз")

 operand = float(input("Сколько операндов? "))
for i in range(1, operand + 1):
    i = float(input("Введите операнд: "))

while True:
    x = input("Выберите операцию (+, -, *, /): ")
    if x in ['+', '-', '*', '/']:
        break
    else:
        print("Вы ввели неправильный символ, попробуйте еще раз")

if x == '+':
    c = a + b
elif x == '-':
    c = a - b
elif x == '*':
    c = a * b
else:
    while b == 0:
        print("На ноль делить нельзя, попробуйте еще раз")
        b = float(input("Введите второе число (отличное от нуля): "))
    c = a / b

print(f"{a} {x} {b} = {c}")