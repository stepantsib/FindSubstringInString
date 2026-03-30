def compute_prefix_function(pattern: str) -> list:
    """
    Вычисляет префикс-функцию для алгоритма КМП.
    """
    pattern_length: int = len(pattern)
    prefix_table: list = [0] * pattern_length
    matched_length: int = 0

    for current_position in range(1, pattern_length):
        while matched_length > 0 and pattern[matched_length] != pattern[current_position]:
            matched_length = prefix_table[matched_length - 1]

        if pattern[matched_length] == pattern[current_position]:
            matched_length += 1

        prefix_table[current_position] = matched_length

    return prefix_table


def kmp_search(pattern: str, text: str) -> int:
    """
    Ищет первое вхождение подстроки в тексте с помощью алгоритма КМП.
    """
    pattern_length: int = len(pattern)
    text_length: int = len(text)

    if pattern_length == 0 or text_length == 0 or pattern_length > text_length:
        return -1

    prefix_table: list = compute_prefix_function(pattern)
    matched_length: int = 0

    for text_position in range(text_length):
        while matched_length > 0 and pattern[matched_length] != text[text_position]:
            matched_length = prefix_table[matched_length - 1]

        if pattern[matched_length] == text[text_position]:
            matched_length += 1

        if matched_length == pattern_length:
            match_index: int = text_position - pattern_length + 1
            return match_index

    return -1