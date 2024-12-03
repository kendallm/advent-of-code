import sys
from utils.get_inputs import ProblemParser

lines = ProblemParser().load_input(2020, 9)


lines = [int(x) for x in lines]


preamble = set()


def two_sum(target):
    for num in preamble:
        if target - num in preamble:
            return True
    return False


invalid = None
for i, v in enumerate(lines):
    if i < 25:
        preamble.add(v)
        continue
    if not two_sum(v):
        invalid = v
        print("Part1", v)
    preamble.remove(lines[i - 25])
    preamble.add(v)

size = 2

i = 0
done = False
while not done:
    if i == len(lines):
        i = 0
        size += 1
    if size == len(lines):
        sys.exit()
    nums = lines[i : i + size]
    if sum(nums) == invalid:
        list.sort(nums)
        print("Part 2", nums[0] + nums[-1])
        done = True
    i += 1
