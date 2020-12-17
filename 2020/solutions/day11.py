from utils.get_inputs import ProblemParser
from collections import defaultdict
lines = ProblemParser().load_input(2020, 11)
lines = [list(x.strip()) for x in lines]


def build_graph_1():
    graph = defaultdict(set)
    for i, v in enumerate(lines):
        for j, _ in enumerate(v):
            spot = (i,j)
            # left
            if j > 0:
                graph[spot].add((i, j - 1))
            # lu
            if i > 0 and j > 0:
                graph[spot].add((i - 1, j - 1))
            # up
            if i > 0:
                graph[spot].add((i - 1, j))
            # ru
            if j < len(v) - 1 and i > 0:
                graph[spot].add((i - 1, j + 1))
            # right
            if j < len(v) - 1:
                graph[spot].add((i, j + 1))
            # rd
            if j < len(v) - 1 and i < len(lines) - 1:
                graph[spot].add((i + 1, j + 1))
            # down
            if i < len(lines) - 1:
                graph[spot].add((i + 1, j))
            # ld 
            if j > 0 and i < len(lines) - 1:
                graph[spot].add((i + 1, j - 1))

    return graph

def build_graph_2(lines):
    graph = defaultdict(set)
    for i, v in enumerate(lines):
        for j, _ in enumerate(v):
            spot = (i,j)
            if lines[i][j] == '.':
                continue
            else:
                graph[spot] = set()
            # left
            if j > 0:
                y = j - 1
                while(y >= 0 and v[y] == '.'):
                    y -= 1
                if y >= 0:
                    graph[spot].add((i, y))
            # lu
            if i > 0 and j > 0:
                y = j - 1
                x = i - 1
                while(x >= 0 and y >= 0 and lines[x][y] == '.'):
                    y -= 1
                    x -= 1
                if y >= 0 and x >= 0:
                    graph[spot].add((x, y))
            # up
            if i > 0:
                x = i - 1
                while(x >= 0 and lines[x][j] == '.'):
                    x -= 1
                if x >= 0:
                    graph[spot].add((x, j))
            # ru
            if j < len(v) - 1 and i > 0:
                y = j + 1
                x = i - 1
                while(x >= 0 and y < len(v) and lines[x][y] == '.'):
                    y += 1
                    x -= 1
                if y < len(v) and x >= 0:
                    graph[spot].add((x, y))
            # right
            if j < len(v) - 1:
                y = j + 1
                while(y < len(v) and v[y] == '.'):
                    y += 1
                if y < len(v):
                    graph[spot].add((i, y))

            # rd
            if j < len(v) - 1 and i < len(lines) - 1:
                y = j + 1
                x = i + 1
                while(x < len(lines) and y < len(v) and lines[x][y] == '.'):
                    y += 1
                    x += 1
                if y < len(v) and x < len(lines):
                    graph[spot].add((x, y))

            # down
            if i < len(lines) - 1:
                x = i + 1
                while(x < len(lines) and lines[x][j] == '.'):
                    x += 1
                if x < len(lines):
                    graph[spot].add((x, j))
                    
            # ld 
            if j > 0 and i < len(lines) - 1:
                y = j - 1
                x = i + 1
                while(x < len(lines) and y >= 0 and lines[x][y] == '.'):
                    y -= 1
                    x += 1
                if y >= 0 and x < len(lines):
                    graph[spot].add((x, y))
    return graph
def part1():
    text = lines.copy()
    changed = True
    while changed:
        occupy = set()
        free = set()
        print('.')
        for k,v in graph.items():
            x, y = k

            if text[x][y] == 'L':
                a = [text[x1][y1] == 'L' or text[x1][y1] == '.' for x1, y1 in v]
                if False not in a:
                    occupy.add((x, y))
            if text[x][y] == '#':
                a = [1 if text[x1][y1] == '#' else 0 for x1, y1 in v]
                if sum(a) >= 4:
                    free.add((x,y))
        if len(occupy) > 0 or len(free) > 0:
            changed = True
            for x, y in occupy:
                text[x][y] = '#'
            for x, y in free:
                text[x][y] = 'L'
        else:
            changed = False
    count = 0
    for x, y in graph.keys():
        if text[x][y] == '#':
            count += 1
    print(count)


def part2():
    graph = build_graph_2(lines)
    text = lines.copy()
    changed = True
    times = 0
    while changed:
        times += 1
        occupy = set()
        free = set()
        for k,v in graph.items():
            x, y = k

            if text[x][y] == 'L':
                a = [text[x1][y1] == 'L' or text[x1][y1] == '.' for x1, y1 in v]
                if False not in a:
                    occupy.add((x, y))
            if text[x][y] == '#':
                a = [1 if text[x1][y1] == '#' else 0 for x1, y1 in v]
                if sum(a) >= 5:
                    free.add((x,y))
        if len(occupy) > 0 or len(free) > 0:
            changed = True
            for x, y in occupy:
                text[x][y] = '#'
            for x, y in free:
                text[x][y] = 'L'
        else:
            changed = False
    count = 0
    for x, y in graph.keys():
        if text[x][y] == '#':
            count += 1
    from pprint import pprint
    print(count)
# part1()
part2()


