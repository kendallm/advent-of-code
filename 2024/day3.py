import sys
import re
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser

def eval_mul(statement):
    matcher = re.compile(r'\d{1,3}')
    args = matcher.findall(statement)
    return int(args[0]) * int(args[1])

def evaluate(statements):
    do = True
    output = 0
    for statement in statements:
        ins = statement.split('(')[0]
        if ins == "mul":
            output +=  eval_mul(statement) if do else 0
            continue
        if ins == "do":
            do = True
            continue
        if ins == "don't":
            do = False
            continue
        raise(f"unexpected instruction in statement")
    return output

def parse(input, conditionals=False):
    matcher = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
    conditional_matcher = re.compile(r'(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))')
    if conditionals:
        return conditional_matcher.findall(input)
    return matcher.findall(input)

def main():
    lines = ProblemParser().load_input(2024, 3)
    program = " ".join(lines)
    print("part2", evaluate(parse(program)))
    print("part2", evaluate(parse(program, conditionals=True)))

if __name__ == '__main__':
    main()
