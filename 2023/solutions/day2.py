import sys
from functools import reduce

from pathlib import Path
from collections import defaultdict

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


class Game:
    def __init__(self):
        self.rounds = {}

    def load_round(self, line):
        id, moves = line.split(":")
        _, id = id.split(" ")
        id = int(id)
        moves = moves.split(";")
        moves = self.load_moves(moves)
        self.rounds[id] = moves

    def load_moves(self, moves):
        res = []
        for move in moves:
            move = move.strip()
            cubes = move.split(",")
            color_cubes = defaultdict(int)
            for cube in cubes:
                count, color = cube.split()
                color_cubes[color] = int(count)
            res.append(color_cubes)
        return res

    def min_powers(self):
        powers = []
        for _, round in self.rounds.items():
            min_cubes = [0, 0, 0]
            for move in round:
                red = move["red"]
                blue = move["blue"]
                green = move["green"]
                min_cubes[0] = max(min_cubes[0], red)
                min_cubes[1] = max(min_cubes[1], blue)
                min_cubes[2] = max(min_cubes[2], green)
            power = reduce(lambda x, y: x * y, min_cubes, 1)
            powers.append(power)
        return powers


def part2(g):
    powers = g.min_powers()
    print(sum(powers))


def part1(g):
    red = 12
    green = 13
    blue = 14

    ids = []
    for id, round in g.rounds.items():
        possible = True
        for move in round:
            if move["red"] > red or move["green"] > green or move["blue"] > blue:
                possible = False
                break
        if possible:
            ids.append(id)
    print(sum(ids))


def main():
    lines = ProblemParser().load_input(2023, 2)
    g = Game()
    for line in lines:
        g.load_round(line)
    part1(g)
    part2(g)


if __name__ == "__main__":
    main()
