import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


lines = ProblemParser().load_input(2021, 2)


def parse_line(line):
    l = line.split(" ")
    direction = l[0]
    dist = int(l[1])
    return direction, dist


def part1():
    position = 0
    depth = 0

    for line in lines:
        direction, dist = parse_line(line)
        if direction == "forward":
            position += dist
        elif direction == "down":
            depth += dist
        else:
            depth -= dist

    print(position * depth)


def part2():
    position = 0
    depth = 0
    aim = 0

    for line in lines:
        direction, dist = parse_line(line)
        if direction == "forward":
            position += dist
            depth += aim * dist
        elif direction == "down":
            aim += dist
        else:
            aim -= dist

    print(position * depth)


part1()
part2()
