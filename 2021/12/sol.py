#!/usr/bin/env python3

import argparse
import numpy as np

# DEFAULT_FILENAME = 'simple'
# DEFAULT_FILENAME = 'example'
# DEFAULT_FILENAME = 'example3'
DEFAULT_FILENAME = 'input'

parser = argparse.ArgumentParser(description="AoC day 12")
parser.add_argument('filename', nargs='?', default=DEFAULT_FILENAME)
args = parser.parse_args()


def part1(data):
    def create_paths(data, path, current):
        if current in path.split(',') and current.islower():
            return []
        elif current == 'end':
            return ['end']
        else:
            paths = []
            for dst in data[current]:
                if dst == 'start':
                    continue
                new_paths = create_paths(data, f'{path},{current}', dst)
                for new_path in new_paths:
                    paths.append(f'{current},{new_path}')
            return paths
    paths = create_paths(data, '', 'start')

    return len(paths)


def part2(data):
    # Check if we only have 1 of each lowercase letter
    def small_cave_single_entry(path) -> bool:
        seen = set()
        double_seen = False
        for ch in path.split(','):
            if ch.isupper():
                continue
            elif ch in seen and not double_seen:
                double_seen = True
            elif ch in seen and double_seen:
                return False
            else:
                seen.add(ch)
        return True

    def create_paths(data, path, current):
        if current == 'end':
            return ['end']
        elif not small_cave_single_entry(path) and current.islower():
            return []
        else:
            paths = []
            for dst in data[current]:
                if dst == 'start':
                    continue
                new_paths = create_paths(data, f'{path},{current}', dst)
                for new_path in new_paths:
                    if small_cave_single_entry(f'{current},{new_path}'):
                        paths.append(f'{current},{new_path}')
            return paths
    paths = create_paths(data, '', 'start')

    return len(paths)


def parse_data(filename):
    data = {}
    with open(filename) as f:
        for line in f:
            line = line.split('-')
            src = line[0]
            dst = line[1].strip()
            # add src->dst pathway
            if src in data.keys():
                data[src].add(dst)
            else:
                data[src] = set()
                data[src].add(dst)

    # Add reverse of all paths to the graph
    old_dict = dict(data)
    for src, dsts in old_dict.items():
        for dst in dsts:
            if dst in data.keys():
                data[dst].add(src)
            else:
                data[dst] = set()
                data[dst].add(src)

    return data


data = parse_data(args.filename)
print(part1(data))
print(part2(data))
