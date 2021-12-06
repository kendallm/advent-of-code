import sys
from collections import defaultdict
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser

lines = ProblemParser().load_input(2021, 6)

line = lines[0]
line = line.split(",")

fish = [int(x) for x in line]

day_fish = [0 for _ in range(9)]
for f in fish:
    day_fish[f] += 1


def loop(x, fish):
    children = 0
    for n in range(x):
        for i in range(len(fish)):
            fish[i] -= 1
            if fish[i] < 0:
                if i == 0:
                    children += 1
                    print(n + 1, children)
                fish.append(8)
                fish[i] = 6
    return fish, children


def solver(day_fish, days):
    for _ in range(days):
        temp = [0 for _ in range(9)]
        for life, count in enumerate(day_fish):
            if life == 0:
                temp[8] += count
                temp[6] += count
            else:
                temp[life - 1] += count
        day_fish = temp
    print(sum(day_fish))


solver(day_fish.copy(), 80)
solver(day_fish.copy(), 256)
