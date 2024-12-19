import sys
from pathlib import Path

import networkx as nx

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser

def find_heads(g:nx.Graph):
    heads = []
    for node in g.nodes:
        if g.nodes[node]['val'] == 0:
            heads.append(node)
    return heads

def score(node: tuple[int, int], g: nx.Graph, found: list[tuple[int, int]]) -> int:
    if g.nodes[node]['val'] == 9:
        found.append(node)
        return 1
    total = 0
    for next in g.neighbors(node):
        if next in found:
            continue
        if g.nodes[next]['val'] == g.nodes[node]['val'] + 1:
            total += score(next, g, found)
    return total

def count_trails(node: tuple[int, int], g: nx.Graph, path: list[tuple[int, int]]) -> int:
    path = path.copy()
    path.append(node)
    if g.nodes[node]['val'] == 9:
        return 1
    total = 0
    for next in g.neighbors(node):
        if g.nodes[next]['val'] == g.nodes[node]['val'] + 1:
            total += count_trails(next, g, path)
    return total


def main():
    problem = ProblemParser()
    lines = problem.load_input(2024, 10)
    g = problem.build_graph(lines)
    for node in g:
        g.nodes[node]['val'] = int(g.nodes[node]['val'])
    heads = find_heads(g)
    print('scores')
    scores = [score(node, g, []) for node in heads]
    print(sum(scores), '\n')

    print('trails')
    trails = [count_trails(node, g, [node]) for node in heads]
    print(sum(trails))

if __name__ == '__main__':
    main()
