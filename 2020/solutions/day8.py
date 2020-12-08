from utils.get_inputs import ProblemParser


lines = ProblemParser().load_input(2020, 8)


def parse_program():
    return [tuple(x.split()) for x in lines]


def parse_value(value):
    return (value[0], int(value[1:]))


def run(program):
    acc = 0
    pointer = 0
    cache = {}
    part1 = False
    looped = set()
    while pointer < len(program):
        command, value = program[pointer]
        sign, number = parse_value(value)
        if pointer in looped:
            acc = cache[pointer]
        elif pointer in cache.keys():
            if not part1:
                print("Part1", acc)
                part1 = True
            
            if command == 'jmp':
                command = 'nop'
            else:
                command = 'nop'
            acc = cache[pointer]
            looped.add(pointer)
        
        cache[pointer] = acc
        if command == 'jmp':
            if sign == '-':
                pointer -= number
            else:
                pointer += number
        else:
            if command != 'nop':
                if sign == '-':
                    acc -= number
                else:
                    acc += number
            pointer += 1
    return acc
print("Part2", run(parse_program()))