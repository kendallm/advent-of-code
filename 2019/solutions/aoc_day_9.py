from collections import defaultdict, deque
from utils import Computer
from math import inf


def main():
    with open("../input/input_9.txt") as f:
        memory = f.readline()

    computer = Computer(memory, deque(), inf)
    computer._input.append("2")
    computer.run()
    print(computer._output)


if __name__ == "__main__":
    main()
