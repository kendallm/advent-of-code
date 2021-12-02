import sys
import requests
from pathlib import Path

class ProblemParser:
    def __init__(self):
        pass
    
    def load_input(self, year, day):
        with open(f"{year}/input/input_{day}.txt") as f:
            lines = f.readlines()
        return lines
    
PYTHON_SOLUTION_TEMPLATE = """import sys
from pathlib import Path
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


lines = ProblemParser().load_input(%s, %s)
"""

if __name__ == '__main__':
    s = requests.session()
    year = sys.argv[1]
    problem_number = sys.argv[2]
    
    p = Path(f'{year}/input/input_{problem_number}.txt')
    if p.is_file():
        print("Input file already exists")
        exit(1)

    with open('.session') as f:
        session_cookie = f.read().strip() 
    cookie_obj = requests.cookies.create_cookie(domain='.adventofcode.com',name='session',value=session_cookie)
    s.cookies.set_cookie(cookie_obj)

    url = f"https://adventofcode.com/{year}/day/{problem_number}/input"
    response = s.get(url)

    if response.ok:
        print(url)
        with open(f'{year}/input/input_{problem_number}.txt', 'w') as f:
            f.write(response.content.decode('utf-8'))
        Path(f'{year}/solutions/day{problem_number}.py').touch()
        with open(f'{year}/solutions/day{problem_number}.py', 'w') as f:
            f.write(PYTHON_SOLUTION_TEMPLATE % year, problem_number)
    else:
        print("Input file not found/available")
        sys.exit(1)
