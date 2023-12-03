import dataclasses
import sys
from collections import defaultdict

import networkx as nx
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


@dataclasses.dataclass(frozen=True)
class Node:
    elevation: int
    idx: int


def parse_graph(lines):
    head = None
    tail = None
    g = nx.DiGraph()
    nodes = defaultdict(list)
    all_coords = defaultdict(list)
    a_nodes = []
    i = 0
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            node = Node(ord(c), i)
            if c == "S":
                node = Node(ord("a"), i)
                head = node
            if c == "E":
                node = Node(ord("z"), i)
                tail = node
            i += 1
            g.add_node(node)
            nodes[node].append((x, y))
            all_coords[(x, y)].append(node)
            if node.elevation == ord("a"):
                a_nodes.append(node)

    for node, coords in nodes.items():
        add_paths_for_neighbors(all_coords, coords, g, node)

    return g, head, tail, a_nodes


def add_paths_for_neighbors(all_coords, coords, g, node):
    for coord in coords:
        neighbors = [
            (coord[0], coord[1] - 1),
            (coord[0], coord[1] + 1),
            (coord[0] - 1, coord[1]),
            (coord[0] + 1, coord[1]),
        ]
        for neighbor in neighbors:
            targets = all_coords[neighbor]
            for target in targets:
                if node.elevation >= target.elevation:
                    g.add_edge(node, target)
                if (target.elevation - node.elevation) == 1:
                    g.add_edge(node, target)


def main():
    lines = ProblemParser().load_input(2022, 12)
    graph, head, tail, a_nodes = parse_graph(lines)
    print("Part 1")
    shortest_path = nx.shortest_path(graph, source=head, target=tail)
    print(len(shortest_path) - 1)

    print("Part 2")
    lengths = []
    for node in a_nodes:
        try:
            shortest_path = nx.shortest_path(graph, source=node, target=tail)
            lengths.append(len(shortest_path) - 1)
        except:
            pass
    print(min(lengths))


if __name__ == "__main__":
    main()
