import itertools

cache = []
with open("input.txt") as f:
    lines = f.readlines()
    for item in lines:
        number = int(item)
        if 2020 - number in cache:
            print(number * (2020 - int(number)))
        cache.append(number)

for item in itertools.combinations(cache, 3):
    if sum(item) == 2020:
        print(item)
