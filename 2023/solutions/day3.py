import sys
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser
from utils.grid import Grid


def part1(lines):
    grid = parse_grid(lines)
    nums = []
    ratios = []
    for k, v in grid.items():
        if not v.isdigit() and not v == ".":
            nums_for_c = []
            neighbors = grid.get_neighbor_coordinates(k)
            for coord in neighbors:
                num, end = get_number(coord, grid)
                if num is not None:
                    nums_for_c.append((num, end))
            nums_for_c = list(set(nums_for_c))
            if is_gear(v, nums_for_c):
                ratio = nums_for_c[0][0] * nums_for_c[1][0]
                ratios.append(ratio)
            nums.extend(nums_for_c)
    print(sum([x for x, _ in nums]))
    print(sum(ratios))


def is_gear(c, nums):
    return c == "*" and len(nums) == 2


def get_number(pos, grid):
    c = grid.get(pos)
    if c.isdigit():
        start = pos[0]
        y = pos[1]
        num = ""
        while grid.contains((start, y)) and grid.get((start, y)).isdigit():
            start -= 1
        start += 1
        while grid.contains((start, y)) and grid.get((start, y)).isdigit():
            num += grid.get((start, y))
            start += 1
        return int(num), start
    return None, None


def parse_grid(lines):
    grid = Grid(lambda: ".")
    y = 0
    for line in lines:
        x = 0
        for c in line:
            grid.put((x, y), c)
            x += 1
        y += 1
    return grid


def main():
    lines = ProblemParser().load_input(2023, 3)
    part1(lines)


if __name__ == "__main__":
    main()
