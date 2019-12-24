from functools import reduce
from collections import *
import pprint

def should_die(pos, grid):
    adjceent = []
    adjceent.append((pos[0], pos[1] +  1))
    adjceent.append((pos[0], pos[1] - 1))
    adjceent.append((pos[0] + 1, pos[1]))
    adjceent.append((pos[0] - 1, pos[1]))
    vals = []
    for i in range(4):
        try:
            vals.append(grid[adjceent[i]])
        except:
            pass
    c = Counter(vals)
    return c[True] != 1

def should_infest(pos, grid):
    adjceent = []
    adjceent.append((pos[0], pos[1] +  1))
    adjceent.append((pos[0], pos[1] - 1))
    adjceent.append((pos[0] + 1, pos[1]))
    adjceent.append((pos[0] - 1, pos[1]))
    vals = []
    for i in range(5):
        try:
            vals.append(grid[adjceent[i]])
        except:
            pass
    c = Counter(vals)
    print(c)
    return c[True] == 1 or c[True] == 2


def tick(grid):
    grid_c = {}
    for spot in grid:
        if grid[spot]:
            grid_c[spot] = not should_die(spot, grid)
        else:
            grid_c[spot] = should_infest(spot, grid)
    return grid_c

def calculate_diversity(grid):
    power = 0
    diversity = 0
    
    for spot in grid:
        if grid[spot]:
            diversity += (2**power)
        power += 1
    return diversity


def main():
    pp = pprint.PrettyPrinter()
    seen = set()
    grid = {}
    with open('../input/input_24.txt') as f:
        y = 0
        for line in f:
            for i, v in enumerate(line.strip()):
                grid[(y, i)] = v =='#'
            y += 1   
    iters = 0
    seen.add(calculate_diversity(grid))

    
    while(True): 
        if iters < 4:
            print(grid)
            print()
        grid = tick(grid)
        diversity = calculate_diversity(grid)
        if diversity in seen:
            break
        else:
            seen.add(diversity)
        iters += 1
    print(grid)
    print(diversity)


if __name__ == "__main__":
    main()