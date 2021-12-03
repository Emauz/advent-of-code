#!/usr/bin/env python3

f = open('input', 'r')
# f = open('example', 'r')


def part1():
    hor = 0
    vert = 0

    for line in f:
        line = line.split(' ')
        dir = line[0]
        magnitude = int(line[1])
        if(dir == 'forward'):
            hor += magnitude
        elif(dir == 'down'):
            vert += magnitude
        elif(dir == 'up'):
            vert -= magnitude

    return hor * vert


def part2():
    hor = 0
    vert = 0
    aim = 0

    for line in f:
        line = line.split(' ')
        dir = line[0]
        magnitude = int(line[1])
        if(dir == 'forward'):
            hor += magnitude
            vert += magnitude * aim
        elif(dir == 'down'):
            aim += magnitude
        elif(dir == 'up'):
            aim -= magnitude

    return hor * vert


print(part1())
f.seek(0)
print(part2())
