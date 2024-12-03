import coloredlogs, logging
import sys
import requests
from pathlib import Path

from requests.models import Response


class ProblemParser:
    def __init__(self):
        pass

    def load_input(self, year, day, strip=True):
        with open(f"{year}/input/input_{day}.txt") as f:
            lines = f.readlines()

        return (
            [line.strip() for line in lines]
            if strip
            else [line.strip("\n") for line in lines]
        )


PYTHON_SOLUTION_TEMPLATE = """import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


def main():
    lines = ProblemParser().load_input(%s, %s)

if __name__ == '__main__':
    main()
"""

LOGGER = logging.getLogger()
coloredlogs.install(level="DEBUG")


def get_session_cookie() -> str:
    with open(".session") as f:
        session_cookie = f.read().strip()
    return session_cookie


def download_input(year: str, problem_number: str) -> Response:
    session = requests.session()
    session_cookie = get_session_cookie()
    cookie_obj = requests.cookies.create_cookie(
        domain=".adventofcode.com", name="session", value=session_cookie
    )
    session.cookies.set_cookie(cookie_obj)

    url = f"https://adventofcode.com/{year}/day/{problem_number}/input"
    response = session.get(
        url,
        headers={
            "user-agent": "https://github.com/kendallm/advent-of-code https://mastodon.social/@kendallmorgan"
        },
    )
    return response


def get_path(dir: str, file: str) -> Path:
    directory = Path(dir)
    if not directory.is_dir():
        directory.mkdir(parents=True)
    p = Path(f"{dir}{file}")
    if p.is_file():
        LOGGER.warning(f"File: {p} already exists")
        raise FileExistsError
    return p


def generate_python_template(year: str, problem_number: str):
    try:
        solution_path = get_path(f"{year}/", f"day{problem_number}.py")
        solution_path.touch()
        with solution_path.open("w") as f:
            f.write(PYTHON_SOLUTION_TEMPLATE % (year, problem_number))
        LOGGER.info("Created python solution file")
    except Exception as _:
        return


def generate_input_file(year: str, problem_number: str):
    try:
        input_path = get_path(f"{year}/input/", f"input_{problem_number}.txt")
        response = download_input(year, problem_number)
        if not response.ok:
            LOGGER.error("Input file not found/available")

        with input_path.open("w") as f:
            f.write(response.content.decode("utf-8"))
        LOGGER.info("Downloaded input file")
    except Exception as _:
        return


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python get_inputs {year} {day}")
        exit(1)
    year = sys.argv[1]
    problem_number = sys.argv[2]

    generate_input_file(year, problem_number)
    generate_python_template(year, problem_number)
