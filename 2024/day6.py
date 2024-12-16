import sys
import networkx as nx

from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


def find_guard(g: nx.Graph):
    for node in g.nodes:
        if g.nodes[node]['val'] == '^':
            return node
    return None

def find_next(curr, g: nx.Graph):
    next = None
    if curr not in g:
        return None
    if g.nodes[curr]['val'] == '^':
        next = (curr[0], curr[1] - 1)
    elif g.nodes[curr]['val'] == 'V':
        next = (curr[0], curr[1] + 1)
    elif g.nodes[curr]['val'] == '<':
        next = (curr[0] - 1, curr[1])
    elif g.nodes[curr]['val'] == '>':
        next = (curr[0] + 1, curr[1])
    else:
        raise ValueError("not a valid curr node")
    return next if next in g else None
    
def find_turn(curr, g):
    if g.nodes[curr]['val'] == '^':
        return '>'
    elif g.nodes[curr]['val'] == 'V':
        return '<'
    elif g.nodes[curr]['val'] == '<':
        return '^'
    elif g.nodes[curr]['val'] == '>':
        return 'V'
    else:
        raise ValueError("not a valid curr node")


def get_guard_path(g: nx.Graph):
    curr = find_guard(g)
    path = set()
    path.add(curr)
    dag = nx.DiGraph()
    while curr is not None:
        next = find_next(curr, g)
        if next is None:
            break
        g.nodes[next]
        dag.add_edge(curr, next)
        if g.nodes[next]['val'] != '#':
            g.nodes[next]['val'] = g.nodes[curr]['val']
            curr = next
            path.add(curr)
            continue
        elif g.nodes[next]['val'] == '#':
            # turn curr
            if g.nodes[curr]['val'] == '^':
                g.nodes[curr]['val'] = '>'
            elif g.nodes[curr]['val'] == 'V':
                g.nodes[curr]['val'] = '<'
            elif g.nodes[curr]['val'] == '<':
                g.nodes[curr]['val'] = '^'
            elif g.nodes[curr]['val'] == '>':
                g.nodes[curr]['val'] = 'V'
            else:
                raise ValueError("not a valid curr node", curr)
    return path, dag


# def find_potentials(g: nx.DiGraph):
#     count = 0
#     cycles = nx.simple_cycles(g)
#     cycles_count = len(list(cycles))
#     for a in g.nodes:
#         for b in g.nodes:
#             if a == b:
#                 continue
#             if a[0] == b[0] or a[1] == b[1]:
#                 g.add_edge(a, b)
#                 try:
#                     pcycle = nx.simple_cycles(g)
#                     pcycle_count = len(list(pcycle))
#                     print(pcycle_count, cycles_count)
#                     if pcycle_count > cycles_count:
#                         count += 1
#                 except Exception as e:
#                     print("no cycle", e)
#                 g.remove_edge(a,b)
#     return count

def main():
    problem = ProblemParser()
    lines = problem.load_input(2024, 6)
    g = problem.build_graph(lines)

    path, dag = get_guard_path(g)
    print(len(path))
    # print(find_potentials(dag))


if __name__ == '__main__':
    main()
