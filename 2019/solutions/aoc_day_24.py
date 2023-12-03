from functools import reduce
from collections import *
import pprint


def should_die(pos, grid):
    adjceent = []
    adjceent.append((pos[0], pos[1] + 1))
    adjceent.append((pos[0], pos[1] - 1))
    adjceent.append((pos[0] + 1, pos[1]))
    adjceent.append((pos[0] - 1, pos[1]))
    vals = []
    for item in adjceent:
        vals.append(grid[item])
    c = Counter(vals)
    return c[True] != 1


def should_infest(pos, grid):
    adjceent = []
    adjceent.append((pos[0], pos[1] + 1))
    adjceent.append((pos[0], pos[1] - 1))
    adjceent.append((pos[0] + 1, pos[1]))
    adjceent.append((pos[0] - 1, pos[1]))
    vals = []
    for item in adjceent:
        vals.append(grid[item])
    c = Counter(vals)
    return c[True] == 1 or c[True] == 2


def tick(grid):
    grid_c = defaultdict(lambda: False)
    old_keys = set(grid)
    for spot in old_keys:
        if grid[spot]:
            grid_c[spot] = not should_die(spot, grid)
        else:
            grid_c[spot] = should_infest(spot, grid)
    for spot in set(grid).difference(old_keys):
        grid_c[spot] = grid[spot]
    return grid_c


def calculate_diversity(grid):
    power = 0
    diversity = 0

    for spot in grid:
        if grid[spot]:
            diversity += 2**power
        power += 1
    return diversity


def main():
    pp = pprint.PrettyPrinter()
    seen = set()
    grid = defaultdict(lambda: False)
    with open("../input/input_24.txt") as f:
        y = 0
        for line in f:
            for i, v in enumerate(line.strip()):
                grid[(y, i)] = v == "#"
            y += 1
    iters = 0
    seen.add(calculate_diversity(grid))

    # while(True):
    #     grid = tick(grid)
    #     diversity = calculate_diversity(grid)
    #     if diversity in seen:
    #         break
    #     else:
    #         seen.add(diversity)
    #     iters += 1
    for i in range(10):
        grid = tick(grid)
    c = Counter(grid.values())
    print(i)
    print(c[True])


if __name__ == "__main__":
    main()
