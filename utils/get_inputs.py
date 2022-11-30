import coloredlogs, logging
import sys
import requests
from pathlib import Path

from requests.models import Response


class ProblemParser:
    def __init__(self):
        pass

    def load_input(self, year, day):
        with open(f"{year}/input/input_{day}.txt") as f:
            lines = f.readlines()
        return [line.strip() for line in lines]


PYTHON_SOLUTION_TEMPLATE = """import sys
from pathlib import Path
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


lines = ProblemParser().load_input(%s, %s)
"""

LOGGER = logging.getLogger()
coloredlogs.install(level="DEBUG")


def get_session_cookie() -> str:
    with open(".session") as f:
        session_cookie = f.read().strip()
    return session_cookie


def download_input(s, year, problem_number, session_cookie) -> Response:
    cookie_obj = requests.cookies.create_cookie(
        domain=".adventofcode.com", name="session", value=session_cookie
    )
    s.cookies.set_cookie(cookie_obj)

    url = f"https://adventofcode.com/{year}/day/{problem_number}/input"
    response = s.get(url)
    return response


def generate_python_template(year, problem_number):
    directory = Path(f"{year}/solutions/")
    if not directory.is_dir():
        directory.mkdir(parents=True)
    solution = Path(f"{year}/solutions/day{problem_number}.py")

    if solution.is_file():
        LOGGER.warning("Python solution file already exists")
        return
    solution.touch()
    with open(f"{year}/solutions/day{problem_number}.py", "w") as f:
        f.write(PYTHON_SOLUTION_TEMPLATE % (year, problem_number))
    LOGGER.info("Created python solution file")


def generate_input_file(year, problem_number):
    s = requests.session()

    directory = Path(f"{year}/input/")
    if not directory.is_dir():
        directory.mkdir(parents=True)

    p = Path(f"{year}/input/input_{problem_number}.txt")
    if p.is_file() and p.stat().st_size > 0:
        LOGGER.warning("Input file already exists")
        return
    session_cookie = get_session_cookie()
    response = download_input(s, year, problem_number, session_cookie)
    if response.ok:
        with open(f"{year}/input/input_{problem_number}.txt", "w") as f:
            f.write(response.content.decode("utf-8"))
        LOGGER.info("Downloaded input file")
    else:
        LOGGER.error("Input file not found/available")


if __name__ == "__main__":
    year = sys.argv[1]
    problem_number = sys.argv[2]

    generate_input_file(year, problem_number)
    generate_python_template(year, problem_number)
