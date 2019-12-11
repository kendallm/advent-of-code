from collections import defaultdict, deque
class Computer:

    def __init__(self, memory, output, pauses):
        memory = memory.split(',')
        self._memory = defaultdict(int)
        for i in range(len(memory)):
            self._memory[i] = memory[i]
        self._name = "Default"
        super().__init__()
        self._default_pauses = pauses
        self._halted = False
        self._address = 0
        self._base = 0
        self._pauses = pauses
        self._paused = True
        self._input = deque()
        self._output = output

    def set_name(self, name):
        self._name = name

    def add_input(self, item):
        self._input.append(item)
    
    def run(self):
        self._pauses = self._default_pauses
        self._paused = False
        while not self._halted and not self._paused:
            v = self._memory[self._address]
            args = []
            (instruction, num_args) = self.get_instruction_pointer(v)
            for i in range(num_args):
                args.append(self._memory[self._address + i + 1])   
            modes = v[:-2]   
            while len(modes) < num_args:
                modes = '0' + modes     
            if(instruction == self.jump_if_false or instruction == self.jump_if_true):
                jumped, update = instruction(self._address, modes, args)
                if jumped:
                    self._address = int(update)
                    continue
            else:
                if instruction(self._address, modes, args) == 0:
                    return
            self._address = self._address + num_args + 1
                
    def get_instruction_pointer(self, intcode):
        intcode = intcode.strip()
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
        elif instruction == '09':
            return (self.adjust_base, 1)
        else:
            raise ValueError("Invalid instruction", instruction)

    
    def adjust_base(self, address, modes, args):
        p1 = int(self._memory[int(args[0])]) if modes[0] == '0' else int(args[0])
        p1 = int(self._memory[self._base + int(args[0])]) if modes[0] == '2' else p1
        self._base += int(p1)

    def jump_if_true(self, address, modes, args):
        p1 = int(self._memory[int(args[0])]) if modes[1] == '0' else int(args[0])
        p1 = int(self._memory[self._base + int(args[0])]) if modes[1] == '2' else p1
        
        p2 = int(self._memory[int(args[1])]) if modes[0] == '0' else int(args[1])
        p2 = int(self._memory[self._base + int(args[1])]) if modes[0] == '2' else p2
        if p1 != 0:
            return True, p2
        return False, address


    def jump_if_false(self, address, modes, args):
        p1 = int(self._memory[int(args[0])]) if modes[1] == '0' else int(args[0])
        p1 = int(self._memory[self._base + int(args[0])]) if modes[1] == '2' else p1
        p2 = int(self._memory[int(args[1])]) if modes[0] == '0' else int(args[1])
        p2 = int(self._memory[self._base + int(args[1])]) if modes[0] == '2' else p2
        if p1 == 0:
            return True, p2
        return False, address

    def less_than(self, address, modes, args):
        p1 = int(self._memory[int(args[0])]) if modes[2] == '0' else int(args[0])
        p1 = int(self._memory[self._base + int(args[0])]) if modes[2] == '2' else p1
        p2 = int(self._memory[int(args[1])]) if modes[1] == '0' else int(args[1])
        p2 = int(self._memory[self._base + int(args[1])]) if modes[1] == '2' else p2
        
        idx = int(args[2])
        if modes[0] == '2':
            idx = idx + self._base
            
        if p1 < p2:
            self._memory[idx] = '1'
        else:
            self._memory[idx] = '0'


    def equals(self, address, modes, args):
        p1 = int(self._memory[int(args[0])]) if modes[2] == '0' else int(args[0])
        p1 = int(self._memory[self._base + int(args[0])]) if modes[2] == '2' else p1
        p2 = int(self._memory[int(args[1])]) if modes[1] == '0' else int(args[1])
        p2 = int(self._memory[self._base + int(args[1])]) if modes[1] == '2' else p2
        
        idx = int(args[2])
        if modes[0] == '2':
            idx = idx + self._base
            
        if p1 == p2:
            self._memory[idx] = '1'
        else:
            self._memory[idx] = '0'

    def mul(self, address, modes, args):
        p1 = int(self._memory[int(args[0])]) if modes[2] == '0' else int(args[0])
        p1 = int(self._memory[self._base + int(args[0])]) if modes[2] == '2' else p1
        p2 = int(self._memory[int(args[1])]) if modes[1] == '0' else int(args[1])
        p2 = int(self._memory[self._base + int(args[1])]) if modes[1] == '2' else p2
        output = p1 * p2
        
        idx = int(args[2])
        if modes[0] == '2':
            idx = idx + self._base
        self._memory[idx] = str(output)

    def add(self, address, modes, args):
        p1 = int(self._memory[int(args[0])]) if modes[2] == '0' else int(args[0])
        p1 = int(self._memory[self._base + int(args[0])]) if modes[2] == '2' else p1
        p2 = int(self._memory[int(args[1])]) if modes[1] == '0' else int(args[1])
        p2 = int(self._memory[self._base + int(args[1])]) if modes[1] == '2' else p2
        output = p1 + p2
        idx = int(args[2])
        if modes[0] == '2':
            idx = idx + self._base
        self._memory[idx] = str(output)

    def get_input(self, address, modes, args):
        p1 = int(args[0])
        if modes[0] == '2':
            p1 += self._base

        self._memory[p1] = self._input.popleft()

    def output(self, address, modes, args):
        p1 = int(self._memory[int(args[0])]) if modes[0] == '0' else int(args[0])
        p1 = int(self._memory[self._base + int(args[0])]) if modes[0] == '2' else p1
        self._pauses -= 1
        if self._pauses == 0:
            self._paused = True
        self._output.append(p1)

    def abort(self, address, modes, args):
        self._halted = True
        return 0