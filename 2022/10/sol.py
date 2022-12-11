#!/usr/bin/env python3

filename = "input.txt"
#filename = "1.txt"
#filename = "2.txt"

with open(filename) as f:
    input_lines = f.readlines()

class CPU(object):
    def __init__(self, lines):
        # registers
        self.x = 1
        # CPU state
        self.ticks = 1
        #self.pc = 1
        self.pipeline = []
        # parse program
        self.program = []
        for line in lines:
            line = line.strip().split()
            self.program.append(line)

    def execute_microcode(self, microcode):
        if(microcode[0] == 'noop'):
            return
        elif(microcode[0] == 'addx'):
            self.x += int(microcode[1])

    # returns if tick was successful
    def tick(self):
        if(len(self.pipeline) == 0):
            #self.pc += 1
            if(len(self.program) == 0):
                return False
            # add next command in the program to the pipeline
            op = self.program.pop(0)
            if(op[0] == 'noop'):
                self.pipeline.append(['noop'])
            elif(op[0] == 'addx'):
                self.pipeline.append(['noop'])
                self.pipeline.append(['addx', op[1]])
        # take operation off the pipeline
        micro_op = self.pipeline.pop(0)
        self.execute_microcode(micro_op)
        self.ticks += 1
        return True


def part1(cpu):
    res = 0
    #while(cpu.tick()):
        #print(f"end of tick: {cpu.ticks}, x: {cpu.x}")
        #print()
    #return

    while(cpu.tick()):
        if((cpu.ticks - 20) % 40 == 0):
            res += (cpu.ticks * cpu.x)
    return res

def part2(cpu):
    for row in range(6):
        for col in range(40):
            if(abs(cpu.x - col) <= 1):
                print('#', end='')
            else:
                print('.', end='')
            cpu.tick()
        print()
    res = 0
    return res

def main():
    cpu = CPU(input_lines)
    print(part1(cpu))
    cpu = CPU(input_lines)
    print(part2(cpu))

if __name__ == '__main__':
    main()
