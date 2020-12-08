cache = {}
target = ('shiny', 'gold')

def parse_bag(text):
    text = text.strip().split()
    return (text[0], text[1])

def parse_contents(text):
    res = []
    items = text[:-1].split(', ')
    items[-1] = items[-1][:-1]
    for item in items:
        if item.strip() == 'no other bags':
            return res
        count = int(item[0])
        contents = parse_bag(item[2:])
        res.append((contents, count))
    return res

def find_bag(source, target, seen):
    found = False
    for contents in cache[source]:
        if contents[0] in seen:
            continue
        if contents[0] == target:
            return True
        else:
            seen.add(contents[0])
            found = found or find_bag(contents[0], target, seen.copy())
    return found

with open('day7.txt') as f:
    for line in f.readlines():
        line = line.split(' contain ')
        bag = parse_bag(line[0])
        if bag in cache.keys():
            cache[bag].append(parse_contents(line[1]))
        else:
            cache[bag] = parse_contents(line[1])

def part1():
    bags = set([])
    for key in cache.keys():
        # print(key)
        if find_bag(key, target, seen = set()):
            bags.add(key)
    print("part 1", len(bags))

def count_bags(source):
    total = 0
    print(cache[source])
    for item in cache[source]:
        bag, number = item
        total += number
        total += count_bags(bag) * number
    print(source, total)
    return total

def part2():
    print(count_bags(target))

part2()
