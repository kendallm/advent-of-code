from collections import defaultdict
import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser

def build_rules(lines):
    rules = defaultdict(set)
    for line in lines:
        rule = line.split("|")
        rules[rule[0]].add(rule[1])

    return rules

def build_afters(lines):
    rules = defaultdict(set)
    for line in lines:
        rule = line.split("|")
        rules[rule[1]].add(rule[0])
    return rules

def is_valid(rules, update):
    reupdate = list(reversed(update))
    for i, v in enumerate(reupdate):
        for vj in reupdate[i+1:]:
            if v not in rules[vj]:
                return False

    return True

def fix(rules, update, afters):
    out = []
    reupdate = list(reversed(update))
    for i, v in enumerate(reupdate):
        for vj in reupdate[i+1:]:
            if v not in rules[vj]:
                out.append(v)
                break
    result = []
    for x in update:
        if x not in out:
            result.append(x)
        else:
            spot = find_spot(afters, result, x)
            result.insert(spot, x)
    return result

def find_spot(afters, update, value):
    spots = afters[value].intersection(set(update))
    if spots is None:
        return 0
    for i, v in enumerate(update):
        if len(spots) == 0:
            return i
        if v in spots:
            spots.remove(v)
    return i


def main():
    lines = ProblemParser().load_input(2024, 5)
    idx = lines.index("")
    rules = build_rules(lines[0:idx])
    updates = [x.split(',') for x in lines[idx+1:]]
    
    valids = [int(x[len(x)//2]) for x in updates if is_valid(rules, x)]
    invalids = [x for x in updates if not is_valid(rules, x)]
    print(sum(valids))

    afters = build_afters(lines[0:idx])
    print(afters)
    print(rules)
    valids = [fix(rules, update, afters) for update in invalids]
    print(valids)
    valids = [int(x[len(x)//2]) for x in valids]
    print(sum(valids))


if __name__ == '__main__':
    main()
