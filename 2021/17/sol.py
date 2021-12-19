#!/usr/bin/env python3

import argparse

# DEFAULT_FILENAME = 'simple'
# DEFAULT_FILENAME = 'example'
DEFAULT_FILENAME = 'input'

parser = argparse.ArgumentParser(description="AoC day 17")
parser.add_argument('filename', nargs='?', default=DEFAULT_FILENAME)
args = parser.parse_args()


def calc_trajectory(x_vel, y_vel, x_range, y_range):
    x_pos = 0
    y_pos = 0
    max_y_pos = 0
    prev_x = x_pos
    # check if we're in the target box
    if x_pos in x_range and y_pos in y_range:
        return True, max_y_pos
    while y_pos > y_range.stop - 250:  # magic 250 solves all issues
        x_pos += x_vel
        if x_pos == prev_x and y_pos < y_range.start:
            return False, max_y_pos
        else:
            prev_x = x_pos
        y_pos += y_vel
        # decrease x vel 1 towards 0
        if x_vel > 0:
            x_vel -= 1
        elif x_vel < 0:
            x_vel += 1
        # Gravity
        y_vel -= 1

        # Update max y pos we've seen
        if y_pos > max_y_pos:
            max_y_pos = y_pos
        # check if we're in the target box
        if x_pos in x_range and y_pos in y_range:
            return True, max_y_pos

    return False, max_y_pos


def part1(x_range, y_range):
    max_alt = -1
    for x_vel in range(0, x_range.stop):
        for y_vel in range(0, 500):
            hit_target, apex = calc_trajectory(x_vel, y_vel, x_range, y_range)
            if hit_target:
                if apex > max_alt:
                    max_alt = apex

    return max_alt


# 250-200 ..200 : 1973
# -1000..1000: 1973
# -500..500: 1973
# -200..200: 920
def part2(x_range, y_range):
    sols_found = 0
    for x_vel in range(250):
        if x_vel % 10 == 0:
            print(x_vel)
        for y_vel in range(-200, 200):
            hit_target, apex = calc_trajectory(x_vel, y_vel, x_range, y_range)
            if hit_target:
                sols_found += 1
    return sols_found


def parse_data(filename):
    with open(filename) as f:
        line = f.readline()
        line = line.split(' ')[2:]
        line[0] = line[0][2:].split('..')
        line[1] = line[1][2:].split('..')
        x_range = range(int(line[0][0]), int(line[0][1][:-1]) + 1)
        y_range = range(int(line[1][0]), int(line[1][1]) + 1)

    return (x_range, y_range)


x_range, y_range = parse_data(args.filename)
# print(part1(x_range, y_range))
print(part2(x_range, y_range))
