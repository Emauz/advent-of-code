#!/usr/bin/env python3

#f = open('1.txt', 'r')
f = open('input.txt', 'r')

def parse():
    elf_calories = []
    current_elf_calories = 0
    for line in f:
        if line == '\n':
            elf_calories.append(current_elf_calories)
            current_elf_calories = 0
        else:
            current_elf_calories += int(line)
    elf_calories.append(current_elf_calories)
    return elf_calories

def part1(elf_calories):
    elf_calories = sorted(elf_calories)
    return elf_calories[-1]

def part2(elf_calories):
    elf_calories = sorted(elf_calories)
    return elf_calories[-1] + elf_calories[-2] + elf_calories[-3]

elf_calories = parse()
print(part1(elf_calories))
print(part2(elf_calories))
