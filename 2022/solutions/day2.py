import sys
from pathlib import Path
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


lines = ProblemParser().load_input(2022, 2)

rock = "A"
paper = "B"
scissors = "C"

my_rock = "X"
my_paper = "Y"
my_scissors = "Z"

rock_score = 1
paper_score = 2
scissors_score = 3

lose = "X"
draw = "Y"
win = "Z"

score = 0
for line in lines:
    them, me = line.split(" ")
    if them == rock:
        if me == my_scissors:
            score +=  scissors_score
        elif me == my_paper:
            score += 6 + paper_score
        else:
            score += 3 + rock_score
    if them == paper:
        if me == my_rock:
            score += rock_score
        elif me == my_scissors:
            score += 6 + scissors_score
        else:
            score += 3 + paper_score
    if them == scissors:
        if me == my_paper:
            score += paper_score
        elif me == my_rock:
            score += 6 + rock_score
        else:
            score += 3 + scissors_score
print(score)

score = 0
for line in lines:
    them, result = line.split(" ")
    if them == rock:
        if result == lose:
            score += scissors_score
        elif result == win:
            score += 6 + paper_score
        else:
            score += 3 + rock_score
    if them == paper:
        if result == lose:
            score += rock_score
        elif result == win:
            score += 6 + scissors_score
        else:
            score += 3 + paper_score
    if them == scissors:
        if result == lose:
            score += paper_score
        elif result == win:
            score += 6 + rock_score
        else:
            score += 3 + scissors_score
def play_game():
    score = 0
    for line in lines:
        them, result = line.split(" ")
        if them == rock:
            if result == lose:
                score += scissors_score
            elif result == win:
                score += 6 + paper_score
            else:
                score += 3 + rock_score
        if them == paper:
            if result == lose:
                score += rock_score
            elif result == win:
                score += 6 + scissors_score
            else:
                score += 3 + paper_score
        if them == scissors:
            if result == lose:
                score += paper_score
            elif result == win:
                score += 6 + rock_score
            else:
                score += 3 + scissors_score
print(score)