def rabin_karp_search(text, pattern):
    # Проверяем случаи, когда текст или подстрока пустые
    if not text or not pattern:
        return []

    # Вычисляем хеш-значение для подстроки и первого окна текста
    pattern_hash = hash(pattern)
    window_hash = hash(text[:len(pattern)])

    matches = [] # Список индексов совпадений

    # Проходим по тексту с помощью скользящего окна
    for i in range(len(text) - len(pattern) + 1):
        # Если хеш-значения совпадают, сравниваем каждый символ окна с подстрокой
        if pattern_hash == window_hash and text[i:i + len(pattern)] == pattern:
            # Стоит уточнить, что благодаря ленивому выполнению Python, если первое условие в связке AND вернёт False, то второе не будет запускаться вообще
            matches.append(i)

        # Обновляем хеш-значение для следующего окна
        window_hash = hash(text[i + 1:i + len(pattern) + 1])

    return matches

# Пример использования
text = "abracadabra"
pattern = "dab"
matches = rabin_karp_search(text, pattern)
print(f"Совпадения найдены на позициях: {matches}")