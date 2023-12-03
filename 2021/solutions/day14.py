import sys
from collections import Counter
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


lines = ProblemParser().load_input(2021, 14)


default_template = lines[0]

rules = {}

for line in lines[2 : len(lines)]:
    part = line.split(" -> ")
    rules[part[0]] = part[1]


print(default_template)


def part1():
    template = default_template
    updated_template = []
    for n in range(10):
        print(n)
        for i in range(len(template) - 1):
            base = template[i : i + 2]
            base = rules[base]
            updated_template.append(base)
        updated_template.append(template[-1])
        template = "".join(updated_template)
        updated_template = []

    c = Counter(template)
    counts = c.most_common(len(c))
    print(counts)
    print(counts[0][1] - counts[-1][1])


def part2():
    template = default_template
    n = 2**40
    print(n)
    updated_template = ["" for _ in range(len(template) * n - n + 1)]
    print(len(updated_template))
    # for n in range(40):
    #     print(f"{n=}")
    #     # for i in range(len(template) - 1):
    #     #     base = template[i: i+2]
    #     #     updated_template[2 * i + 1] = rules[base]
    #     template = "".join(updated_template)
    #     # updated_template = [template[i // 2] for i in range(2 * len(template) - 1)]
    #     updated_template = [template[i // 2] for i in range(2 * len(template) - 1)]
    # c = Counter(template)
    # counts = c.most_common(len(c))
    # print(counts)
    # print(counts[0][1] - counts[-1][1])


# part1()
part2()
