import dataclasses
import sys
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser

@dataclasses.dataclass
class Movement:
    direction: str
    count: int


def parse_movements(lines: list[str]) -> list[Movement]:
    movements = []
    for line in lines:
        direction, count = line.split()
        movements.append(Movement(direction, int(count)))
    return movements


def move_tail(head, tail):
    hx, hy = head
    tx, ty = tail
    if abs(hx - tx) <= 1 and abs(hy - ty) <= 1:
        return tail
    elif abs(hx - tx) == 2 and hy == ty:
        if hx > tx:
            return tx + 1, hy
        return tx - 1, hy
    elif hx == tx and abs(hy - ty) == 2:
        if hy > ty:
            return hx, ty + 1
        return hx, ty - 1
    else:
        if abs(hx - tx) > abs(hy - ty):
            x = hx - 1 if hx > tx else hx + 1
            return x, hy
        y = hy + 1 if hy < ty else hy - 1
        return hx, y


def simulate(movements: list[Movement]) -> int:
    tail = (0, 0)
    head = (0, 0)
    seen = set()
    for move in movements:
        seen.add(tail)
        for count in range(move.count):
            x, y = head
            if move.direction == "R":
                x += 1
            elif move.direction == "L":
                x -= 1
            elif move.direction == "U":
                y -= 1
            elif move.direction == "D":
                y += 1
            else:
                raise Exception("Unknown direction")
            head = (x, y)
            tail = move_tail(head, tail)
            seen.add(tail)
    return len(seen)

def simulate_ten(movements: list[Movement]) -> int:
    knots = [(0, 0) for _ in range(9)]
    head = (0, 0)
    seen = set()
    for move in movements:
        for count in range(move.count):
            x, y = head
            if move.direction == "R":
                x += 1
            elif move.direction == "L":
                x -= 1
            elif move.direction == "U":
                y -= 1
            elif move.direction == "D":
                y += 1
            else:
                raise Exception("Unknown direction")
            head = (x, y)
            start = head
            for i, knot in enumerate(knots):
                tail = move_tail(start, knot)
                start = tail
                knots[i] = start
            seen.add(knots[-1])
    return len(seen)


def main():
    lines = ProblemParser().load_input(2022, 9)
    movements = parse_movements(lines)
    seen = simulate(movements)
    print(seen)
    seen = simulate_ten(movements)
    print(seen, "real", 2514)


if __name__ == '__main__':
    main()
