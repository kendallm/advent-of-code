import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


lines = ProblemParser().load_input(2022, 1)

count = 0
calories = []

for line in lines:
    if line == "":
        calories.append(count)
        count = 0
        continue
    c = int(line)
    count = count + c

calories.sort(reverse=True)

print(f"Part 1: {calories[0]}")
print(f"Part 2: {calories[0] + calories[1] + calories[2]}")
