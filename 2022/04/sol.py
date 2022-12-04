#!/usr/bin/env python3

filename = "input.txt"
#filename = "1.txt"

with open(filename) as f:
    lines = f.readlines()

def parse():
    pairs = []
    for line in lines:
        line = line.strip()
        a, b = line.split(',') # split pairs
        a = a.split('-') # split each pair into its two numbers
        b = b.split('-')
        a = range(int(a[0]), int(a[1])+1) # create Range object for each elf
        b = range(int(b[0]), int(b[1])+1)
        pairs.append((a, b))
    return pairs

def is_overlapping(a, b) -> bool:
    # check if a is inside b
    if(a.start >= b.start and a.stop <= b.stop):
        return True
    # check if b is inside a
    if(b.start >= a.start and b.stop <= a.stop):
        return True
    return False

def part1(parsed):
    result = 0
    for a, b in parsed:
        if(is_overlapping(a, b)):
            result += 1
    return result

def part2(parsed):
    result = 0
    for a, b in parsed:
        if(len(set.intersection(set(a), set(b))) > 0):
            result += 1
    return result

parsed = parse()
print(part1(parsed))
print(part2(parsed))
