#!/usr/bin/env python3

import argparse
import numpy as np

DEFAULT_FILENAME = 'input'

parser = argparse.ArgumentParser(description="AoC day 03")
parser.add_argument('filename', nargs='?', default=DEFAULT_FILENAME)
args = parser.parse_args()


def part1(grid):
    # count number of '1' elements in each column
    one_counts = np.count_nonzero(grid, axis=0)
    # calculate gamma and epsilon boolean arrays
    num_entries = np.ma.size(grid, axis=0)
    gamma = (one_counts > (num_entries // 2))
    epsilon = (gamma == False)  # bitwise inverse of gamma
    # convert boolean arrays to numbers
    gamma = gamma.dot(1 << np.arange(gamma.size)[::-1])
    epsilon = epsilon.dot(1 << np.arange(epsilon.size)[::-1])
    power_consumption = gamma * epsilon
    return power_consumption


# calculate rating value for part 2, specifying if majority is
# number of ones (O2) or number of zeroes (CO2)
def rating_value_calculation(grid, majority_one: bool):
    current_col = 0
    # while we have more than one row to choose from
    while(np.ma.size(grid, axis=0) > 1):
        # count number of '1' elements in each column
        one_counts = np.count_nonzero(grid, axis=0)[current_col]
        zero_counts = np.ma.size(grid, axis=0) - one_counts
        # calculate most common value for current col
        val = (one_counts >= zero_counts) ^ majority_one
        # filter grid to rows where column has specified value
        grid = (grid[grid[:, current_col] == val])
        current_col += 1
    grid = grid[0]
    grid = grid.dot(1 << np.arange(grid.size)[::-1])
    return grid


def part2(grid):
    O2 = rating_value_calculation(grid, True)
    CO2 = rating_value_calculation(grid, False)

    return O2 * CO2


def clean_data(filename):
    grid = np.genfromtxt(filename, delimiter=1, dtype=int)
    grid = (grid == 1)  # convert to boolean array
    return grid


grid = clean_data(args.filename)

print(part1(grid))
print(part2(grid))
