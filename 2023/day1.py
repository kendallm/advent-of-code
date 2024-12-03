import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser

word_digit = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def main():
    lines = ProblemParser().load_input(2023, 1)
    # part_one(lines)
    part_two(lines)


def first_word_digit(line: str) -> (int, int):
    first, first_idx = None, None
    for x in range(len(line)):
        for k, v in word_digit.items():
            if k in str(line[x : x + 5]):
                if first is None:
                    first = v
                    first_idx = line.find(k)
    return first, first_idx


def last_word_digit(line: str) -> (int, int):
    highest = float("-inf")
    digit = -1
    for k, v in word_digit.items():
        if k in line:
            pos = line.rfind(k)
            highest = max(highest, pos)
            if highest == pos:
                digit = v
    if highest < 0:
        return None, None
    return digit, highest


def first_digit(line: str) -> (int, int):
    for i, x in enumerate(line):
        if x.isdigit():
            return int(x), i
    return None, None


def last_digit(line: str) -> (int, int):
    a, b = first_digit("".join(reversed(line)))
    if a is None:
        return a, b
    return a, len(line) - b - 1


def part_two(lines: list[str]) -> None:
    result = 0
    for line in lines:
        first, first_idx = first_digit(line)
        last, last_idx = last_digit(line)
        first_w, first_w_idx = first_word_digit(line)
        last_w, last_w_idx = last_word_digit(line)
        if first is None:
            first, first_idx = first_w, first_w_idx
        if last is None:
            last, last_idx = last_w, last_w_idx
        if first_w is None:
            first_w, first_w_idx = first, first_idx
        if last_w is None:
            last_w, last_w_idx = last, last_idx

        if first_w_idx < first_idx:
            first = first_w
        if last_w_idx > last_idx:
            last = last_w
        num = first * 10 + last
        result += num
    print(result)


def part_one(lines: str) -> None:
    result = 0
    for line in lines:
        first, first_idx = first_digit(line)
        last, last_idx = last_digit(line)
        num = first * 10 + last
        result += num
    print(result)


if __name__ == "__main__":
    main()
