#!/usr/bin/env python3

import argparse
import numpy as np

# DEFAULT_FILENAME = 'simple'
# DEFAULT_FILENAME = 'example'
DEFAULT_FILENAME = 'input'

parser = argparse.ArgumentParser(description="AoC day 09")
parser.add_argument('filename', nargs='?', default=DEFAULT_FILENAME)
args = parser.parse_args()


def local_minimum(i: int, j: int, grid) -> bool:
    center_val = grid[i][j]
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            try:
                if grid[i+di][j+dj] <= center_val:
                    return False
            except IndexError:
                continue
    return True


def part1(grid):
    answer = 0

    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if(local_minimum(i, j, grid)):
                risk_level = val + 1
                answer += risk_level

    return answer


def calculate_basin(initial_i: int, initial_j: int, grid) -> int:
    size = 0
    memoized_coords = []
    queue = [(initial_i, initial_j)]  # start with center of basin
    while len(queue) >= 1:
        i, j = queue.pop(0)
        if((i, j) in memoized_coords):
            continue
        if(grid[i][j] == 9):
            continue
        if(i < 0 or j < 0):
            continue
        size += 1
        memoized_coords.append((i, j))
        # add all adjacent vents
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                if abs(di * dj) == 1:
                    continue
                try:
                    if(grid[i+di][j+dj] == 9):
                        continue
                    queue.append((i+di, j+dj))
                except IndexError:
                    continue

    return size


def part2(grid):
    basin_sizes = []

    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if(local_minimum(i, j, grid)):
                basin_sizes.append(calculate_basin(i, j, grid))

    basin_sizes = sorted(basin_sizes)
    answer = np.prod(basin_sizes[-3:])
    return answer


def parse_data(filename):
    # split line into individual chars
    def split(line):
        return [int(char) for char in line[:-1]]

    grid = []
    with open(filename) as f:
        for line in f:
            grid.append(split(line))

    return grid


grid = parse_data(args.filename)
print(part1(grid))
print(part2(grid))
