import os
import time
import math
import csv
from BF import brute_force_search
from KMP import kmp_search


DATA_DIR = "../benchmark_data"
RESULTS_FILE = "../benchmark_results.csv"


N_RUNS = 11
N_WARMUP = 3
T_STUDENT = 2.2281


def measure_algorithm(func, text, pattern) -> tuple[float, float]:
    """
    Выполняет замеры времени работы алгоритма и возвращает (среднее_время, дельта).
    """
    for _ in range(N_WARMUP):
        func(text, pattern)

    times = []

    for _ in range(N_RUNS):
        start_time = time.perf_counter()
        func(text, pattern)
        end_time = time.perf_counter()

        times.append(end_time - start_time)

    # Вычисление среднего времени
    avg_time = sum(times) / N_RUNS

    # Вычисление стандартного отклонения
    variance = sum((t - avg_time) ** 2 for t in times) / (N_RUNS - 1)
    s = math.sqrt(variance)

    # Вычисление доверительного интервала
    delta = T_STUDENT * (s / math.sqrt(N_RUNS))

    return avg_time, delta


def main():
    if not os.path.isdir(DATA_DIR):
        print(f"Папка {DATA_DIR} не найдена. Сначала запустите text.py")
        return

    print("Начинаем тестирование. Это может занять некоторое время...")

    with open(RESULTS_FILE, mode="w", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Size", "Case_Type", "Algorithm", "Avg_Time_sec", "Delta_sec"])

        def folder_sort_key(name):
            parts = name.split("_", 1)
            return int(parts[0]) if parts[0].isdigit() else 0

        for folder in sorted(os.listdir(DATA_DIR), key=folder_sort_key):
            fpath = os.path.join(DATA_DIR, folder)
            if not os.path.isdir(fpath):
                continue

            parts = folder.split("_", 1)
            if len(parts) != 2:
                continue

            size_str, case_type = parts[0], parts[1]
            size = int(size_str)

            with open(os.path.join(fpath, "text.txt"), "r", encoding="utf-8") as f:
                text = f.read()
            with open(os.path.join(fpath, "pattern.txt"), "r", encoding="utf-8") as f:
                pattern = f.read()

            print(
                f"Тестируем: Размер = {size:>10}, Случай = {case_type:<7} ",
                end="",
                flush=True,
            )

            bf_avg, bf_delta = measure_algorithm(brute_force_search, text, pattern)
            writer.writerow([size, case_type, "BF", f"{bf_avg:.6f}", f"{bf_delta:.6f}"])
            print(".", end="", flush=True)

            kmp_avg, kmp_delta = measure_algorithm(kmp_search, text, pattern)
            writer.writerow(
                [size, case_type, "KMP", f"{kmp_avg:.6f}", f"{kmp_delta:.6f}"]
            )
            print(". Готово.")

    print(f"\nТестирование завершено! Результаты сохранены в файл: {RESULTS_FILE}")


if __name__ == "__main__":
    main()
