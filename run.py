from text import main as generate
from main import main as benchmark
from results import main as plot

if __name__ == "__main__":
    print("=== Шаг 1: Генерация данных ===")
    generate()
    print("\n=== Шаг 2: Бенчмарк ===")
    benchmark()
    print("\n=== Шаг 3: Построение графиков ===")
    plot()
    print("\nГотово!")
