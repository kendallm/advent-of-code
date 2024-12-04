import sys
import networkx as nx

from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser

def gen_paths(node):
    paths = ([node], [node], [node], [node], [node], [node], [node], [node])
    x, y = node
    for i in range(4):
        i += 1
        xl = x - i
        xr = x + i
        yu = y - i
        yd = y + i
        paths[0].append((xl, y))
        paths[1].append((xr, y))
        paths[2].append((x, yu))
        paths[3].append((x, yd))

        paths[4].append((xl, yu))
        paths[5].append((xr, yu))
        paths[6].append((xl, yd))
        paths[7].append((xr, yd))

    return paths

def gen_mas_paths(node):
    paths = ([], [])
    x, y = node
    xl = x - 1
    xr = x + 1
    yu = y - 1
    yd = y + 1

    paths[0].append((xl, yu))
    paths[0].append(node)
    paths[0].append((xr, yd))

    paths[1].append((xr, yu))
    paths[1].append(node)
    paths[1].append((xl, yd))

    return paths


def is_mas_x(g, first, second):
    try:
        a = g.nodes[first[0]]['letter'] + g.nodes[first[1]]['letter'] + g.nodes[first[2]]['letter']
        b = g.nodes[second[0]]['letter'] + g.nodes[second[1]]['letter'] + g.nodes[second[2]]['letter']
        return (a == "MAS" or a == "SAM") and (b == "MAS" or b == "SAM")
    except:
        return False

def is_xmas(g, path):
    try:
        return g.nodes[path[0]]['letter']  == "X" and \
            g.nodes[path[1]]['letter']  == "M"  and \
            g.nodes[path[2]]['letter'] == "A"  and \
            g.nodes[path[3]]['letter']  == "S"  
    except:
        return False

def count_xmas(g):
    potentials = []
    for x in g.nodes:
        if g.nodes[x]['letter'] != "X":
            continue
        potentials.extend(gen_paths(x))
    return sum([1 if is_xmas(g, p) else 0 for p in potentials])

def count_mas_x(g):
    potentials = []
    for x in g.nodes:
        if g.nodes[x]['letter'] != "A":
            continue
        potentials.append(gen_mas_paths(x))
    return sum([1 if is_mas_x(g, p[0], p[1]) else 0 for p in potentials])

def build_graph(lines):
    g = nx.Graph()
    for y, line in enumerate(reversed(lines)):
        for x, v in enumerate(line):
            node = (x, y)
            g.add_node(node)
            if y == 0:
                if x == len(lines[0]) - 1:
                    continue
                right = (x+1, y)
                g.add_edge(node, right)
                continue
            top = (x, y - 1)
            g.add_edge(node, top)

            if x > 0:
                top_l = (x - 1, y - 1)
                g.add_edge(node, top_l)
            if x < len(lines[0]) - 1:
                top_r = (x + 1, y - 1)
                g.add_edge(node, top_r)
    for node in g.nodes:
        g.nodes[node]['letter'] = lines[node[1]][node[0]]
    return g

def main():
    lines = ProblemParser().load_input(2024, 4)
    lines = [list(x) for x in lines]
 
    g = build_graph(lines)
    print(f"part1: {count_xmas(g)=}")
    print(f"part2: {count_mas_x(g)=}")


if __name__ == '__main__':
    main()
