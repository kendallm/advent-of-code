class Computer:

    def __init__(self, memory):
        self._memory = memory
        super().__init__()
    
    def run(self):
        address = 0
        while address < len(self._memory):
            v = self._memory[address]
            args = []
            (instruction, num_args) = self.get_instruction_pointer(v)
            for i in range(num_args):
                args.append(self._memory[address + i + 1])   
            modes = v[:-2]   
            while len(modes) < num_args:
                modes = '0' + modes     
            if(instruction == self.jump_if_false or instruction == self.jump_if_true):
                jumped, update = instruction(address, modes, args)
                if jumped:
                    address = int(update)
                    continue
            else:
                instruction(address, modes, args)
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


    def jump_if_true(self, address, modes, args):
        p1 = int(self._memory[int(args[0])]) if modes[1] == '0' else int(args[0])
        p2 = int(self._memory[int(args[1])]) if modes[0] == '0' else int(args[1])
        if p1 != 0:
            return True, p2
        return False, address


    def jump_if_false(self, address, modes, args):
        p1 = int(self._memory[int(args[0])]) if modes[1] == '0' else int(args[0])
        p2 = int(self._memory[int(args[1])]) if modes[0] == '0' else int(args[1])
        if p1 == 0:
            return True, p2
        return False, address

    def less_than(self, address, modes, args):
        p1 = int(self._memory[int(args[0])]) if modes[2] == '0' else int(args[0])
        p2 = int(self._memory[int(args[1])]) if modes[1] == '0' else int(args[1])
        if p1 < p2:
            self._memory[int(args[2])] = '1'
        else:
            self._memory[int(args[2])] = '0'


    def equals(self, address, modes, args):
        p1 = int(self._memory[int(args[0])]) if modes[2] == '0' else int(args[0])
        p2 = int(self._memory[int(args[1])]) if modes[1] == '0' else int(args[1])
        if p1 == p2:
            self._memory[int(args[2])] = '1'
        else:
            self._memory[int(args[2])] = '0'

    def mul(self, address, modes, args):
        p1 = int(self._memory[int(args[0])]) if modes[2] == '0' else int(args[0])
        p2 = int(self._memory[int(args[1])]) if modes[1] == '0' else int(args[1])
        output = p1 * p2
        self._memory[int(args[2])] = str(output)

    def add(self, address, modes, args):
        p1 = int(self._memory[int(args[0])]) if modes[2] == '0' else int(args[0])
        p2 = int(self._memory[int(args[1])]) if modes[1] == '0' else int(args[1])
        output = p1 + p2

        self._memory[int(args[2])] = str(output)

    def get_input(self, address, modes, args):
        p1 = int(args[0])
        self._memory[p1] = input("Input value: ")

    def output(self, address, modes, args):
        p1 = int(self._memory[int(args[0])]) if modes[0] == '0' else int(args[0])
        print( p1 )

    def abort(self, address, modes, args):
        exit(0)

if __name__ == "__main__":
    with open('../input/input_5.txt') as f:
        line = f.read()
        memory = line.split(',')
    computer = Computer(memory)
    computer.run()