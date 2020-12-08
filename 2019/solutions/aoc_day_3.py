from collections import defaultdict

crosses = set()
xs = defaultdict(lambda: defaultdict(tuple))

def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def do_work(x, y, steps, wire):
    
    seen = False
    try:
        point = xs[x][y]
        if point[1] != wire:
            seen = xs[x][y][0] > 0
    except:
        pass

    if seen:
        crosses.add((x, y, steps + xs[x][y][0]))
    else:
        xs[x][y] = (steps, wire)

if __name__ == "__main__":
    with open('../input/input_3.txt') as f:
        wire = 0
        for line in f:
            line = line.split(',')
            x = 0
            y = 0
            steps = 0
            wire += 1
            for move in line:
                move = move.strip()
                direction = move[0]
                if direction == 'L':
                    #going left
                    for i in range(int(move[1:])):
                        steps +=1
                        x -= 1
                        do_work(x, y, steps, wire)
                elif direction == 'R':
                    for i in range(int(move[1:])):
                        steps +=1
                        x += 1
                        do_work(x, y, steps, wire)
                elif direction == 'D':
                    #going down
                    for i in range(int(move[1:])):
                        steps +=1
                        y -= 1
                        do_work(x, y, steps, wire)         
                else:
                    #going up
                    for i in range(int(move[1:])):
                        steps +=1
                        y += 1
                        do_work(x, y, steps, wire)
             
    minimum = None
    for cross in crosses:
        if minimum == None:
            minimum = cross[2]
        minimum = min(minimum, cross[2])

    print(minimum)
