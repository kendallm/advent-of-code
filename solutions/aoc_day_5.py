def process_intcode(intcode):
    if len(intcode) == 1:
        intcode = '0' + intcode
    instruction = intcode[-2:]
    modes = intcode[:-2]

    if(instruction == '99'):
        return (0, abort, modes)
    elif instruction == '01':
        while len(modes) < 3:
            modes = '0' + modes
        return (3, add, modes)
    elif instruction == '02':
        while len(modes) < 3:
            modes = '0' + modes
        return (3, mul, modes)
    elif instruction == '03':
        return (1, get_input, modes)
    elif instruction == '04':
        while len(modes) < 1:
            modes = '0' + modes
        return (1, output, modes)
    else:
        raise ValueError("Invalid instruction", instruction, intcode)


def mul(memory, modes, args):
    p1 = int(memory[int(args[0])]) if modes[2] == '0' else int(args[0])
    p2 = int(memory[int(args[1])]) if modes[1] == '0' else int(args[1])
    output = p1 * p2

    memory[int(args[2])] = str(output)
    return memory

def add(memory, modes, args):
    p1 = int(memory[int(args[0])]) if modes[2] == '0' else int(args[0])
    p2 = int(memory[int(args[1])]) if modes[1] == '0' else int(args[1])
    output = p1 + p2

    memory[int(args[2])] = str(output)
    return memory

def get_input(memory, modes, args):
    p1 = int(args[0])
    memory[p1] = input("Input value: ")

def output(memory, modes, args):
    p1 = int(memory[int(args[0])]) if modes[0] == '0' else int(args[0])
    print( p1 )

def abort(memory, modes, args):
    exit(0)

if __name__ == "__main__":
    with open('../input/input_5.txt') as f:
        line = f.read()
        # line = '1002,4,3,4,33'
        memory = line.split(',')
    
    itr =  enumerate(memory)
    for i, v in itr:
        options = process_intcode(v)
        args = []
        for j in range(options[0]):
            args.append(next(itr)[1])
        options[1](memory, options[2], args)

