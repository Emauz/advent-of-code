#!/usr/bin/env python3

import sys

import numpy as np

from pprint import pprint

filename = "input.txt"
#filename = "1.txt"

with open(filename) as f:
    input_lines = f.readlines()

def parse(lines, part2=False):
    highest_row = 0
    rocks = []
    for line in lines:
        line = line.strip().split(' -> ')
        rock_trace = []
        for element in line:
            element = element.split(',')
            col = int(element[0])
            row = int(element[1])
            if(row > highest_row):
                highest_row = row
            rock_trace.append((col, row))
        rocks.append(rock_trace)

    # from all the rock traces, build the cave structure
    cave = np.full((1000, 1000), '.')
    for rock_trace in rocks:
        prev_col = rock_trace[0][0]
        prev_row = rock_trace[0][1]
        for col, row in rock_trace[1:]:
            #print(prev_col, prev_row)
            #print(col, row)
            if col == prev_col:
                # moving vertical
                step = +1 if row < prev_row else -1
                for r in range(row, prev_row+step, step):
                    #print(f"setting row:{r}, col:{col}")
                    cave[r][col] = '#'
            else:
                # moving horizontal
                step = +1 if col < prev_col else -1
                for c in range(col, prev_col+step, step):
                    #print(f"setting row:{row}, col:{c}")
                    cave[row][c] = '#'
            prev_col = col
            prev_row = row
    if part2:
        for i in range(1000):
            cave[highest_row+2][i] = '#'
    return cave

# drops a single grain of sand. returns if the sand settled
def drop_sand(cave) -> bool:
    if(cave[0][500] != '.'):
        return False
    row = 0
    col = 500
    while(row < 900):
        if(cave[row+1][col] == '.'):
            row += 1
        elif(cave[row+1][col-1] == '.'):
            row += 1
            col -= 1
        elif(cave[row+1][col+1] == '.'):
            row += 1
            col += 1
        else:
            # Sand has settled here
            cave[row][col] = 'o'
            return True
    return False

def solve(cave):
    num_grains = 0
    while(drop_sand(cave)):
        num_grains += 1
    return num_grains

def main():
    cave = parse(input_lines)
    print(solve(cave))
    cave = parse(input_lines, part2=True)
    print(solve(cave))

if __name__ == '__main__':
    main()
