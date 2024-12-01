import sys
from collections import Counter
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


def get_lists(lines):
    a, b = [], []
    for line in lines:
        items = line.split()
        a.append(int(items[0]))
        b.append(int(items[1]))
    a.sort()
    b.sort()
    return a, b


def main():
    lines = ProblemParser().load_input(2024, 1)
    a, b = get_lists(lines)
    dist = [abs(x - y) for x, y in zip(a, b)]
    print(sum(dist))

    # Part 2
    counts = Counter(b)
    similarity = [x * counts.get(x, 0) for x in a]
    print(sum(similarity))


if __name__ == '__main__':
    main()

