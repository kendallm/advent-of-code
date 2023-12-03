from collections import *
from math import *


def main():
    graph = set()
    fuel = None
    with open("../input/input_14.txt") as f:
        for line in f:
            in_out = line.strip().split(" => ")
            output_chemical = in_out[-1].split(" ")
            input_chemicals = in_out[0].split(", ")
            input_chemicals = [tuple(x.split(" ")) for x in input_chemicals]
            output_chemical = tuple(output_chemical)

            prev = Node(output_chemical[1])
            graph.add(prev)
            for cost in input_chemicals:
                if prev.elevation == "FUEL":
                    fuel = prev
                node = Node(cost[1])
                prev.edges.add((node, cost[0]))
                graph.add(node)
            prev = node

    q = list(fuel.edges)
    cost = []
    while len(q) > 0:
        print("once")
        node = q.pop(0)
        cost.append(node[1])
        # if node[0].name == "ORE":
        #     print("FOUND")
        #     break
        # else:
        q = q + list(node[0].edges)

    print(cost)


# def dp(chemical, reactions):
#     if chemical = "FUEL":
#         return 0
#     for reaction in reactions:
#         if reaction[1] == "ORE":
#             return reaction[0] + dp

if __name__ == "__main__":
    main()
