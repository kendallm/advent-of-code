import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


def parse_maps(lines):
    maps = []
    curr = []
    for line in lines:

        if line == '':
            maps.append(curr)
            curr = []
            continue
        if line[-1] == ':':
            continue
        dest, source, length = line.split()
        curr.append((int(source), int(dest), int(length)))
    maps.append(curr)
    return maps


def find_location(seed, maps):
    for m in maps:
        for (source, dest, length) in m:
            if source <= seed <= (source + length):
                seed = dest + (seed - source)
                break
    return seed

def main():
    lines = ProblemParser().load_input(2023, 5)
    seed_ranges = lines[0].split(" ")[1:]
    seed_ranges = [int(x) for x in seed_ranges]
    seeds = [seed_ranges[s:s+2] for s in range(0, len(seed_ranges), 2)]
    maps = parse_maps(lines[2:])
    locations = float("inf")
    for sr in seeds:
        print(sr)
        for n in range(sr[1]):
            seed = sr[0] + n
            location = find_location(seed, maps)
            locations = min(location, locations)
    print(locations)

if __name__ == '__main__':
    main()
