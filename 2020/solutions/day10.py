from collections import defaultdict, deque, namedtuple
from functools import lru_cache

import sys
from typing import DefaultDict, Deque
from utils.get_inputs import ProblemParser
from pprint import pprint

lines = ProblemParser().load_input(2020, 10)

lines = [int(x) for x in lines]
list.sort(lines)
lines.append(lines[-1] + 3)
lines.insert(0, 0)

diffs = DefaultDict(int)

i = 1
while i < len(lines):
    diffs[lines[i] - lines[i - 1]] = diffs[lines[i] - lines[i - 1]] + 1
    i += 1
print(diffs[1] * diffs[3])
print("Part 2\n")


def dp():
    t = [0 for _ in range(max(lines) + 1)]
    i = 1

    t[0] = 1
    if 1 in lines:
        t[1] = 1
    if 2 in lines:
        t[2] = t[1] + 1
    i = 2
    if 3 in lines:
        t[3] = t[2] + 1
        i = 3
    while i < len(lines):
        jolts = lines[i]
        t[jolts] = t[jolts - 3] + t[jolts - 2] + t[jolts - 1]
        i += 1
    return t[-1]


print(dp())
