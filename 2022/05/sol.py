#!/usr/bin/env python3

filename = "input.txt"
#filename = "1.txt"

with open(filename) as f:
    data = f.read()

def parse():
    moves = []
    split_data = data.split('\n\n')
    stacks = split_data[0].split('\n')
    commands = split_data[1].split('\n')

    # first, handle the stacks
    column_ids = stacks[-1].split()
    # cast column ids to 0-indexed integers
    column_ids = map(lambda x: int(x) - 1, column_ids) 
    max_stack_size = len(stacks) - 1
    columns = []
    for id in column_ids:
        # make a stack for this column
        columns.append([])
        # iterate through the columns from bottom up
        for stack_idx in range(max_stack_size-1, -1, -1):
            box = stacks[stack_idx][(id*4)+1]
            if(box == ' '):
                break
            columns[id].append(box)

    # then, handle commands
    for line in commands:
        line = line.strip().split()
        if(len(line) != 6):
            # make sure we aren't trying to parse any non-command lines
            continue
        num = int(line[1])
        src = int(line[3])
        dst = int(line[5])
        moves.append((num, src, dst))
    return columns, moves

def part1(columns, moves):
    for num, src, dst in moves:
        for i in range(num):
            columns[dst-1].append(columns[src-1].pop())
    # get first letter in each stack
    result = ''
    for column in columns:
        result += column[-1]
    return result

def part2(columns, moves):
    tmp = []
    for num, src, dst in moves:
        for i in range(num):
            tmp.append(columns[src-1].pop())
        for i in range(num):
            columns[dst-1].append(tmp.pop())
    # get first letter in each stack
    result = ''
    for column in columns:
        result += column[-1]
    return result

columns, moves = parse()
print(part1(columns, moves))
columns, moves = parse()
print(part2(columns, moves))
