#!/usr/bin/env python3

import argparse
import numpy as np

# DEFAULT_FILENAME = 'simple'
# DEFAULT_FILENAME = 'example'
DEFAULT_FILENAME = 'input'

parser = argparse.ArgumentParser(description="AoC day 13")
parser.add_argument('filename', nargs='?', default=DEFAULT_FILENAME)
args = parser.parse_args()


# always folds along x axis
def fold_paper(data, fold_row):
    # print(data)
    for i in range(fold_row):
        for j in range(len(data[0])):
            data[i][j] |= data[(fold_row*2)-(i)][j]
    data = data[:fold_row]
    return data


def part1(data, folds):
    if(folds[0][0] == 'x'):
        data = data.T
    data = fold_paper(data, folds[0][1])

    return np.count_nonzero(data)


def part2(data, folds):
    for fold in folds:
        if(fold[0] == 'x'):
            data = data.T
            data = fold_paper(data, fold[1])
            data = data.T
        else:
            data = fold_paper(data, fold[1])

    # print out data at end
    for line in data:
        for ch in line:
            ch = ('#' if ch else ' ')
            print(ch, end='')
        print()


def parse_data(filename):
    raw = open(filename).read()
    raw = raw.split('\n\n')
    # Create paper grid
    coords = raw[0].split('\n')
    coords = [(int(x.split(',')[0]), int(x.split(',')[1])) for x in coords]
    grid = np.zeros((2000, 2000), dtype=int)
    for x, y in coords:
        grid[y][x] = True
    # grid = np.trim_zeros(grid, 'b')

    # Create list of folds
    folds = raw[1].split('\n')[:-1]
    folds = [(x.split('=')[0][-1], int(x.split('=')[1])) for x in folds]

    return grid, folds


grid, folds = parse_data(args.filename)
print(part1(grid, folds))
part2(grid, folds)
