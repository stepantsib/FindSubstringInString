def check_match_at_position(text: str, pattern: str, start_position: int) -> int:
    """
    Проверяет, совпадает ли образец с текстом начиная с заданной позиции.
    """
    pattern_position: int = 0
    text_length: int = len(text)
    pattern_length: int = len(pattern)

    while start_position + pattern_position < text_length and \
            text[start_position + pattern_position] == pattern[pattern_position]:
        pattern_position += 1

        if pattern_position == pattern_length:
            return start_position

    return -1


def brute_force_find_all_occurrences(text: str, pattern: str) -> dict:
    """
    Ищет все вхождения подстроки в тексте методом грубой силы.
    """
    found_positions: list = []
    text_length: int = len(text)
    pattern_length: int = len(pattern)

    for text_position in range(text_length - pattern_length + 1):
        if check_match_at_position(text, pattern, text_position) != -1:
            found_positions.append(text_position)

    return {
        "positions": found_positions
    }