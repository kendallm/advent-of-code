class Computer:
    def __init__(self, memory):
        self._memory = memory
        self._name = "Default"
        super().__init__()
        self._done = False
        self._address = 0

    def set_name(self, name):
        self._name = name

    def run(self):
        while self._address < len(self._memory) and not self._done:
            v = self._memory[self._address]
            args = []
            (instruction, num_args) = self.get_instruction_pointer(v)
            for i in range(num_args):
                args.append(self._memory[self._address + i + 1])
            modes = v[:-2]
            while len(modes) < num_args:
                modes = "0" + modes
            if instruction == self.jump_if_false or instruction == self.jump_if_true:
                jumped, update = instruction(self._address, modes, args)
                if jumped:
                    self._address = int(update)
                    continue
            else:
                if instruction(self._address, modes, args) == 0:
                    return
            self._address = self._address + num_args + 1
        return self._address <= len(self._memory)

    def get_instruction_pointer(self, intcode):
        intcode = intcode.strip()
        if len(intcode) == 1:
            intcode = "0" + intcode
        instruction = intcode[-2:]

        if len(instruction) < 2:
            instruction = "0" + instruction

        if instruction == "99":
            return (self.abort, 0)
        elif instruction == "01":
            return (self.add, 3)
        elif instruction == "02":
            return (self.mul, 3)
        elif instruction == "03":
            return (self.get_input, 1)
        elif instruction == "04":
            return (self.output, 1)
        elif instruction == "05":
            return (self.jump_if_true, 2)
        elif instruction == "06":
            return (self.jump_if_false, 2)
        elif instruction == "07":
            return (self.less_than, 3)
        elif instruction == "08":
            return (self.equals, 3)
        else:
            raise ValueError("Invalid instruction", instruction)

    def jump_if_true(self, address, modes, args):
        p1 = int(self._memory[int(args[0])]) if modes[1] == "0" else int(args[0])
        p2 = int(self._memory[int(args[1])]) if modes[0] == "0" else int(args[1])
        if p1 != 0:
            return True, p2
        return False, address

    def jump_if_false(self, address, modes, args):
        p1 = int(self._memory[int(args[0])]) if modes[1] == "0" else int(args[0])
        p2 = int(self._memory[int(args[1])]) if modes[0] == "0" else int(args[1])
        if p1 == 0:
            return True, p2
        return False, address

    def less_than(self, address, modes, args):
        p1 = int(self._memory[int(args[0])]) if modes[2] == "0" else int(args[0])
        p2 = int(self._memory[int(args[1])]) if modes[1] == "0" else int(args[1])
        if p1 < p2:
            self._memory[int(args[2])] = "1"
        else:
            self._memory[int(args[2])] = "0"

    def equals(self, address, modes, args):
        p1 = int(self._memory[int(args[0])]) if modes[2] == "0" else int(args[0])
        p2 = int(self._memory[int(args[1])]) if modes[1] == "0" else int(args[1])
        if p1 == p2:
            self._memory[int(args[2])] = "1"
        else:
            self._memory[int(args[2])] = "0"

    def mul(self, address, modes, args):
        p1 = int(self._memory[int(args[0])]) if modes[2] == "0" else int(args[0])
        p2 = int(self._memory[int(args[1])]) if modes[1] == "0" else int(args[1])
        output = p1 * p2
        self._memory[int(args[2])] = str(output)

    def add(self, address, modes, args):
        p1 = int(self._memory[int(args[0])]) if modes[2] == "0" else int(args[0])
        p2 = int(self._memory[int(args[1])]) if modes[1] == "0" else int(args[1])
        output = p1 + p2

        self._memory[int(args[2])] = str(output)

    def get_input(self, address, modes, args):
        p1 = int(args[0])
        self._memory[p1] = input(f"Input value for {self._name}: \n")

    def output(self, address, modes, args):
        p1 = int(self._memory[int(args[0])]) if modes[0] == "0" else int(args[0])
        self._done = True

        print(p1)

    def abort(self, address, modes, args):
        self._done = True
        return 0
