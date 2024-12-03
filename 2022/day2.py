import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


lines = ProblemParser().load_input(2022, 2)

scores = {
    "A X": (4, 3),
    "A Y": (8, 4),
    "A Z": (3, 8),
    "B X": (1, 1),
    "B Y": (5, 5),
    "B Z": (9, 9),
    "C X": (7, 2),
    "C Y": (2, 6),
    "C Z": (6, 7),
}


def play_game():
    part1 = 0
    part2 = 0
    for line in lines:
        a, b = scores[line]
        part1 += a
        part2 += b
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


play_game()
