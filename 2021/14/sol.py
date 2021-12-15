#!/usr/bin/env python3

import argparse
from collections import Counter

# DEFAULT_FILENAME = 'example'
DEFAULT_FILENAME = 'input'

parser = argparse.ArgumentParser(description="AoC day 14")
parser.add_argument('filename', nargs='?', default=DEFAULT_FILENAME)
args = parser.parse_args()


# slow part 1 solution
def insert(chain, rules):
    output = chain[0]
    for i in range(len(chain) - 1):
        pair = chain[i] + chain[i+1]
        output += rules[pair]
        output += chain[i+1]

    return output


# improved solution for part 2
def insert_part2(pair_counts, char_counts, rules):
    new_pair_counts = {}
    for pair, count in pair_counts.items():
        result1, result2, new_char = rules[pair]
        if result1 not in new_pair_counts:
            new_pair_counts[result1] = 0
        if result2 not in new_pair_counts:
            new_pair_counts[result2] = 0
        if new_char not in char_counts:
            char_counts[new_char] = 0
        new_pair_counts[result1] += count
        new_pair_counts[result2] += count
        char_counts[new_char] += count

    return new_pair_counts, char_counts


def part1(chain, rules):
    for i in range(10):
        chain = insert(chain, rules)

    counts = sorted(list(Counter(chain).values()))
    return counts[-1] - counts[0]


def part2(starting_str, pair_counts, rules):
    # initialize count of all chars in starting string
    char_counts = {}
    for char in starting_str:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    for i in range(40):
        pair_counts, char_counts = insert_part2(pair_counts, char_counts, rules)

    counts = sorted(list(Counter(char_counts).values()))
    return counts[-1] - counts[0]


def parse_data(filename):
    f = open(filename)
    template = list(f.readline().strip())
    f.readline()  # skip one line
    rules = {}
    for line in f:
        line = line.strip().split(' -> ')
        rules[line[0]] = line[1]

    return template, rules


def parse_data_part2(filename):
    f = open(filename)
    template = list(f.readline().strip())
    # create count of each pair in template
    pair_counts = {}
    for i in range(len(template) - 1):
        pair = template[i] + template[i+1]
        if pair not in pair_counts:
            pair_counts[pair] = 1
        else:
            pair_counts[pair] += 1
    f.readline()  # skip one line
    # rules map a single pair to the two pairs that result from it
    rules = {}
    for line in f:
        line = line.strip().split(' -> ')
        result1 = line[0][0] + line[1]
        result2 = line[1] + line[0][1]
        resulting_pairs = (result1, result2, line[1])
        rules[line[0]] = resulting_pairs

    return template, pair_counts, rules


template, rules = parse_data(args.filename)
print(part1(template, rules))

# part 2 completely re-does parsing and implementation
starting_str, pair_counts, rules = parse_data_part2(args.filename)
print(part2(starting_str, pair_counts, rules))
