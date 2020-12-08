from utils import Computer
from collections import deque, defaultdict
import pprint
from functools import reduce
import numpy as np


def cmp(a, b):
    return (a>b)-(a<b)

def apply_velocity(items, velocities):
    results = []
    new_vel = {}
    for item in items:
        velocity = velocities[item]
        updated = (item[0] + velocity[0],
                   item[1] + velocity[1], 
                   item[2] + velocity[2])
        results.append(updated)
        new_vel[updated] = velocity
    return (results, new_vel)
    

def apply_gravity(items, velocities):
    results = defaultdict()
    
    for item in items:
        velocity = velocities[item]
        for other in items:
            velocity = (
                velocity[0] + cmp(other[0], item[0]),
                velocity[1] + cmp(other[1], item[1]),
                velocity[2] + cmp(other[2], item[2]),
            )
        results[item] = velocity
    return results
    
def calculate_total_energy(items, velocities):
    potentials = defaultdict()
    kinetics = defaultdict()
    totals = defaultdict()
    
    for item in items:
        potentials[item] = sum([abs(x) for x in item])
        kinetics[item] = sum([abs(x) for x in velocities[item]])
        totals[item] = potentials[item] * kinetics[item]
    return totals

def all_found(initial, items, velcoties, i):
    same = []
    # print(velcoties.values()[i])
    for j in range(len(initial)):
        x = initial[j][i]
        y = items[j][i]
        v = list(velcoties.values())[j][i]
        same.append(x == y and v == 0)
    return all(same)

def cycle(items, velocities):
    return apply_velocity(items, apply_gravity(items, velocities))

def part_one(items, velocities):
    for _ in range(100):
        (items, velocities) = cycle(items, velocities)
    print(f"Total energy: {sum(calculate_total_energy(items, velocities).values())}")


def part_two(items, velocities):
    inital_positions = items.copy()
    repeats = [-1,-1,-1]
    (items, velocities) = cycle(items, velocities)
    cycles = 1
    while True:
        cycles +=1
        (items, velocities) = cycle(items, velocities)
        if repeats[0] == -1 and all_found(inital_positions, items, velocities, 0):
            repeats[0] = cycles
        if repeats[1] == -1 and all_found(inital_positions, items, velocities, 1):
            repeats[1] = cycles
        if repeats[2] == -1 and all_found(inital_positions, items, velocities, 2):
            repeats[2] = cycles
        if -1 not in repeats:
            break
    print(np.lcm.reduce(repeats))

def main():
    items = []
    velocities = defaultdict()
    with open('../input/input_12.txt') as f:
        for line in f:
            pos = line.strip()[1:-1].split(', ')
            item = (
                int(pos[0].split('=')[1].strip()), 
                int(pos[1].split('=')[1].strip()), 
                int(pos[2].split('=')[1].strip())
            )
            items.append(item)
            velocities[item] = (0,0,0)
    part_one(items, velocities)
    part_two(items, velocities)

if __name__ == "__main__":
    main()

