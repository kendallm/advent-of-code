from utils import Computer
from collections import deque, defaultdict
from math import inf
import curses
from time import sleep

def main():
    with open('../input/input_13.txt') as f:
        items = f.read()
        items[0] = "2"
    computer = Computer(items, [], inf)
    computer.run()
    count = 0
    for i in range(len(computer._output)):
        out = computer._output[i]
        if (i + 1) % 3 == 0 and out == 2:
            count += 1
        i += 1
    print(count)

def print_screen(stdscr, screen):
    stdscr.clear()
    for k, v in screen.items()  :
        try:
            stdscr.addstr(k[1], k[0], v)
        except:
            pass
    stdscr.refresh()
    sleep(1)            


def main2(stdscr, win):
    stdscr.clear()
    with open('../input/input_13.txt') as f:
        items = f.read()
        items = items[1:]
        items = "2" + items
    computer = Computer(items, [], inf, win)
    # computer.add_input("0")
    computer.run()
    screen = {}
    ball_location = (0,0)
    prev_ball = (0,0)
    position = (0,0)
    prev_position = (0,0)
    while not computer._halted:
        while computer._paused:
            out = []
            while len(computer._output) > 0:
                out.append(computer._output.pop(0))
            while(len(out) > 0):
                x = out.pop(0)
                y = out.pop(0)
                coord = (x, y)
                tile = out.pop(0)
                if x == -1 and y == 0:
                    print(tile)
                if tile == 4: # Ball
                    screen[coord] = '*'
                    prev_ball = ball_location
                    ball_location = coord 
                elif tile == 1: #wall
                    screen[coord] = '|'
                elif tile == 2: #block
                    screen[coord] = '#'
                elif tile == 3:
                    screen[coord] = '~'
                    prev_position = position
                    position = coord
                elif tile == 0:
                    screen[coord] = '.'
            if prev_position[0] < prev_ball[0]:
                computer.add_input('1')
            elif position[0] > prev_ball[0]:
                computer.add_input('-1')
            else:
                computer.add_input('0')
            print_screen(stdscr, screen)  
            computer.run()
        print(tile)
            
            
if __name__ == "__main__":
    import curses
    from curses import wrapper

    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()

    begin_x = 0; begin_y = 0
    height = 500; width = 500
    win = curses.newwin(height, width, begin_y, begin_x)
    main2(stdscr, win)

