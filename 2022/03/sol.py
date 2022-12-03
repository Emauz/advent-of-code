#!/usr/bin/env python3

filename = "input.txt"
#filename = "1.txt"

with open(filename) as f:
    lines = f.readlines()

def priority(item):
    item = ord(item)
    if(item > ord('a')):
        priority = item - ord('a')
        priority += 1
    else:
        priority = item - ord('A')
        priority += 27
    return priority
    
def parse():
    bags = []
    for line in lines:
        line = line.strip()
        bags.append(line)
    return bags

def part2(bags):
    sum = 0
    for i in range(0, len(bags), 3):
        same = set.intersection(set(bags[i]), set(bags[i+1]), set(bags[i+2]))
        same = list(same)[0]
        sum += priority(same)
    return sum

def part1(bags):
    sum = 0
    for bag in bags:
        middle = len(bag) // 2
        first = set(bag[:middle])
        second = set(bag[middle:])
        same = list(first & second)[0]
        sum += priority(same)
    return sum


bags = parse()
print(part1(bags))
print(part2(bags))
