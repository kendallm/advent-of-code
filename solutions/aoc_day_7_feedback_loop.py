from aoc_day_7 import Computer

if __name__ == "__main__":
    sum = 0
    with open("../input/input_7.txt") as f:
        memory = f.read()
    # memory = '3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10'
    memory = memory.split(',')
    amps = [Computer(memory.copy()),
        Computer(memory.copy()),
        Computer(memory.copy()),
        Computer(memory.copy()),
        Computer(memory.copy())]

    i = 0
    can_run = {}
    for amp in amps:
        i += 1
        can_run[amp] = True
        amp.set_name(str(i))
    
    have_runable = True
    while(have_runable):
        for amp in amps:
            if can_run[amp]:
                can_run[amp] = amp.run()
                amp._done = False
        
        if True in can_run.values():
            have_runable = True
        else:
            have_runable = False
    

