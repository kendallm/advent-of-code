from functools import reduce
import sys
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser

max_dist = 3

def get_reports(lines):
    reports = [[int(b) for b in a.split()] for a in lines]
    return reports

def verify_report(report, skip = None):
    inc, dec = False, False
    if skip == 0:
        start = 1
        skip = None
    else:
        start = 0
    prev = report[start]
    for i, curr in enumerate(report[start + 1:len(report)]):
        if skip is not None and i+1 == skip:
            continue
        if curr == prev:
            return False, i
        dist = abs(curr - prev)
        if (dist == 0 or dist > max_dist):
            return False, i
        
        if prev < curr:
            dec = True
        if prev > curr:
            inc = True

        if dec and inc:
            return False, i
        if inc and dec:
            return False, i
        prev = curr

    return True, -1
    
def verify_with_dampener(report):
    valid, idx = verify_report(report)
    if valid:
        return True
    for i in [idx, idx - 1, idx + 1]:
        valid, _ = verify_report(report, skip=i)
        if valid:
            return True
    return False


def main():
    lines = ProblemParser().load_input(2024, 2)

    reports = get_reports(lines)
    part1 = [verify_report(a) for a in reports]
    part1 = reduce(lambda x, y: x + 1 if y[0] is True else x, part1, 0)
    print(f"{part1=}")

    part2 = [verify_with_dampener(a) for a in reports]
    part2 = reduce(lambda x, y: x + 1 if y is True else x, part2, 0)
    print(f"{part2=}")


if __name__ == '__main__':
    main()
