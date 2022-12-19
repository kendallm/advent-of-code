import sys
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


class Cpu:

    def __init__(self, lines):
        self.register = 1
        self.cycles = [1]
        self.instructions = self._parse_instructions(lines)

    def _parse_instructions(self, lines):
        instructions = []
        for line in lines:
            if line == "noop":
                instructions.append((line, 0))
            else:
                instruction, number = line.split()
                instructions.append((instruction, int(number)))
        return instructions

    def run(self):
        for i, instruction in enumerate(self.instructions):
            if instruction[0] == "noop":
                self.cycles.append(self.register)
                continue
            self.cycles.append(self.register)
            self.cycles.append(self.register)
            self.register += instruction[1]


def main():
    lines = ProblemParser().load_input(2022, 10)
    cpu = Cpu(lines)
    cpu.run()
    res = sum([
        cpu.cycles[20] * 20,
        cpu.cycles[60] * 60,
        cpu.cycles[100] * 100,
        cpu.cycles[140] * 140,
        cpu.cycles[180] * 180,
        cpu.cycles[220] * 220
    ])
    print(res)
    print(get_crt_image(cpu))


def get_crt_image(cpu):
    count = 0
    image = ""
    for i, v in enumerate(cpu.cycles[1:]):
        sprite_start = v - 1
        sprite_end = v + 1
        if sprite_start <= count <= sprite_end:
            image += "#"
        else:
            image += "."
        count = (count + 1) % 40
        if count == 0:
            image += '\n'
    return image


if __name__ == '__main__':
    main()
