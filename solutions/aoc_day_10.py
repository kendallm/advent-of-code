from aoc_day_9 import Computer
import functools
from collections import defaultdict, Counter
from math import gcd, sqrt

max_x = 0
max_y = 0

nodes = set()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Segment:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def cmp(self, a, b):
        return (a > b) - (a < b) 
    
    def is_between(self, c):
        # Check if slope of a to c is the same as a to b ;
        # that is, when moving from a.x to c.x, c.y must be proportionally
        # increased than it takes to get from a.x to b.x .

        # Then, c.x must be between a.x and b.x, and c.y must be between a.y and b.y.
        # => c is after a and before b, or the opposite
        # that is, the absolute value of cmp(a, b) + cmp(b, c) is either 0 ( 1 + -1 )
        #    or 1 ( c == a or c == b)

        a, b = self.a, self.b             

        return ((b.x - a.x) * (c.y - a.y) == (c.x - a.x) * (b.y - a.y) and 
                abs(self.cmp(a.x, c.x) + self.cmp(b.x, c.x)) <= 1 and
                abs(self.cmp(a.y, c.y) + self.cmp(b.y, c.y)) <= 1)

def is_multiple(a, b):
    return a == b or (b != 0 and a / b == 0)

@functools.lru_cache(None)
def in_grid(position, max_x, max_y):
    return position[0] >= 0 and \
        position[0] < max_x and \
        position[1] >= 0 and \
        position[1] < max_y

@functools.lru_cache(None)
def distance(a,b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

@functools.lru_cache(None)
def is_between(a,c,b):
    return distance(a,c) + distance(c,b) == distance(a,b)

def can_see(nodes, max_x, max_y):
    best = None
    seen = defaultdict(set)
    for node in nodes:
        node_point = Point(node[0], node[1])
        for other in nodes:
            other_point = Point(other[0], other[1])
            if node == other:
                continue
            found = True
            for spot in nodes:
                spot_point = Point(spot[0], spot[1])
                if spot == node or spot == other:
                    continue
                if Segment(node_point, other_point).is_between(spot_point):
                    found = False
                    break
            if found:
                seen[node].add(other)
    best = 0    
    for item in seen.values():
        best = max(best, len(item))
    return best                
                        
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
        max_x = x
        max_y = y
    print(can_see(nodes, max_x, max_y))
    

if __name__ == "__main__":
    main()