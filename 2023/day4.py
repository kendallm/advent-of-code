import math
import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


def main():
    lines = ProblemParser().load_input(2023, 4)
    part1(lines)
    part2(lines)


def part1(lines):
    scores = []
    for line in lines:
        _, card = line.split(":")
        mine, theirs = card.split("|")
        score = wins(mine, theirs)
        if score > 0:
            score = math.pow(2, score - 1)
            scores.append(score)
    print(sum(scores))


def part2(lines):
    counts = []
    cards = []
    for line in lines:
        _, card = line.split(":")
        counts.append(1)
        cards.append(card)
    for i, card in enumerate(cards):
        mine, theirs = card.split("|")
        for c in range(wins(mine, theirs)):
            counts[i + c + 1] += counts[i]
    print(sum(counts))


def wins(mine, theirs):
    my_nums = {}
    for num in mine.split():
        num = int(num.strip())
        my_nums[num] = True
    their_nums = {}
    for num in theirs.split():
        num = int(num.strip())
        their_nums[num] = True
    score = 0
    for k in my_nums.keys():
        if k in their_nums:
            score += 1
    return score


if __name__ == "__main__":
    main()
