from BF import brute_force_find_all_occurrences
from KMP import kmp_search


def main():

    # Тестовые данные
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"

    print(f"Текст:     {text}")
    print(f"Шаблон:   {pattern}\n")

    # Brute Force
    bf_result = brute_force_find_all_occurrences(text, pattern)
    print("Brute Force:")
    print(f"   Позиции: {bf_result['positions']}")

    # KMP
    kmp_pos = kmp_search(pattern, text)
    print("KMP (поиск первого вхождения):")
    if kmp_pos != -1:
        print(f"   Найдено на позиции: {kmp_pos}")
    else:
        print("   Не найдено")


if __name__ == "__main__":
    main()