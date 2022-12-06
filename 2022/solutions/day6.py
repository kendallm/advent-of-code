import sys
from collections import Counter
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


def find_start_of_packet(line):
    count = 0
    for i in range(len(line)):
        chars = line[i: i + 4]
        counter = Counter(chars)
        if len(counter.items()) == 4:
            return count + 4
        count += 1
    raise Exception("Start of packet not found")


def find_start_of_message(line):
    count = 0
    for i in range(len(line)):
        chars = line[i: i + 14]
        counter = Counter(chars)
        if len(counter.items()) == 14:
            return count + 14
        count += 1
    raise Exception("Start of message not found")


def main():
    lines = ProblemParser().load_input(2022, 6)
    line = lines[0]
    print(find_start_of_packet(line))
    print(find_start_of_message(line))



if __name__ == '__main__':
    main()
