import sys
import requests

url_structure = "https://adventofcode.com/2019/day/%s/input"
if __name__ == "__main__":
    s = requests.session()
    problem_number = sys.argv[1]
    with open(".session") as f:
        session_cookie = f.read().strip()
    cookie_obj = requests.cookies.create_cookie(
        domain=".adventofcode.com", name="session", value=session_cookie
    )
    s.cookies.set_cookie(cookie_obj)

    url = url_structure % problem_number
    print(url)
    response = s.get(url)

    with open(f"../input/input_{problem_number}.txt", "w") as f:
        f.write(response.content.decode("utf-8"))
