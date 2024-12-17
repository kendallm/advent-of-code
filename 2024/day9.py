import itertools
import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


def get_fs(line):
    print('building fs...')
    fs = []
    count = 0
    for i in range(0, len(line), 2):
        j = i + 1
        a = line[i]
        b = 0
        if len(line) > j:
            b = line[j]
        for _ in range(int(a)):
            fs.append(count)
        for _ in range(int(b)):
            fs.append(None)
        count += 1
    return fs

def right_most(fs):
    for i in range(len(fs) - 1, 0, -1):
        if fs[i] is not None:
           return i, fs[i]

def defrag(fs):
    print('defraging...')
    for i in range(len(fs)):
        if fs[i] is None:
            spot, val = right_most(fs)
            if spot < i:
                return fs
            fs[i] = val
            fs[spot] = None
    return fs

def get_blocks(fs):
    block = []
    for i in range(len(fs) - 1, -1, -1):
        v = fs[i]
        if v is None and len(block) == 0:
            continue
        if len(block) == 0 or v == block[0]:
            block.append(v)
            continue
        yield i + 1, block
        block = [] if v is None else [v]
    yield i + 1, block

def find_space(block, fs):
    size = len(block)
    # print(f"finding space for block {block}")
    count = 0
    idx = -1
    for i, v in enumerate(fs):
        if v is None:
            count += 1
            if idx == -1:
                idx = i
            continue
        else:
            if count >= size:
                return idx
            count = 0
            idx = -1
    return idx if count >= size else -1

def defrag_by_block(fs):
    print('block defraging...')
    blocks = get_blocks(fs.copy())
    for idx, block in blocks:
        start = find_space(block, fs)
        if start > idx:
            continue
        if start == -1:
            continue
        for i in range(len(block)):
            fs[start + i] = block[0]
        for i in range(len(block)):
            fs[idx + i] = None
    return fs

def checksum(fs):
    print('calculating checksum...')
    cs = 0
    for i, v in enumerate(fs):
        cs += (i * v) if v is not None else 0
    return cs

def main():
    lines = ProblemParser().load_input(2024, 9)
    line = lines[0]
    fs = get_fs(line)
    # fs = defrag(fs)
    fs = defrag_by_block(fs)
    cs = checksum(fs)
    print(cs)

if __name__ == '__main__':
    main()
