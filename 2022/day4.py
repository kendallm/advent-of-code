from pathlib import Path
import sys

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

import dataclasses

from utils.get_inputs import ProblemParser


@dataclasses.dataclass
class Range:
    left: int
    right: int


def fully_contains(first, second):
    return (
        first.left <= second.left
        and first.right >= second.right
        or second.left <= first.left
        and second.right >= first.right
    )


def overlaps(first, second):
    return (
        first.left <= second.left
        and (first.right >= second.right or first.right >= second.left)
    ) or (
        second.left <= first.left
        and (second.right >= first.right or second.right >= first.left)
    )


def parse_range(item):
    a, b = item.split("-")
    return Range(int(a), int(b))


def main():
    lines = ProblemParser().load_input(2022, 4)
    ranges = []
    for line in lines:
        first, second = line.split(",")
        ranges.append(parse_range(first))
        ranges.append(parse_range(second))

    count = 0
    any_count = 0
    for i in range(0, len(ranges), 2):
        first = ranges[i]
        second = ranges[i + 1]
        if fully_contains(first, second):
            count += 1
        if overlaps(first, second):
            any_count += 1
    print(count)
    print(any_count)


if __name__ == "__main__":
    main()
