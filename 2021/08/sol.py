#!/usr/bin/env python3

import argparse

# DEFAULT_FILENAME = 'example'
# DEFAULT_FILENAME = 'example2'
DEFAULT_FILENAME = 'input'

parser = argparse.ArgumentParser(description="AoC day 08")
parser.add_argument('filename', nargs='?', default=DEFAULT_FILENAME)
args = parser.parse_args()

map = [
    [' ', 'a', 'a', 'a', 'a', ' '],
    ['b', ' ', ' ', ' ', ' ', 'c'],
    ['b', ' ', ' ', ' ', ' ', 'c'],
    [' ', 'd', 'd', 'd', 'd', ' '],
    ['e', ' ', ' ', ' ', ' ', 'f'],
    ['e', ' ', ' ', ' ', ' ', 'f'],
    [' ', 'g', 'g', 'g', 'g', ' ']
]

number_configs = {
    'abcefg'    : 0,
    'cf'        : 1,
    'acdeg'     : 2,
    'acdfg'     : 3,
    'bcdf'      : 4,
    'abdfg'     : 5,
    'abdefg'    : 6,
    'acf'       : 7,
    'abcdefg'   : 8,
    'abcdfg'    : 9,
}


def part1(data) -> int:
    ones = 0
    fours = 0
    sevens = 0
    eights = 0
    for d in data:
        example_data, output_value = d
        for output in output_value:
            if len(output) == 2:
                ones += 1
            elif len(output) == 3:
                sevens += 1
            elif len(output) == 4:
                fours += 1
            elif len(output) == 7:
                eights += 1

    total = ones + fours + sevens + eights
    return total


def part2(data) -> int:
    running_sum = 0
    # sorted list will be of sizes:
    #  0123456789
    # [2345556667]
    for line in data:
        example_data, output_value = line
        # sort by size of segment list
        example_data = sorted(example_data, key=lambda x: len(x))
        # hard-code each individual solution (the industry standard way)
        # locate C, F
        cf = set(example_data[0])
        # locate B, D
        bd = set(example_data[2]) - cf
        # solve for A
        A = set(example_data[1]) - cf
        # Get verticals
        adg = set(example_data[3]) & set(example_data[4]) & set(example_data[5])
        # locate D
        D = adg & set(example_data[2])
        # Solve for B
        B = bd - D
        # solve for G
        G = (adg - A) - D
        # solve for F
        abfg = set(example_data[6]) & set(example_data[7]) & set(example_data[8])
        F = ((abfg - A) - B) - G
        # solve for C
        C = cf - F
        # solve for E
        E = ((((((set('abcdefg') - A) - B) - C) - D) - F) - G)
        # print(A)
        # print(B)
        # print(C)
        # print(D)
        # print(E)
        # print(F)
        # print(G)
        map = {
            'a': next(iter(A)),
            'b': next(iter(B)),
            'c': next(iter(C)),
            'd': next(iter(D)),
            'e': next(iter(E)),
            'f': next(iter(F)),
            'g': next(iter(G))
        }

        # as debugging, flip keys and values in above dict
        map = dict((v, k) for k, v in map.items())
        # apparently that actually fixed it!

        # Replace elements in original string with mapped values
        num_string = ''
        for output in output_value:
            mapped_string = ''
            for ch in output:
                mapped_string += map[ch]
            mapped_string = ''.join(sorted(mapped_string))
            num_string += str(number_configs[mapped_string])
        running_sum += int(num_string)
    return running_sum


def print_segment_display(segments):
    for line in map:
        for char in line:
            if char == ' ':
                print(' ', end='')
            elif char in segments:
                print(char, end='')
            else:
                print('.', end='')
        print()


def parse_data(filename):
    f = open(filename, 'r')
    data = []
    for line in f:
        line = line.split('|')
        example_data = line[0]
        example_data = example_data.split()
        output_value = line[1]
        output_value = output_value.split()
        data.append((example_data, output_value))

    return data

data = parse_data(args.filename)

print(part1(data))
print(part2(data))
