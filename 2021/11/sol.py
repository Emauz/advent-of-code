#!/usr/bin/env python3

import argparse
import numpy as np

# DEFAULT_FILENAME = 'example2'
# DEFAULT_FILENAME = 'example'
DEFAULT_FILENAME = 'input'

parser = argparse.ArgumentParser(description="AoC day 11")
parser.add_argument('filename', nargs='?', default=DEFAULT_FILENAME)
args = parser.parse_args()


def calculate_flashes(grid) -> int:
    grid = grid + 1
    recently_flashed = True
    num_flashed = 0
    while(recently_flashed):
        recently_flashed = False
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if(val > 9):
                    # Current squid will flash
                    num_flashed += 1
                    grid[i][j] = 0
                    recently_flashed = True
                    # Increase all neighboring squid energy by 1
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            # make sure we don't re-flash a squid
                            try:
                                # hacky: prevents int underflow accesses
                                if i+di == -1 or j+dj == -1:
                                    continue
                                if grid[i+di][j+dj] != 0:
                                    grid[i+di][j+dj] += 1
                            except IndexError:
                                pass
    return grid, num_flashed


def part1(grid):
    answer = 0
    for i in range(100):
        grid, num_flashed = calculate_flashes(grid)
        answer += num_flashed
        # print(f'\nAfter step {i+1}:')
        # print(np.array_str(grid).replace('[', '').replace(' ', '').replace(']', ''))
    return answer


def part2(grid):
    steps = 0
    while grid.sum() != 0:
        grid, num_flashed = calculate_flashes(grid)
        steps += 1

    return steps


def parse_data(filename):
    # split line into individual chars
    def split(line):
        return [int(char) for char in line[:-1]]

    grid = []
    with open(filename) as f:
        for line in f:
            grid.append(split(line))

    grid = np.array(grid, dtype=int)
    return grid


grid = parse_data(args.filename)
print(part1(grid))
print(part2(grid))
