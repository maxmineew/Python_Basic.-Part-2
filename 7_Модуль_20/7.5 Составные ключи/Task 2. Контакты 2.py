'''Задача 2. Контакты 2
Мы уже реализовывали телефонную книгу для Степана, однако её проблема была в том, что туда нельзя было добавить людей с
одинаковыми именами. Надо это исправить.
Напишите программу, которая запрашивает у пользователя имя контакта, фамилию и номер телефона, добавляет их в словарь
и выводит на экран текущий словарь контактов. Словарь состоит из пар «Ф. И. — телефон», где Ф. И. — это составной ключ.
Запрос на добавление идёт бесконечно (но можно задать своё условие для завершения программы). Обеспечьте контроль ввода:
 если этот человек уже есть в словаре, то выведите соответствующее сообщение.'''

current_contacts = {}
while True:
    print("Текущие контакты на телефоне:")
    if current_contacts:
        for name in current_contacts:
            print(name, current_contacts[name])
    else:
        print("<Пусто>")
    new_name = input("Введите имя (для остановки введите пустую строку): ")
    new_surname = input("Введите фамилию: ")
    new_telephone = int(input("Введите номер телефона: "))
    new_contact = (new_name, new_surname)
    if new_contact in current_contacts:
        print("Ошибка: такое имя уже существует.")
    else:
        current_contacts[new_contact] = new_telephone

# Или:
contacts = {}

while True:
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    name_n_surname = (name, surname)
    if name_n_surname not in contacts:
        contacts[name_n_surname] = int(input("Введите номер телефона: "))
    else:
        print("Такой контакт уже есть!")
    print(contacts)




