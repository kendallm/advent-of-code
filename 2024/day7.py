import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser

def parse_equation(line):
    left, right = line.split(":")
    result = int(left)
    vals = right.split()
    return result, [int(x) for x in vals]

def helper(result, acc, vals):
    if len(vals) == 0:
        return result == acc
    head = vals[0]
    tail = vals[1:]
    return helper(result, acc + head, tail) or helper(result, acc * head, tail)

def can_solve(result, vals):
    head = vals[0]
    tail = vals[1:]

    return helper(result, head, tail)

def helper_concat(result, acc, vals):
    if len(vals) == 0:
        return result == acc
    head = vals[0]
    tail = vals[1:]
    # can do this with math but lets see if string conv works fine, int(math.log10(abs(n))) + 1
    return helper_concat(result, acc + head, tail) or helper_concat(result, acc * head, tail) or helper_concat(result, int(f'{acc}{head}'), tail)

def can_solve_concat(result, vals):
    head = vals[0]
    tail = vals[1:]

    return helper_concat(result, head, tail)

def main():
    lines = ProblemParser().load_input(2024, 7)
    final = 0
    final_concat = 0
    for line in lines:
        result, vals = parse_equation(line)
        if can_solve(result, vals):
            final += result
        if can_solve_concat(result, vals):
            final_concat += result
    print(final, final_concat)


if __name__ == '__main__':
    main()
