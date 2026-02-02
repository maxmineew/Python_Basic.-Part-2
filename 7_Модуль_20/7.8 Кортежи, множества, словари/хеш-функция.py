def simple_hash(input_string): # На вход получаем строку
    hash_value = 0
    for char in input_string: # Запускаем цикл по символам строки
        hash_value += ord(char) # Суммируем код каждого символа
    return hash_value # На выходе получаем сумму — некое числовое значение