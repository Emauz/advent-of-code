#!/usr/bin/env python3

import argparse
import itertools

# DEFAULT_FILENAME = 'example'
DEFAULT_FILENAME = 'input'

parser = argparse.ArgumentParser(description="AoC day 20")
parser.add_argument('filename', nargs='?', default=DEFAULT_FILENAME)
args = parser.parse_args()


class Image(object):
    def __init__(self, parent, pixels=None, algo=None):
        if pixels:
            self.pixels = pixels
        else:
            self.pixels = {}
        self.parent = parent
        if algo:
            self.algo = algo
        else:
            self.algo = parent.algo

    def get_pixel(self, coord):
        if coord in self.pixels.keys():
            return self.pixels[coord]
        # we've reached the base image, where unknowns are false
        if self.parent is None:
            return False
        # determine current pixel value by enhancing parent
        enhancement_val = 0
        for i, (dx, dy) in enumerate(list(itertools.product([-1, 0, 1], [-1, 0, 1]))):
            # print(coord[0]+dx, coord[1]+dy, self.parent.get_pixel((coord[0]+dx, coord[1]+dy)))
            if self.parent.get_pixel((coord[0] + dx, coord[1] + dy)):
                enhancement_val += (2 ** (8-i))  # (8-i) is to fix endianness issues
        self.pixels[coord] = self.algo[enhancement_val]
        return self.pixels[coord]

    def __str__(self):
        import numpy as np
        grid = np.full((15, 15), '.')
        for (x, y), val in self.pixels.items():
            grid[x][y] = ('#' if val else '.')
        output_str = ''
        for row in grid:
            for c in row:
                output_str += c
            output_str += '\n'
        return output_str


def part1(layer_1):
    def true_in_layer(layer):
        return list(layer.pixels.values()).count(True)

    layers = [layer_1]
    top_layer = Image(layer_1)
    layers.append(top_layer)
    top_layer.get_pixel((0, 0))
    for i in range(150):
        print(i)
        top_layer = Image(top_layer)
        layers.append(top_layer)
    top_layer.get_pixel((0, 0))  # update pixels from current layer outward
    print(true_in_layer(layers[2]))

    return true_in_layer(layers[2])


def part2(layer_1):
    def true_in_layer(layer):
        return list(layer.pixels.values()).count(True)

    layers = [layer_1]
    top_layer = Image(layer_1)
    layers.append(top_layer)
    top_layer.get_pixel((0, 0))
    for i in range(250):
        top_layer = Image(top_layer)
        top_layer.get_pixel((0, 0))  # update pixels from current layer outward
        layers.append(top_layer)
        if(i > 50):
            print(i, true_in_layer(layers[50]))

    return true_in_layer(layers[50])


def parse_data(filename):
    with open(filename) as f:
        raw = f.read()
    raw = raw.split('\n\n')
    algo = raw[0].replace('\n', '')
    algo = [(x == '#') for x in algo]
    pixels = {}
    for y, row in enumerate(raw[1].split('\n')):
        for x, c in enumerate(row):
            pixels[(y, x)] = (c == '#')
    return Image(None, pixels=pixels, algo=algo)


img = parse_data(args.filename)
print(part1(img))
print(part2(img))
