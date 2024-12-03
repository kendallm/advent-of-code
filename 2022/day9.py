import dataclasses
import math
import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


@dataclasses.dataclass
class Movement:
    direction: str
    count: int


class RopeSimulation:
    def __init__(self, lines: list[str], num_knots: int):
        self.movements = self._parse_movements(lines)
        self.num_knots = num_knots

    def simulate(self) -> int:
        knots = [(0, 0) for _ in range(self.num_knots - 1)]
        head = (0, 0)
        seen = set()
        for move in self.movements:
            for count in range(move.count):
                head = self._move_head(head, move)
                start = head
                for i, knot in enumerate(knots):
                    tail = self._move_tail(start, knot)
                    start = tail
                    knots[i] = tail
                seen.add(start)
        return len(seen)

    def _parse_movements(self, lines: list[str]) -> list[Movement]:
        movements = []
        for line in lines:
            direction, count = line.split()
            movements.append(Movement(direction, int(count)))
        return movements

    def _move_head(self, head: (int, int), move: Movement) -> (int, int):
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
        return head

    def _move_tail(self, head: (int, int), tail: (int, int)) -> (int, int):
        hx, hy = head
        tx, ty = tail

        xdiff = int(math.dist([hx], [tx]))
        ydiff = int(math.dist([hy], [ty]))

        # Directly up or down
        if xdiff == 0 and ydiff == 2:
            return tx, ty - 1 if hy < ty else ty + 1

        # Directly left or right
        if xdiff == 2 and ydiff == 0:
            return tx - 1 if hx < tx else tx + 1, ty

        if (xdiff >= 2 and ydiff >= 1) or (xdiff >= 1 and ydiff >= 2):
            x = tx - 1 if hx < tx else tx + 1
            y = ty - 1 if hy < ty else ty + 1
            return x, y
        return tail


def main():
    lines = ProblemParser().load_input(2022, 9)
    sim = RopeSimulation(lines, 2)
    seen = sim.simulate()
    print(seen)

    sim = RopeSimulation(lines, 10)
    seen = sim.simulate()
    print(seen)


if __name__ == "__main__":
    main()
