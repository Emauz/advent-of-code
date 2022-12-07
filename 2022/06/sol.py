#!/usr/bin/env python3

filename = "input.txt"
#filename = "1.txt"

with open(filename) as f:
    lines = f.readlines()

def parse():
    return lines[0]

def solve(parsed, num_unique):
    result = 0
    marker = []
    for i in range(len(parsed)):
        # MOVING WINDOW ALGORITHMS!
        marker.append(parsed[i])
        if(i >= num_unique):
            marker.pop(0)
        if(len(set(marker)) == num_unique):
            return i + 1
    return -1

def part1(parsed):
    return solve(parsed, 4)

def part2(parsed):
    return solve(parsed, 14)

parsed = parse()
print(part1(parsed))
print(part2(parsed))
