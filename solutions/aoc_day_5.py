def get_instruction_pointer(intcode):
    if len(intcode) == 1:
        intcode = '0' + intcode
    instruction = intcode[-2:]

    if len(instruction) < 2:
        instruction = '0' + instruction

    if(instruction == '99'):
        return (abort, 0)
    elif instruction == '01':
        return (add, 3)
    elif instruction == '02':
        return (mul, 3)
    elif instruction == '03':
        return (get_input, 1)
    elif instruction == '04':
        return (output, 1)
    elif instruction == '05':
        return (jump_if_true, 2)
    elif instruction == '06':
        return (jump_if_false, 2)
    elif instruction == '07':
        return (less_than, 3)
    elif instruction == '08':
        return (equals, 3)
    else:
        raise ValueError("Invalid instruction", instruction)


def jump_if_true(address, memory, modes, args):
    p1 = int(memory[int(args[0])]) if modes[1] == '0' else int(args[0])
    p2 = int(memory[int(args[1])]) if modes[0] == '0' else int(args[1])
    if p1 != 0:
        return True, p2
    return False, address


def jump_if_false(address, memory, modes, args):
    p1 = int(memory[int(args[0])]) if modes[1] == '0' else int(args[0])
    p2 = int(memory[int(args[1])]) if modes[0] == '0' else int(args[1])
    if p1 == 0:
        return True, p2
    return False, address

def less_than(address, memory, modes, args):
    p1 = int(memory[int(args[0])]) if modes[2] == '0' else int(args[0])
    p2 = int(memory[int(args[1])]) if modes[1] == '0' else int(args[1])
    if p1 < p2:
        memory[int(args[2])] = '1'
    else:
        memory[int(args[2])] = '0'
    return memory


def equals(address, memory, modes, args):
    p1 = int(memory[int(args[0])]) if modes[2] == '0' else int(args[0])
    p2 = int(memory[int(args[1])]) if modes[1] == '0' else int(args[1])
    if p1 == p2:
        memory[int(args[2])] = '1'
    else:
        memory[int(args[2])] = '0'
    return memory

def mul(address, memory, modes, args):
    p1 = int(memory[int(args[0])]) if modes[2] == '0' else int(args[0])
    p2 = int(memory[int(args[1])]) if modes[1] == '0' else int(args[1])
    output = p1 * p2
    memory[int(args[2])] = str(output)
    return memory

def add(address, memory, modes, args):
    p1 = int(memory[int(args[0])]) if modes[2] == '0' else int(args[0])
    p2 = int(memory[int(args[1])]) if modes[1] == '0' else int(args[1])
    output = p1 + p2

    memory[int(args[2])] = str(output)
    return memory

def get_input(address, memory, modes, args):
    p1 = int(args[0])
    memory[p1] = input("Input value: ")
    return memory

def output(address, memory, modes, args):
    p1 = int(memory[int(args[0])]) if modes[0] == '0' else int(args[0])
    print( p1 )

def abort(address, memory, modes, args):
    exit(0)

if __name__ == "__main__":
    with open('../input/input_5.txt') as f:
        line = f.read()
        memory = line.split(',')
    i = 0
    while i < len(memory):
        v = memory[i]
        args = []
        (instruction, num_args) = get_instruction_pointer(v)
        for j in range(num_args):
            args.append(memory[i + j + 1])   
        modes = v[:-2]   
        while len(modes) < num_args:
            modes = '0' + modes     
        if(instruction == jump_if_false or instruction == jump_if_true):
            jumped, update = instruction(i, memory, modes, args)
            if jumped:
                i = int(update)
                continue
        else:
            instruction(i, memory, modes, args)
        i = i + num_args + 1