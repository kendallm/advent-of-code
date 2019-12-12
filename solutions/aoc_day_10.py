from aoc_day_9 import Computer
import functools
from collections import defaultdict
import heapq
from math import gcd, sqrt, atan2


nodes = set()


def can_see(nodes):
    visible = defaultdict(lambda: defaultdict(list))
    for node in nodes:
        for other in nodes:
            angle = atan2(node[0] - other[0], node[1] - other[1])
            visible[node][angle].append(other)
    best = 0  
    spot = None
    for k, v in visible.items():
        if len(v) > best:
            best = len(v)
            spot = k
    angles = list(visible[spot].items())
    angles.sort()
    
    for angle in angles:
        heapq.heapify(angle[1])
    
    count = 0
    while count < 200:
        for angle in angles:
            nodes = angle[1]
            if len(nodes) > 0:
                node = nodes.pop(0)
                count += 1
                if count == 200:
                    print(node[0] * 100 + node[1])
                continue
        
    print(f"Best astroid can see {best} others") 
    
                   
                        
def main():
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