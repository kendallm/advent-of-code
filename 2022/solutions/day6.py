import sys
from collections import Counter
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


def find_start_of_packet(line: str) -> int:
    return count_until_unique(line, 4)


def find_start_of_message(line: str) -> int:
    return count_until_unique(line, 14)


def count_until_unique(line: str, num_unique: int) -> int:
    count = 0
    for i in range(len(line)):
        chars = line[i : i + num_unique]
        counter = Counter(chars)
        if len(counter.items()) == num_unique:
            return count + num_unique
        count += 1
    raise Exception(f"unable to find {num_unique} chars")


def main():
    lines = ProblemParser().load_input(2022, 6)
    line = lines[0]
    print(find_start_of_packet(line))
    print(find_start_of_message(line))


if __name__ == "__main__":
    main()
