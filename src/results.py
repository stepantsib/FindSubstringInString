import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

RESULTS_FILE = "../benchmark_results.csv"


def main():
    if not os.path.exists(RESULTS_FILE):
        print(f"Файл {RESULTS_FILE} не найден. Сначала проведите тестирование.")
        return

    df = pd.read_csv(RESULTS_FILE)

    # Получаем уникальные типы случаев: best, worst, random
    case_types = df["Case_Type"].unique()
    algorithms = df["Algorithm"].unique()

    colors = {"BF": "blue", "KMP": "red"}

    for case in case_types:
        plt.figure(figsize=(10, 6))

        # Фильтруем данные по конкретному случаю (best, worst, random)
        df_case = df[df["Case_Type"] == case]

        for algo in algorithms:
            df_algo = df_case[df_case["Algorithm"] == algo]
            if df_algo.empty:
                continue

            # Обязательно сортируем по размеру данных
            df_algo = df_algo.sort_values(by="Size")

            X = df_algo["Size"].values
            Y = df_algo["Avg_Time_sec"].values
            Delta = df_algo["Delta_sec"].values
            color = colors.get(algo, "green")

            # 1. Отрисовка экспериментальных точек с доверительными интервалами
            # linestyle='None' гарантирует, что точки не будут соединены ломаной линией!
            plt.errorbar(
                X,
                Y,
                yerr=Delta,
                fmt="o",
                color=color,
                ecolor=color,
                capsize=4,
                markersize=5,
                linestyle="None",
                label=f"{algo} ",
            )

            # 2. Аппроксимация результатов функцией
            # Так как длина искомого слова (pattern) у нас постоянная,
            # сложность алгоритмов зависит линейно от длины текста.
            # Используем линейную аппроксимацию: y = ax + b
            if len(X) > 1:
                # np.polyfit подбирает коэффициенты a и b
                coefficients = np.polyfit(X, Y, 1)
                poly_func = np.poly1d(coefficients)

                # Отрисовка линии аппроксимации
                plt.plot(
                    X,
                    poly_func(X),
                    color=color,
                    linestyle="--",
                    alpha=0.7,
                    label=f"{algo} (Аппроксимация O(N))",
                )

        plt.title(
            f"Сравнение производительности: {case.capitalize()} случай", fontsize=14
        )
        plt.xlabel("Размер текста (символов)", fontsize=12)
        plt.ylabel("Время работы (секунды)", fontsize=12)

        plt.grid(True, linestyle=":", alpha=0.7)
        plt.legend(loc="upper left")

        plt.xscale('log')

        filename = f"graph_{case}_case.png"
        plt.savefig(filename, dpi=300, bbox_inches="tight")
        plt.close()

        print(f"Сохранен график: {filename}")


if __name__ == "__main__":
    main()
