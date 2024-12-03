import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


class Elf:
    def __init__(self, sack: str):
        size = len(sack)
        mid = len(sack) // 2
        left, right = (sack[0:mid], sack[mid:size])
        lset = set(left)
        rset = set(right)
        self.left = lset
        self.right = rset
        self.full_sack = lset.union(rset)

    def get_common(self):
        return list(self.left.intersection(self.right))


def main():
    def calculate_priority(char):
        if char.islower():
            score = ord(char) - ord("a") + 1
        else:
            score = ord(char) - ord("A") + 27
        return score

    def part1(elves):
        print(sum([calculate_priority(e.get_common()[0]) for e in elves]))

    def part2(elves):
        groups = []
        for start_idx in range(0, len(elves), 3):
            a, b, c = elves[start_idx : start_idx + 3]
            group = a.full_sack.intersection(b.full_sack).intersection(c.full_sack)
            groups.append(list(group)[0])
        print(sum([calculate_priority(g) for g in groups]))

    elves = []
    for line in ProblemParser().load_input(2022, 3):
        elf = Elf(line)
        elves.append(elf)

    part1(elves)
    part2(elves)


if __name__ == "__main__":
    main()
