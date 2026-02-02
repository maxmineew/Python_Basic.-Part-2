word_count = 0
def is_palindrome(word):
    return word == word[::-1]

with open("words.txt", 'r', encoding='utf-8') as file, open('errors.log', 'w', encoding='utf-8') as log_file:
    for line in file:
        try:
            clear_line = line.strip()
            if clear_line.isalpha():
                word_count += is_palindrome(clear_line) #это краткая запись:
                # if is_palindrome(clear_line):
                # word_count += 1
            else:
                raise ValueError('\n Строка не полностью состоит из букв!')
        except ValueError as exc:
            log_file.write(str(exc))
    print(f'Количество слов, из которых можно получить палиндром: {word_count}.')
