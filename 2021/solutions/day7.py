import sys
from pathlib import Path
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


lines = ProblemParser().load_input(2021, 7)
positions = lines[0]
# positions = "16,1,2,0,4,2,7,1,2,14"

positions = [int(x) for x in positions.split(",")]


def part1(positions):
    gas = [0 for _ in range(max(positions) + 1)]
    for i in range(len(gas)):
        acc = sum([i - x if i > x else x - i for x in positions])
        gas[i] = acc
    print(min(gas))

"""
Can also use @functools.cache but this seems to be a lot slower
Though the implementation does seem easier to read so may be worth it.

## Using functools.cache
python 2021/solutions/day7.py  7.92s user 0.05s system 99% cpu 7.976 total

## Using self implemented cache
python 2021/solutions/day7.py  0.34s user 0.02s system 98% cpu 0.362 total


@functools.cache
def compute_gas_for_diff(i, x):
    diff = i - x if i > x else x - i
    acc = sum(range(diff + 1))
    return acc


def part2(positions):
    gas = [0 for _ in range(max(positions) + 1)]
    for i in range(len(gas)):
        for x in positions:
            gas[i] += compute_gas_for_diff(i, x)

    print(min(gas))
"""
def part2(positions):
    gas = [0 for _ in range(max(positions) + 1)]
    cache = {}
    for i in range(len(gas)):
        acc = 0
        for x in positions:
            diff = i - x if i > x else x - i
            if diff not in cache:
                val = sum(range(diff + 1))
                cache[diff] = val
            acc += cache[diff]
        gas[i] = acc
    print(min(gas))


part1(positions)
part2(positions)