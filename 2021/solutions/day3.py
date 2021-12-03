import sys
from collections import defaultdict
from pathlib import Path
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


lines = ProblemParser().load_input(2021, 3)

def count_bits_in_positions(in_lines):
    bits = defaultdict(int)
    for line in in_lines:
        for i, c in enumerate(line.strip()):
            if c == '1':
                bits[i] += 1
    return bits

def bit_string_to_int(bit_string):
    return int(bit_string, 2)

def part1():
    bits = count_bits_in_positions(lines)
    gamma = ""
    epsilon = ""
    keys = list(bits.keys())
    keys.sort()
    count = len(lines)
    for key in keys:
        zeros = count - bits[key]
        ones = bits[key]
        if zeros > ones:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    print("=== part 1 ====")
    print(bit_string_to_int(gamma) * bit_string_to_int(epsilon))

def find_most_common_in_position(bits, pos, count):
    zeros = count - bits[pos]
    ones = bits[pos]

    if ones >= zeros:
        return "1"
    return "0"

def part2():
    oxy = lines.copy()
    bits = count_bits_in_positions(oxy)
    pos = 0
    common = find_most_common_in_position(bits, pos, len(oxy))
    res = []
    for line in oxy:
        if line[pos] == common:
            res.append(line)
    while len(res) > 1:
        pos += 1
        oxy = res.copy()
        bits = count_bits_in_positions(oxy)
        common = find_most_common_in_position(bits, pos, len(oxy))

        res = []
        for line in oxy:
            if line[pos] == common:
                res.append(line)
    oxy = bit_string_to_int(res[0])

    co2 = lines.copy()
    bits = count_bits_in_positions(co2)
    pos = 0
    common = find_most_common_in_position(bits, pos, len(co2))
    res = []
    for line in co2:
        if line[pos] != common:
            res.append(line)
    while len(res) > 1:
        co2 = res.copy()
        bits = count_bits_in_positions(co2)
        pos += 1
        common = find_most_common_in_position(bits, pos, len(co2))
        res = []
        for line in co2:
            if line[pos] != common:
                res.append(line)
    co2 = bit_string_to_int(res[0])
    print("=== part 2 ====")
    print(oxy * co2)

part1()
part2()
