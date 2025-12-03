import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


def main():
    lines = ProblemParser().load_input(2025, 1)
    curr = 50
    counts = 0
    count_any = 0
    for line in lines:
        scalar = 1
        if line[0] == 'L':
            scalar = -1
        abs_rot = abs(int(line[1:]) )
        rot = abs_rot* scalar
        count_any += abs_rot // 100
        div = (abs_rot % 100) * scalar
        extra = div + curr
        if curr != 0 and extra < 1 or extra >= 100:
            count_any += 1
        curr = (curr + rot) % 100
        if curr == 0:
            counts += 1
    print(counts)
    print(count_any)

    curr = 50

if __name__ == '__main__':
    main()

# curr=84, rot=-212, times=3