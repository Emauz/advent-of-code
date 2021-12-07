#!/usr/bin/env python3

import argparse
import numpy as np

# DEFAULT_FILENAME = 'example'
DEFAULT_FILENAME = 'input'

parser = argparse.ArgumentParser(description="AoC day 06")
parser.add_argument('filename', nargs='?', default=DEFAULT_FILENAME)
args = parser.parse_args()

"""
def original_part1(fish, num_generations):
    for i in range(NUM_GENERATIONS):
        new_fish = 0
        for f in range(len(fish)):
            fish[f] -= 1
            if fish[f] < 0:
                fish[f] = 6
                new_fish += 1
        # birth all the new fish!
        fish = np.append(fish, np.full(new_fish, 8))

    return len(fish)
"""


def better_solution(fish, num_generations):
    # count how many fish are at each stage
    adults = np.zeros(7, dtype=int)
    newborns = 0
    toddlers = 0

    # record starting generation
    for f in fish:
        adults[f] += 1
    for i in range(num_generations):
        born_this_gen = adults[0]
        adults = np.roll(adults, -1)
        adults[6] += toddlers
        toddlers = newborns
        newborns = born_this_gen

    return np.sum(adults) + newborns + toddlers


def part1(fish):
    return better_solution(fish, 80)


def part2(fish):
    return better_solution(fish, 256)


def parse_data(filename):
    fish = np.genfromtxt(filename, delimiter=',', dtype=int)
    return fish


fish = parse_data(args.filename)
print(part1(fish))
print(part2(fish))
