class Computer:
    def __init__(self):
        super().__init__()
    
    def run(self, memory):
        address = 0
        while address < len(memory):
            v = memory[address]
            args = []
            (instruction, num_args) = self.get_instruction_pointer(v)
            for i in range(num_args):
                args.append(memory[address + i + 1])   
            modes = v[:-2]   
            while len(modes) < num_args:
                modes = '0' + modes     
            if(instruction == self.jump_if_false or instruction == self.jump_if_true):
                jumped, update = instruction(address, memory, modes, args)
                if jumped:
                    address = int(update)
                    continue
            else:
                instruction(address, memory, modes, args)
            address = address + num_args + 1

    def get_instruction_pointer(self, intcode):
        if len(intcode) == 1:
            intcode = '0' + intcode
        instruction = intcode[-2:]

        if len(instruction) < 2:
            instruction = '0' + instruction

        if(instruction == '99'):
            return (self.abort, 0)
        elif instruction == '01':
            return (self.add, 3)
        elif instruction == '02':
            return (self.mul, 3)
        elif instruction == '03':
            return (self.get_input, 1)
        elif instruction == '04':
            return (self.output, 1)
        elif instruction == '05':
            return (self.jump_if_true, 2)
        elif instruction == '06':
            return (self.jump_if_false, 2)
        elif instruction == '07':
            return (self.less_than, 3)
        elif instruction == '08':
            return (self.equals, 3)
        else:
            raise ValueError("Invalid instruction", instruction)


    def jump_if_true(self, address, memory, modes, args):
        p1 = int(memory[int(args[0])]) if modes[1] == '0' else int(args[0])
        p2 = int(memory[int(args[1])]) if modes[0] == '0' else int(args[1])
        if p1 != 0:
            return True, p2
        return False, address


    def jump_if_false(self, address, memory, modes, args):
        p1 = int(memory[int(args[0])]) if modes[1] == '0' else int(args[0])
        p2 = int(memory[int(args[1])]) if modes[0] == '0' else int(args[1])
        if p1 == 0:
            return True, p2
        return False, address

    def less_than(self, address, memory, modes, args):
        p1 = int(memory[int(args[0])]) if modes[2] == '0' else int(args[0])
        p2 = int(memory[int(args[1])]) if modes[1] == '0' else int(args[1])
        if p1 < p2:
            memory[int(args[2])] = '1'
        else:
            memory[int(args[2])] = '0'
        return memory


    def equals(self, address, memory, modes, args):
        p1 = int(memory[int(args[0])]) if modes[2] == '0' else int(args[0])
        p2 = int(memory[int(args[1])]) if modes[1] == '0' else int(args[1])
        if p1 == p2:
            memory[int(args[2])] = '1'
        else:
            memory[int(args[2])] = '0'
        return memory

    def mul(self, address, memory, modes, args):
        p1 = int(memory[int(args[0])]) if modes[2] == '0' else int(args[0])
        p2 = int(memory[int(args[1])]) if modes[1] == '0' else int(args[1])
        output = p1 * p2
        memory[int(args[2])] = str(output)
        return memory

    def add(self, address, memory, modes, args):
        p1 = int(memory[int(args[0])]) if modes[2] == '0' else int(args[0])
        p2 = int(memory[int(args[1])]) if modes[1] == '0' else int(args[1])
        output = p1 + p2

        memory[int(args[2])] = str(output)
        return memory

    def get_input(self, address, memory, modes, args):
        p1 = int(args[0])
        memory[p1] = input("Input value: ")
        return memory

    def output(self, address, memory, modes, args):
        p1 = int(memory[int(args[0])]) if modes[0] == '0' else int(args[0])
        print( p1 )

    def abort(self, address, memory, modes, args):
        exit(0)

if __name__ == "__main__":
    computer = Computer()
    with open('../input/input_5.txt') as f:
        line = f.read()
        memory = line.split(',')
    computer.run(memory)