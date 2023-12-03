import sys
from collections import defaultdict
from functools import reduce
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


def build_sight_lines(lines: list[str]):
    sight_lines = defaultdict(list)
    width = len(lines)
    length = len(lines[0])
    for x in range(width):
        for y in range(length):
            coord = (x, y, lines[x][y])
            for z in range(length):
                spot = (x, z, lines[x][z])
                if spot != coord:
                    sight_lines[coord].append(spot)
            for z in range(width):
                spot = (z, y, lines[z][y])
                if spot != coord:
                    sight_lines[coord].append(spot)
    return sight_lines


def count_flags(items):
    if len(items) == 0:
        return 0
    count = 0
    i = 0
    v = False
    for i, v in enumerate(items):
        if v:
            count += 1
        else:
            break
    if i == len(items) - 1 and v:
        return count
    return count + 1


def main():
    lines = ProblemParser().load_input(2022, 8)
    count = 0
    sight_lines = build_sight_lines(lines)

    # part 1
    for k, v in sight_lines.items():
        if k[0] == 0 or k[0] == len(lines) - 1:
            count += 1
            continue
        if k[1] == 0 or k[1] == len(lines[0]) - 1:
            count += 1
            continue
        x = [a[2] for a in v]
        x = [int(a[2]) < int(k[2]) for a in v if a[0] < k[0] and a[1] == k[1]]
        if all(x):
            count += 1
            continue
        x = [int(a[2]) < int(k[2]) for a in v if a[0] > k[0] and a[1] == k[1]]
        if all(x):
            count += 1
            continue
        x = [int(a[2]) < int(k[2]) for a in v if a[0] == k[0] and a[1] < k[1]]
        if all(x):
            count += 1
            continue
        x = [int(a[2]) < int(k[2]) for a in v if a[0] == k[0] and a[1] > k[1]]
        if all(x):
            count += 1
            continue
    print(count)

    # part 2
    result = 0
    for k, v in sight_lines.items():
        count = 1
        up = [int(a[2]) < int(k[2]) for a in v if a[0] < k[0] and a[1] == k[1]]
        up.reverse()
        if len(up) > 0:
            count *= count_flags(up)

        down = [int(a[2]) < int(k[2]) for a in v if a[0] > k[0] and a[1] == k[1]]
        if len(down) > 0:
            count *= count_flags(down)

        left = [int(a[2]) < int(k[2]) for a in v if a[0] == k[0] and a[1] < k[1]]
        left.reverse()
        if len(left) > 0:
            count *= count_flags(left)

        right = [int(a[2]) < int(k[2]) for a in v if a[0] == k[0] and a[1] > k[1]]
        if len(right) > 0:
            count *= count_flags(right)
        result = max(result, count)
    print(result)


if __name__ == "__main__":
    main()
