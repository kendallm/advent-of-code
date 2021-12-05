import sys
from collections import defaultdict
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser

lines = ProblemParser().load_input(2021, 5)


def parse_line(line):
    line = line.split(" -> ")
    x1, y1 = line[0].split(",")
    x2, y2 = line[1].split(",")
    return (int(x1), int(y1)), (int(x2), int(y2))


def part1():
    grid = defaultdict(int)
    for line in lines:
        start, end = parse_line(line)
        if start[0] == end[0]:
            # vertical
            first = min(start[1], end[1])
            second = max(start[1], end[1])
            for i in range(first, second + 1):
                grid[(start[0]), i] += 1
        elif start[1] == end[1]:
            # horizontal
            first = min(start[0], end[0])
            second = max(start[0], end[0])
            for i in range(first, second + 1):
                grid[i, (start[1])] += 1
    count = 0
    for v in grid.values():
        if v > 1:
            count += 1
    print(count)


def part2():
    grid = defaultdict(int)
    for line in lines:
        start, end = parse_line(line)
        if start[0] == end[0]:
            # vertical
            first = min(start[1], end[1])
            second = max(start[1], end[1])
            for y in range(first, second + 1):
                grid[(start[0], y)] += 1
        elif start[1] == end[1]:
            # horizontal
            first = min(start[0], end[0])
            second = max(start[0], end[0])
            for x in range(first, second + 1):
                grid[(x, start[1])] += 1
        else:
            # diagonal
            x = [start, end]
            x.sort()
            [start, end] = x
            if start[1] < end[1]:
                for x, y in zip(
                    range(start[0], end[0] + 1), range(start[1], end[1] + 1)
                ):
                    grid[(x, y)] += 1
            elif start[1] > end[1]:
                for x, y in zip(
                    range(start[0], end[0] + 1), reversed(range(end[1], start[1] + 1))
                ):
                    grid[(x, y)] += 1
    count = 0
    for v in grid.values():
        if v > 1:
            count += 1
    print(count)


part1()
part2()
