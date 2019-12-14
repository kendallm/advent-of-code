from aoc_day_9 import Computer
import functools
from collections import defaultdict
import heapq
from math import gcd, sqrt, atan2, pi


def destroy_nodes(spot, visible):
    angles = list(visible[spot].items())
    angles.sort()
    
    q1 = []
    q2 = []
    q3 = []
    q4 = []
    for angle in angles:
        if angle[1][0][0] >= spot[0]:
            if angle[1][0][1] < spot[1]:
                q1.append(angle)
            else:
                q2.append(angle)
        if angle[1][0][0] <= spot[0]:
            if angle[1][0][1] > spot[1]:
                q3.append(angle)
            else:
                q4.append(angle)
    
    angles = q1 + q2 + q3 + q4

    count = 0
    for angle in angles:
        nodes = angle[1]
        if len(nodes) == 0:
            continue
        node = nodes.pop(0)
        count += 1
        ans = node[0] * 100 + node[1]
        if count == 201:
            print(f"ans = {ans}")


def can_see(nodes):
    visible = defaultdict(lambda: defaultdict(list))
    for node in nodes:
        for other in nodes:
            angle = atan2(node[1] - other[1], node[0] - other[0])
            visible[node][angle].append((other))
    best = 0  
    spot = None
    for k, v in visible.items():
        if len(v) > best:
            best = len(v)
            spot = k
        
    print(f"Best astroid can see {best} others from spot {spot}") 
    destroy_nodes(spot, visible)
    
                        
def main():
    nodes = set()
    with open('../input/input_10.txt') as f:
        y = 0
        for line in f:
            x = 0
            for i in range(len(line)):
                spot = line[i]
                if spot == '#':
                    position = (x, y)
                    nodes.add(position)               
                x += 1
            y += 1
    can_see(nodes)
    

if __name__ == "__main__":
    main()