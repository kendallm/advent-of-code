import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


lines = ProblemParser().load_input(2021, 4)

numbers = lines[0]

lines = lines[2:]


class BingoCard(object):
    def __init__(self, numbers: list[str]):
        self.card = {}
        self.numbers = {}
        self._build_card(numbers)

    def _build_card(self, numbers: list[str]) -> None:
        for i, row in enumerate(numbers):
            row = row.split()
            for j, number in enumerate(row):
                number = int(number)
                self.card[(i, j)] = False
                self.numbers[number] = (i, j)

    def mark_number(self, number) -> None:
        if number in self.numbers:
            self.card[self.numbers[number]] = True

    def won(self) -> bool:
        return self._check_horizontal() or self._check_vertical()

    def _check_horizontal(self) -> bool:
        for i in range(5):
            col = True
            for j in range(5):
                col = col and self.card[(j, i)]
            if col:
                return True
        return False

    def _check_vertical(self) -> bool:
        for i in range(5):
            row = True
            for j in range(5):
                row = row and self.card[(i, j)]
            if row:
                return True
        return False

    def sum_unmarked_numbers(self) -> int:
        result = 0
        for number, pos in self.numbers.items():
            if not self.card[pos]:
                result += number
        return result


def parse_cards(cards: list[str]) -> list[BingoCard]:
    rows = []
    result = []
    for line in cards:
        if line == "":
            result.append(BingoCard(rows.copy()))
            rows = []
        else:
            rows.append(line)
    result.append(BingoCard(rows.copy()))
    return result


def part1():
    cards = parse_cards(lines)
    winner = False
    for number in numbers.split(","):
        number.strip()
        number = int(number.strip())
        for card in cards:
            card.mark_number(number)
            if card.won():
                # calculate score
                winner = True
                print(card.sum_unmarked_numbers() * number)
        if winner:
            return


def part2():
    cards = parse_cards(lines)
    winners = []
    winning_number = []
    for number in numbers.split(","):
        number.strip()
        number = int(number.strip())
        for card in cards:
            if card in winners:
                continue
            card.mark_number(number)
            if card.won():
                winners.append(card)
                winning_number.append(number)

    print(winners[-1].sum_unmarked_numbers() * winning_number[-1])


part1()
part2()
