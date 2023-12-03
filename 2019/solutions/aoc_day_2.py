def process_intcode(memory, noun, verb):
    address = 0
    while address < len(memory) - 1:
        instruction = memory[address]
        output = 0
        if instruction == 99:
            return memory
        elif instruction == 1:
            output = memory[memory[address + 1]] + memory[memory[address + 2]]
            memory[memory[address + 3]] = output
        elif instruction == 2:
            output = memory[memory[address + 1]] * memory[memory[address + 2]]
            memory[memory[address + 3]] = output
        else:
            pass
        if output == 19690720:
            print(f"Found output with noun {noun} and verb {verb}")
        address += 4

    return memory


if __name__ == "__main__":
    with open("../input/input_2.txt") as f:
        line = f.read().split(",")
        line = list(map(lambda x: int(x), line))

    for i in range(100):
        for j in range(100):
            memory = line.copy()
            memory[1] = i
            memory[2] = j
            process_intcode(memory, i, j)
