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
    
if __name__ == '__main__':
    s = requests.session()
    year = sys.argv[1]
    problem_number = sys.argv[2]
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
    else:
        print("Input file not found/available")
        sys.exit(1)
