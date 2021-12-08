#!/usr/bin/env python3

import argparse
import numpy as np
import sys

# DEFAULT_FILENAME = 'example'
DEFAULT_FILENAME = 'input'

parser = argparse.ArgumentParser(description="AoC day 07")
parser.add_argument('filename', nargs='?', default=DEFAULT_FILENAME)
args = parser.parse_args()


# Calculates the cost using the triangular number formula
def calculate_triangular_cost(pos: int, crabs) -> int:
    running_cost = 0
    for c in crabs:
        dist = abs(c - pos)
        running_cost += (dist*(dist+1))//2
    return running_cost


def calculate_linear_cost(pos: int, crabs) -> int:
    running_cost = 0
    for c in crabs:
        running_cost += abs(c - pos)
    return running_cost


def part1(crabs) -> int:
    best_solution = (sys.maxsize, sys.maxsize)
    for i in range(np.max(crabs) + 1):
        current_solution = calculate_linear_cost(i, crabs)
        if(current_solution < best_solution[1]):
            best_solution = (i, current_solution)

    return best_solution[1]


def part2(crabs) -> int:
    best_solution = (sys.maxsize, sys.maxsize)
    for i in range(np.max(crabs) + 1):
        current_solution = calculate_triangular_cost(i, crabs)
        if(current_solution < best_solution[1]):
            best_solution = (i, current_solution)

    return best_solution[1]

    return -1


def parse_data(filename):
    crabs = np.genfromtxt(filename, delimiter=',', dtype=int)
    return crabs


crabs = parse_data(args.filename)
print(part1(crabs))
print(part2(crabs))
