from collections import Counter
import collections

passwords = []

counter = 0
with open("day2.txt") as f:
    for line in f.readlines():
        counter += 1
        line = line.strip()
        password_policy = line.split(":")
        password = password_policy[1].strip()
        letter_range = password_policy[0].strip().split(" ")
        letter = letter_range[1].strip()
        minimum, maximum = letter_range[0].split("-")
        passwords.append(
            ((int(minimum), int(maximum)), letter, Counter(password), password)
        )

counter = 0
for v in passwords:
    minimum = v[0][0]
    maximum = v[0][1]
    letter = v[1]
    counts = v[2][letter]
    if counts >= minimum and counts <= maximum:
        counter = counter + 1
print(f"Part 1 {counter}")

counter = 0
for v in passwords:
    first = v[0][0]
    second = v[0][1]
    letter = v[1]
    counts = v[2][letter]
    password = v[3]
    if (password[first - 1] == letter and password[second - 1] != letter) or (
        password[first - 1] != letter and password[second - 1] == letter
    ):
        counter = counter + 1
print(f"Part 2 {counter}")
