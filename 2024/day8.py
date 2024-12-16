import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


def main():
    lines = ProblemParser().load_input(2024, 8)

if __name__ == '__main__':
    main()
