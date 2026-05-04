def check_match_at_position(text: str, pattern: str, start_position: int) -> int:
    """
    Проверяет, совпадает ли образец с текстом начиная с заданной позиции.
    """
    pattern_position: int = 0
    text_length: int = len(text)
    pattern_length: int = len(pattern)

    while (
        start_position + pattern_position < text_length
        and text[start_position + pattern_position] == pattern[pattern_position]
    ):
        pattern_position += 1

        if pattern_position == pattern_length:
            return start_position

    return -1


def brute_force_search(text: str, pattern: str) -> int:
    """
    Ищет первое вхождение подстроки в тексте методом грубой силы.
    Возвращает индекс или -1, если совпадений нет.
    """
    text_length: int = len(text)
    pattern_length: int = len(pattern)

    if pattern_length == 0 or text_length == 0 or pattern_length > text_length:
        return -1

    for text_position in range(text_length - pattern_length + 1):
        if check_match_at_position(text, pattern, text_position) != -1:
            return text_position  # Возвращаем сразу первое найденное

    return -1
