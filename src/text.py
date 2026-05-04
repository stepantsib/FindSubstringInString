import os
import random
import string
from pathlib import Path

SIZES = [
    1_024,
    3_072,
    10_240,
    32_768,
    102_400,
    307_200,
    1_048_576,
    2_097_152,
    4_194_304,
    8_388_608,
    10_485_760,
    16_777_216,
    20_971_520,
]
PATTERN_LEN = 1000

ROOT = Path(__file__).parent.parent

DATA_DIR = str(ROOT / "benchmark_data")
RESULTS_FILE = str(ROOT / "benchmark_results.csv")


def save_case(size: int, case_type: str, text: str, pattern: str):
    folder = os.path.join(DATA_DIR, f"{size}_{case_type}")
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "text.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    with open(os.path.join(folder, "pattern.txt"), "w", encoding="utf-8") as f:
        f.write(pattern)


def main():
    os.makedirs(DATA_DIR, exist_ok=True)
    chars = string.ascii_letters + string.digits + string.punctuation

    for size in SIZES:
        # Лучший случай
        save_case(size, "best", "B" * size, "A" * PATTERN_LEN)
        # Худший случай
        save_case(size, "worst", "A" * size, "A" * (PATTERN_LEN - 1) + "B")
        # Случайный случай
        text_list = random.choices(chars, k=size)
        pattern = "".join(random.choices(chars, k=PATTERN_LEN))
        text_list[-PATTERN_LEN:] = list(pattern)
        save_case(size, "random", "".join(text_list), pattern)


if __name__ == "__main__":
    main()
