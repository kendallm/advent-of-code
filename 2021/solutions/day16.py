import sys
from collections import namedtuple
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


Packet = namedtuple(
    "Packet",
    ["version", "type_id", "sub_packets", "length_id", "length", "val", "operation"],
)

lines = ProblemParser().load_input(2021, 16)
binary = ""

for c in lines[0]:
    binary += format(int(c, 16), "004b")


def decode_header(binary, start):
    version = int(binary[start : start + 3], 2)
    type_id = int(binary[start + 3 : start + 6], 2)
    return version, type_id


def decode(binary, start) -> Packet:
    version, type_id = decode_header(binary, start)
    sub_packets = []
    length_type_id = None
    length = 6
    val = ""
    if type_id == 4:
        # Literal
        i = start + 6
        while binary[i] == "1":
            val += binary[i + 1 : i + 5]
            length += 5
            i += 5
        val += binary[i + 1 : i + 5]
        length += 5
        i += 5
    else:
        length_type_id = int(binary[start + 6], 2)
        length += 1
        if length_type_id == 0:
            # total length in bits
            sub_length = int(binary[start + 7 : start + 7 + 15], 2)
            length += 15 + sub_length
            total = 0
            while sub_length > total:
                sub_packets.append(decode(binary, start + 7 + 15 + total))
                total += sub_packets[-1].length
        elif length_type_id == 1:
            num_sub_packets = int(binary[start + 7 : start + 7 + 11], 2)
            length += 11
            start = start + 7 + 11
            for i in range(num_sub_packets):
                sub_packets.append(decode(binary, start))
                length += sub_packets[-1].length
                start += sub_packets[-1].length
    op = decode_op(type_id)
    return Packet(version, type_id, sub_packets, length_type_id, length, val, op)


def decode_op(type_id):
    op = "LITERAL"
    if type_id == 0:
        op = "SUM"
    elif type_id == 1:
        op = "PRODUCT"
    elif type_id == 2:
        op = "MINIMUM"
    elif type_id == 3:
        op = "MAXIMUM"
    elif type_id == 5:
        op = "GREATER"
    elif type_id == 6:
        op = "LESS"
    elif type_id == 7:
        op = "EQUAL"
    return op


def eval(p: Packet):
    if len(p.sub_packets) == 0:
        return int(p.val, 2)
    type_id = p.type_id
    vals = []
    for sp in p.sub_packets:
        vals.append(eval(sp))

    if type_id == 0:
        return sum(vals)
    elif type_id == 1:
        acc = 1
        for val in vals:
            acc *= val
        return acc
    elif type_id == 2:
        return min(vals)
    elif type_id == 3:
        return max(vals)
    elif type_id == 5:
        return 1 if vals[0] > vals[1] else 0
    elif type_id == 6:
        return 1 if vals[0] < vals[1] else 0
    elif type_id == 7:
        return 1 if vals[0] == vals[1] else 0


def sum_versions(packet: Packet):
    acc = 0
    packets = [packet]
    for p in packets:
        acc += p.version
        for sub in p.sub_packets:
            acc += sum_versions(sub)
    return acc


p = decode(binary, 0)
print(f"{sum_versions(p)=}")
print(f"{eval(p)=}")
