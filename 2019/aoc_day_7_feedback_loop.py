from aoc_day_7 import Computer

if __name__ == "__main__":
    sum = 0
    with open("../input/input_7.txt") as f:
        memory = f.read()
    memory = memory.split(",")
    amps = [
        Computer(memory.copy()),
        Computer(memory.copy()),
        Computer(memory.copy()),
        Computer(memory.copy()),
        Computer(memory.copy()),
    ]

    i = 0
    can_run = {}
    for amp in amps:
        i += 1
        can_run[amp] = True
        amp.set_name(str(i))

    have_runable = True
    while have_runable:
        for amp in amps:
            if can_run[amp]:
                can_run[amp] = amp.run()
                amp._done = False

        if True in can_run.values():
            have_runable = True
        else:
            have_runable = False
