while True:
    grats_template = input('Введите шаблон поздравления, '
                           'в шаблоне нужно использовать конструкцию {name}:')
    # Сделаем контроль ввода, нам нужно проверить, есть ли эта конструкция
    # внутри строки, которую вводит пользователь.

    if '{name}' in grats_template:
        break
    print('Ошибка, отсутствует конструкция {name}.')
# Сколько будет имен мы не знаем, т.е. используем не list comprefensions, а append
print('Введите список имен (заканчивается на end):')
names_list = []
while True:
    name = input('Имя: ')
    if name != 'end':
        names_list.append(name)
    else:
        break

for i_name in names_list:
    print(grats_template.format(name = i_name))