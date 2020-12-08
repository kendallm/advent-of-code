from functools import reduce
from collections import defaultdict
trees = defaultdict(lambda: False)
depth = 0
width = 0

with open('day3.txt') as f:
    lines = f.readlines()
    depth = len(lines)
    width = len(lines[0]) - 1
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '#':
                trees[(j, i)] = True


slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

trees_on_slopes = []
for slope in slopes:
    x = 0
    spots = []
    count = 0
    for i in range(slope[1], depth, slope[1]):
        x = (x + slope[0]) % width
        y = i
        spots.append((x, y))
        if(trees[(x,y)]):
            count += 1
    print(f"Slope: {slope}, trees: {count}")
    trees_on_slopes.append(count)

print(reduce((lambda x,y: x * y), trees_on_slopes))