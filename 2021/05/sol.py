#!/usr/bin/env python3

import argparse
import numpy as np

# DEFAULT_FILENAME = 'example'
DEFAULT_FILENAME = 'input'

parser = argparse.ArgumentParser(description="AoC day 03")
parser.add_argument('filename', nargs='?', default=DEFAULT_FILENAME)
args = parser.parse_args()


def part1(grid):
    count = (grid > 1).sum()

    return count


def part2(grid):
    count = (grid > 1).sum()

    return count


def parse_data(filename, parse_diags: bool):
    f = open(filename)
    grid = np.zeros((1000, 1000), dtype=int)
    for line in f:
        line = line.split(' -> ')
        start = eval(line[0])
        end = eval(line[1])
        if start[0] == end[0]:
            # line is vertical
            direction = 1 if start[1] < end[1] else -1
            for y in range(start[1], end[1] + direction, direction):
                grid[y][start[0]] += 1
        elif start[1] == end[1]:
            # line is horizontal
            direction = 1 if start[0] < end[0] else -1
            for x in range(start[0], end[0] + direction, direction):
                grid[start[1]][x] += 1
        elif parse_diags:
            # line is diagonal
            x_dir = 1 if start[0] < end[0] else -1
            y_dir = 1 if start[1] < end[1] else -1
            x_coords = list(range(start[0], end[0] + x_dir, x_dir))
            y_coords = list(range(start[1], end[1] + y_dir, y_dir))
            for (x, y) in zip(x_coords, y_coords):
                grid[y][x] += 1

    return grid


grid = parse_data(args.filename, False)
print(part1(grid))

grid = parse_data(args.filename, True)
print(part2(grid))
