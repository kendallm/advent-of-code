import copy
import re
import sys
from collections import defaultdict
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


prog = re.compile(r"^move (\d+) from (\d+) to (\d)$")


def parse_move(line: str) -> (int, int, int):
    result = prog.search(line)
    if result is None:
        raise Exception("No move found")
    return result.groups()


def parse_crates(line: str) -> dict:
    count = 0
    stacks = {}
    for i in range(0, len(line), 4):
        count += 1
        if line[i] == "[":
            crate = line[i + 1]
            stacks[count] = crate
    return stacks


def execute_move(move: (int, int, int), stacks: dict) -> dict:
    for _ in range(int(move[0])):
        crate = stacks[int(move[1])].pop()
        stacks[int(move[2])].append(crate)
    return stacks


def execute_move_grouped(move: (int, int, int), stacks: dict) -> dict:
    crates = stacks[int(move[1])][-int(move[0]) :]
    stacks[int(move[1])] = stacks[int(move[1])][: -int(move[0])]
    stacks[int(move[2])].extend(crates)

    return stacks


def parse_input(lines: str) -> (list, dict):
    stacks = defaultdict(list)
    parsed_crates = False
    moves = []
    for line in lines:
        if line.strip() == "":
            parsed_crates = True
            continue
        elif parsed_crates:
            move = parse_move(line)
            moves.append(move)
        else:
            crates = parse_crates(line)
            place_crates(crates, stacks)
    return moves, stacks


def place_crates(crates: dict, stacks: dict) -> None:
    for k, v in crates.items():
        stacks[k].insert(0, v)


def main():
    lines = ProblemParser().load_input(2022, 5, strip=False)
    moves, stacks = parse_input(lines)
    stacks_grouped = copy.deepcopy(stacks)

    for move in moves:
        stacks = execute_move(move, stacks)
        stacks_grouped = execute_move_grouped(move, stacks_grouped)

    for i in range(len(stacks)):
        print(f"{stacks[i + 1][-1]}", end="")
    print()

    for i in range(len(stacks_grouped)):
        print(f"{stacks_grouped[i + 1][-1]}", end="")
    print()


if __name__ == "__main__":
    main()
