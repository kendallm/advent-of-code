from functools import reduce
from collections import *
import pprint
import re


def deal(deck):
    deck.reverse()
    return deck


def cut(deck, n):       
    new_deck = deck[n:]
    new_deck.extend(deck[:n])
    return new_deck


def deal_with_inc(deck, n):
    new_deck = [0 for _ in range(len(deck))]
    for i, v in enumerate(deck):
        new_deck[(i * n) % len(deck)] = v
    return new_deck


def part1(instructions):
    deck = [i for i in range(10007)]
    for line in instructions:
        if "deal into new stack" in line:
            deck = deal(deck)
        elif "cut" in line:
            deck = cut(deck, int(re.search(r'-?\d+', line).group()))
        else:
            deck = deal_with_inc(deck, int(re.search(r'-?\d+', line).group()))
    print(f"Part 1: {deck.index(2019)}")                


def part2(instructions):
    position = 2020
    
    pass


def main():
    with open('../input/input_22.txt') as f:
        instructions = f.readlines()
    part1(instructions)                
    part2(instructions)


if __name__ == "__main__":
    main()