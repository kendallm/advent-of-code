import sys
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


class Monkey:

    def __init__(self):
        self.items = []
        self.test = 0
        self.operation = []
        self.true = 0
        self.false = 0

    def set_items(self, items):
        self.items = items

    def set_test(self, test):
        self.test = int(test)

    def set_operation(self, operation):
        self.operation = operation

    def set_true(self, idx):
        self.true = idx

    def set_false(self, idx):
        self.false = idx

    def __repr__(self):
        return f"""Monkey: 
    items={self.items}, 
    test={self.test},
    op={self.operation}, 
    true={self.true}, 
    false={self.false}\n"""


class Game:

    def __init__(self, lines):
        self.monkeys = self.parse_monkeys(lines)
        self.all_mods = 1
        for monkey in self.monkeys:
            self.all_mods *= monkey.test

    def parse_monkeys(self, lines):
        monkeys = []
        current = Monkey()
        for line in lines:
            if line == "":
                monkeys.append(current)
                current = Monkey()
                continue
            desc, value = line.split(":")
            if value == "":
                continue
            if desc == "Starting items":
                value = value.strip()
                items = [int(x) for x in value.split(",")]
                current.set_items(items)
            elif desc == "Operation":
                current.set_operation(value.split("=")[1].strip().split(" "))
            elif desc == "Test":
                value = value.split()
                current.set_test(value[2])
            elif desc == "If true":
                idx = int(value.split(" ")[-1])
                current.set_true(idx)
            elif desc == "If false":
                idx = int(value.split(" ")[-1])
                current.set_false(idx)
        monkeys.append(current)
        return monkeys

    def play_round(self):
        inspections = []
        for _, monkey in enumerate(self.monkeys):
            inspections.append(len(monkey.items))
            for i, item in enumerate(monkey.items):
                new = self.execute_operation(monkey.operation, item)
                new = new // 3
                if new % monkey.test == 0:
                    self.monkeys[monkey.true].items.append(new)
                else:
                    self.monkeys[monkey.false].items.append(new)
                monkey.items = []
        return inspections

    def play_round_without_worry(self):
        inspections = []
        for _, monkey in enumerate(self.monkeys):
            inspections.append(len(monkey.items))
            for i, item in enumerate(monkey.items):
                new = self.execute_operation(monkey.operation, item)
                new = new % self.all_mods
                if new % monkey.test == 0:
                    self.monkeys[monkey.true].items.append(new)
                else:
                    self.monkeys[monkey.false].items.append(new)
                monkey.items = []
        return inspections

    def execute_operation(self, operation, old):
        lhs, op, rhs = operation
        if lhs == "old":
            lhs = old
        else:
            lhs = int(lhs)

        if rhs == "old":
            rhs = old
        else:
            rhs = int(rhs)
        if op == "*":
            return lhs * rhs
        if op == "+":
            return lhs + rhs
        raise Exception("Unknown op")


def main():
    lines = ProblemParser().load_input(2022, 11)
    game = Game(lines)
    game2 = Game(lines)
    rounds = 20
    total = [0 for _ in range(len(game.monkeys))]
    for _ in range(rounds):
        inspections = game.play_round()
        total = [a + b for a, b in zip(total, inspections)]

    rounds = 10000
    total = [0 for _ in range(len(game2.monkeys))]
    for i in range(rounds):
        inspections = game2.play_round_without_worry()
        total = [a + b for a, b in zip(total, inspections)]
    total.sort(key=lambda x: -x)
    print(total[0] * total[1])


if __name__ == '__main__':
    main()
