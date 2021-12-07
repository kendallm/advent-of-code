import sys
from pathlib import Path
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


lines = ProblemParser().load_input(2021, 7)
lines = lines[0]
# lines = "16,1,2,0,4,2,7,1,2,14"

lines = [int(x) for x in lines.split(",")]


def part1(lines):
    gas = [0 for _ in range(max(lines) + 1)]
    for i in range(len(gas)):
        acc = sum([i - x if i > x else x - i for x in lines])
        gas[i] = acc
    print(min(gas))

def part2(lines):
    gas = [0 for _ in range(max(lines) + 1)]
    cache = {}
    for i in range(len(gas)):
        acc = 0
        for x in lines:
            diff = i - x if i > x else x - i
            if diff not in cache:
                val = sum(range(diff + 1))
                cache[diff] = val
            acc += cache[diff]
        gas[i] = acc
    print(min(gas))


part1(lines)
part2(lines)