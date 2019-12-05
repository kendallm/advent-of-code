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
        return (3, get_instruction_pointer(instruction), modes)
    elif instruction == '02':
        while len(modes) < 3:
            modes = '0' + modes
        return (3, get_instruction_pointer(instruction), modes)
    elif instruction == '03':
        return (1, get_instruction_pointer(instruction), modes)
    elif instruction == '04':
        while len(modes) < 1:
            modes = '0' + modes
        return (1, get_instruction_pointer(instruction), modes)
    elif instruction == '05':
        while len(modes) < 2:
            modes = '0' + modes
        return (2, get_instruction_pointer(instruction), modes)
    elif instruction == '06':
        while len(modes) < 2:
            modes = '0' + modes
        return (2, get_instruction_pointer(instruction), modes)
    elif instruction == '07':
        while len(modes) < 3:
            modes = '0' + modes
        return (3, get_instruction_pointer(instruction), modes)
    elif instruction == '08':
        while len(modes) < 3:
            modes = '0' + modes
        return (3, get_instruction_pointer(instruction), modes)


def get_instruction_pointer(instruction):
    if len(instruction) < 2:
        instruction = '0' + instruction

    if(instruction == '99'):
        return abort
    elif instruction == '01':
        return add
    elif instruction == '02':
        return mul
    elif instruction == '03':
        return get_input
    elif instruction == '04':
        return output
    elif instruction == '05':
        return jump_if_true
    elif instruction == '06':
        return jump_if_false
    elif instruction == '07':
        return less_than
    elif instruction == '08':
        return equals
    else:
        raise ValueError("Invalid instruction", instruction)


def jump_if_true(memory, modes, args):
    p1 = int(memory[int(args[0])]) if modes[2] == '0' else int(args[0])
    p2 = int(memory[int(args[1])]) if modes[1] == '0' else int(args[1])
    print("jump if true")
    if p1 != 0:
        return get_instruction_pointer(memory[p2])(memory, modes, args)
    return memory


def jump_if_false(memory, modes, args):
    print("jump if false")
    p1 = int(memory[int(args[0])]) if modes[1] == '0' else int(args[0])
    p2 = int(memory[int(args[1])]) if modes[0] == '0' else int(args[1])
    if p1 == 0:
        return get_instruction_pointer(memory[p2])(memory, modes, args)
    return memory

def less_than(memory, modes, args):
    p1 = int(memory[int(args[0])]) if modes[1] == '0' else int(args[0])
    p2 = int(memory[int(args[1])]) if modes[0] == '0' else int(args[1])
    if p1 < p2:
        memory[int(args[2])] = '1'
    else:
        memory[int(args[2])] = '0'
    return memory


def equals(memory, modes, args):
    p1 = int(memory[int(args[0])]) if modes[2] == '0' else int(args[0])
    p2 = int(memory[int(args[1])]) if modes[1] == '0' else int(args[1])
    if p1 == p2:
        memory[int(args[2])] = '1'
    else:
        memory[int(args[2])] = '0'
    return memory

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
    return memory

def output(memory, modes, args):
    p1 = int(memory[int(args[0])]) if modes[0] == '0' else int(args[0])
    print( p1 )

def abort(memory, modes, args):
    exit(0)

if __name__ == "__main__":
    with open('../input/input_5.txt') as f:
        line = f.read()
        # line = '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,9'
        memory = line.split(',')
    
    itr =  enumerate(memory)
    for i, v in itr:
        options = process_intcode(v)
        args = []
        for j in range(options[0]):
            args.append(next(itr)[1])            
        options[1](memory, options[2], args)