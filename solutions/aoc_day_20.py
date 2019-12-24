import os, sys
from collections import *
import re
import copy

class Node(object):
    def __init__(self, name, edges=set()):
        self._name = name
        self.edges = edges


def build_edges(grid, portals):
    keys = list(grid.keys())
    keys.sort(key=lambda x: (x[1], x[0]))
    for (x, y) in grid:
        if (x + 1, y) in grid:
            grid[(x,y)].add((x + 1, y))
        if (x - 1, y) in grid:
            grid[(x,y)].add((x - 1, y))
        if (x, y + 1) in grid:
            grid[(x,y)].add((x, y + 1))
        if (x, y - 1) in grid:
            grid[(x,y)].add((x, y - 1))

    # need to join outer and inner here
    ps = portals["inner"]
    for k, v in portals['outer'].items():
        ps[k].extend(v)
    for portal in ps.values():
        if len(portal) > 1:
            grid[portal[0]].add(portal[1])
            grid[portal[1]].add(portal[0])
    return grid


def get_horizontal_portals(line, y, portals):
    p = re.compile('[A-Za-z]{2}')
    ms = p.finditer(line)
    for m in ms:
        (start, stop) = m.span()
        if start == 0:
            #Outer
            portals["outer"][m.group(0)].append((stop + 1, y))
        elif line[start - 1] == ' ':
            #to right
            portals["inner"][m.group(0)].append((stop + 1, y))
        elif line[start - 2] == ' ':
            #to left
            portals["inner"][m.group(0)].append((start, y))
        elif line[stop] == ' ':
            portals["inner"][m.group(0)].append((start, y))
        else:
            portals["outer"][m.group(0)].append((start, y))


def get_vertical_portals(line, found_first, prev_prev, portals, prev, y):
    p = re.compile(' [A-Za-z]')
    ms = p.finditer(line)
    for m in ms:
        if not found_first:
            return True
        (_, stop) = m.span()
        if prev_prev != '' and prev_prev[stop - 1] == '.':
            if prev[2] == '#':
                portals["inner"][prev[stop - 1] + line[stop - 1]].append((stop, y - 2))
            else:
                portals["outer"][prev[stop - 1] + line[stop - 1]].append((stop, y - 2))
            #bottom
        else:
            #top
            if prev_prev == '':
                portals["outer"][prev[stop - 1] + line[stop - 1]].append((stop, y + 1))
            else:
                portals["inner"][prev[stop - 1] + line[stop - 1]].append((stop, y + 1))
    return False


def get_num_steps(grid, start, stop):
    q = deque()
    q.append(start)

    steps = 0
    seen = set()
    while(q):
        node = q.popleft()
        steps += 1
        if node == stop:
            return steps
        for node in grid[node]:
            if node not in seen:
                q.append(node)
                seen.add(node)
    return steps

def get_steps(grid, start, stop, steps, seen=set()):
    # print(f"start: {start}, stop: {stop}, steps {steps}")
    seen.add(start)
    # print(start, stop)
    if start == stop:
        print(f"found at {steps}")
        return steps
    nodes = grid[start]
    if nodes.issubset(seen):
        return steps
    for node in nodes:
        if node in seen:
            continue
        steps + get_steps(grid, node, stop, steps + 1, seen.copy())
    return steps


def get_steps_levels(grid, start, stop, steps, portals, seen=defaultdict(set), level=0):
    seen[level].add(start)
    if start == stop and level == 0:
        print(f"found at {steps}")
        return steps
    nodes = grid[start]
    if nodes.issubset(seen[level]):
        return steps
    for node in nodes:
        if node in seen[level]:
            continue
        if node in portals['outer'] and level == 0:
            print("skip out")
            continue
        if node in portals['inner']:
            seen[level].add(node)
            # print(node)
            level += 1
        elif node in portals['outer']:
            seen[level].add(node)
            # print(node)
            level -= 1
        steps + get_steps_levels(grid, node, stop, steps + 1, portals, seen, level)
    return steps


def main():
    grid = {}
    portals = {} 
    portals["inner"] = defaultdict(list)
    portals["outer"] = defaultdict(list)

    with open('../input/input_20.txt') as f:
        y = 0
        prev = ''
        prev_prev = ''
        found_first = False
        for line in f:
            found_first = get_vertical_portals(line, found_first, prev_prev, portals, prev, y)
            get_horizontal_portals(line, y, portals)
            x = 1
            print(line[:-1] + str(y))
            for char in line:
                if char == '.':
                    grid[(x, y)] = set()
                x += 1
            y += 1
            prev_prev = prev
            prev = line
    grid = build_edges(grid, copy.deepcopy(portals))
    start = portals['outer']['AA'][0]
    target = portals['outer']['ZZ'][0]
    # get_steps(grid, start, target, 0, set())
    ps = {
        'inner': set(),
        'outer': set()
    }
    

    for portal in portals['inner'].values():
        ps['inner'] = ps['inner'].union(set(portal))
        
    for portal in portals['outer'].values():
        ps['outer'] = ps['outer'].union(set(portal))
    get_steps_levels(grid, start, target, 0, ps)

if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()