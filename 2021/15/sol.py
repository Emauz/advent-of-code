#!/usr/bin/env python3

import sys
import argparse
from queue import PriorityQueue
import numpy as np

# DEFAULT_FILENAME = 'simple'
# DEFAULT_FILENAME = 'example'
DEFAULT_FILENAME = 'input'

parser = argparse.ArgumentParser(description="AoC day 15")
parser.add_argument('filename', nargs='?', default=DEFAULT_FILENAME)
args = parser.parse_args()


def djikstra(grid, starting_coords, target_coords):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, starting_coords))
    while not queue.empty():
        cost, coords = queue.get()
        visited.add(coords)
        if(coords == target_coords):
            return grid

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            x = coords[0] + dx
            y = coords[1] + dy
            if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
                continue
            if (x, y) in visited:
                continue
            # for each valid, unvisited neighbor
            old_cost = grid[x][y][1]
            new_cost = cost + grid[x][y][0]
            if new_cost < old_cost:
                grid[x][y][1] = new_cost
                grid[x][y][2] = coords  # prev node is us
                queue.put((new_cost, (x, y)))

    print("Error: djikstra's algorithm terminated without reaching target coords")
    exit(1)


def part1(grid):
    grid = prep_data(grid)
    grid = djikstra(grid, (0, 0), (len(grid[0])-1, len(grid)-1))
    return grid[-1][-1][1]  # return the djikstra calculated cost of target element


def part2(grid):
    grid = expand_grid(grid)
    grid = prep_data(grid)
    grid = djikstra(grid, (0, 0), (len(grid[0])-1, len(grid)-1))
    return grid[-1][-1][1]  # return the djikstra calculated cost of target element


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


def prep_data(grid):
    grid = [[[x, sys.maxsize, None] for x in row] for row in grid]
    return grid


def expand_grid(grid):
    base_grid = grid
    # expand horizontally
    for i in range(1, 5):
        newarray = base_grid.copy()
        newarray += i
        grid = np.concatenate((grid, newarray), axis=1)
        grid -= 1
        grid %= 9
        grid += 1
    # expand vertically
    base_grid = grid
    for i in range(1, 5):
        newarray = base_grid.copy()
        newarray = newarray + i
        grid = np.concatenate((grid, newarray), axis=0)
        grid -= 1
        grid %= 9
        grid += 1
    return grid


grid = parse_data(args.filename)
print(part1(grid))
print(part2(grid))
