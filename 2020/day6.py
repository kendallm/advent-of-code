def part1():
    groups = [set()]
    with open("day6.txt") as f:
        i = 0
        for line in f.readlines():
            if line.strip() == "":
                groups.append(set())
                i += 1
            else:
                [groups[i].add(x) for x in (list(line.strip()))]

    groups = [len(x) for x in groups]

    print("Part1", sum(groups))


def part2():

    groups = [[set()]]
    with open("day6.txt") as f:
        i = 0
        j = 0
        for line in f.readlines():
            if line.strip() == "":
                groups.append(([set()]))
                i += 1
                j = 0
            else:
                [groups[i][j].add(x) for x in (list(line.strip()))]
                j += 1
                groups[i].append(set())

    groups = [len(set.intersection(*x[0:-1])) for x in groups]
    print("Part2", sum(groups))


part1()
part2()
