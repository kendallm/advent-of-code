import sys
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


lines = ProblemParser().load_input(2021, 1)
lines = [int(x) for x in lines]

prev = lines[0]
inc = 0
for x in lines:
    if x > prev:
        inc += 1
    prev = x
print(inc)

inc = 0
a = lines[0:3]
for x in range(len(lines)):
    # print(a)
    s1 = sum(a)
    b = lines[x : x + 3]
    if len(b) < 3:
        break
    s2 = sum(b)
    if s1 < s2:
        inc += 1
    a = b
print(inc)
