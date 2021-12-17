#!/usr/bin/env python3

import argparse
import numpy as np

# DEFAULT_FILENAME = 'example'
# DEFAULT_FILENAME = 'example2'
# DEFAULT_FILENAME = 'example4'
# DEFAULT_FILENAME = 'example5'
# DEFAULT_FILENAME = 'example6'
# DEFAULT_FILENAME = 'example7'
DEFAULT_FILENAME = 'input'

parser = argparse.ArgumentParser(description="AoC day 16")
parser.add_argument('filename', nargs='?', default=DEFAULT_FILENAME)
args = parser.parse_args()

version_sum = 0

hex_map = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}


def parse_header(bit_str) -> (int, int, bool, int, []):
    version = int(bit_str[0:3], 2)
    global version_sum
    version_sum += version
    type = int(bit_str[3:6], 2)
    if type == 4:
        return (version, type, None, None, bit_str[6:])

    # parse out payload length
    length_type = (bit_str[6] == '1')
    if length_type:
        length = int(bit_str[7:18], 2)
        bit_str = bit_str[18:]
    else:
        length = int(bit_str[7:22], 2)
        bit_str = bit_str[22:]

    # print('PARSED HEADER')
    # print(f'version: {version}')
    # print(f'type: {type}')
    # print(f'length_type: {length_type}')
    # print(f'length: {length}')
    # print(f'bit_str: {bit_str}')
    return (version, type, length_type, length, bit_str)


def parse_packet(bit_str):  # return count of bits
    # print(f'parsing <{bit_str}>')
    if not bit_str:
        return ''
    version, type, length_type, length, bit_str = parse_header(bit_str)
    if type == 4:
        bit_str, val = parse_literal(bit_str)
        return bit_str, val

    # get values of contained packets
    pkt_values = []
    if length_type:
        # pkt_count
        for _ in range(length):
            bit_str, val = parse_packet(bit_str)
            pkt_values.append(val)
    else:
        # bit_count
        starting_len = len(bit_str)
        # import pdb
        # pdb.set_trace()
        while(starting_len - len(bit_str) < length):
            bit_str, val = parse_packet(bit_str)
            pkt_values.append(val)

    # Perform calculation of values
    if type == 0:
        # sum
        retval = 0
        for val in pkt_values:
            retval += val
        return bit_str, retval
    elif type == 1:
        # product
        retval = 1
        for val in pkt_values:
            retval *= val
        return bit_str, retval
    elif type == 2:
        # min
        minval = pkt_values[0]
        for val in pkt_values:
            if val < minval:
                minval = val
        return bit_str, minval
    elif type == 3:
        # max
        maxval = -1
        for val in pkt_values:
            if val > maxval:
                maxval = val
        return bit_str, maxval
    elif type == 5:
        # greater than
        retval = (pkt_values[0] > pkt_values[1])
        return bit_str, retval
    elif type == 6:
        # less than
        retval = (pkt_values[0] < pkt_values[1])
        return bit_str, retval
    elif type == 7:
        # equal to
        retval = (pkt_values[0] == pkt_values[1])
        return bit_str, retval

    raise Error


def parse_literal(bit_str) -> int:
    # print(f'parsing literal: {bit_str}')
    hex_repr = ''
    while(bit_str[0] == '1'):
        msb = bit_str[1:5]
        hex_repr += msb
        bit_str = bit_str[5:]
    msb = bit_str[1:5]
    hex_repr += msb
    return bit_str[5:], int(hex_repr, 2)


def part1(bit_str):
    bit_str, val = parse_packet(bit_str)
    return version_sum


def part2(bit_str):
    bit_str, val = parse_packet(bit_str)
    return val


def parse_data(filename):
    with open(filename) as f:
        line = f.readline()
    bit_str = ''
    for ch in line:
        bin_representation = bin(hex_map[ch])
        str_representation = str(bin_representation)[2:].rjust(4, '0')
        bit_str += str_representation
    return bit_str


bit_str = parse_data(args.filename)
# print(parse_literal('11010001010'))
print(part1(bit_str))
print(part2(bit_str))
