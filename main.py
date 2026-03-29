from BF import brute_force_find_all_occurrences
from KMP import kmp_search


def main():

    # Тестовые данные
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"

    print(f"Текст:     {text}")
    print(f"Образец:   {pattern}\n")

    # Brute Force
    bf_result = brute_force_find_all_occurrences(text, pattern)
    print("Brute Force:")
    print(f"   Позиции: {bf_result['positions']}")
    print(f"   Количество совпадений: {bf_result['count']}")
    print(f"   Коллизии: {bf_result['collisions']}\n")

    # KMP
    kmp_pos = kmp_search(pattern, text)
    print("KMP (поиск первого вхождения):")
    if kmp_pos != -1:
        print(f"   Найдено на позиции: {kmp_pos}")
    else:
        print("   Не найдено")

    # Проверка согласованности результатов
    if kmp_pos != -1 and kmp_pos in bf_result['positions']:
        print("\n Результаты обоих алгоритмов совпадают")
    elif kmp_pos == -1 and bf_result['count'] == 0:
        print("\n Результаты обоих алгоритмов совпадают (не найдено)")
    else:
        print("\n Результаты НЕ совпадают!")


if __name__ == "__main__":
    main()