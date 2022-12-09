#!/usr/bin/env python3

filename = "input.txt"
#filename = "1.txt"

with open(filename) as f:
    input_lines = f.readlines()

def parse(lines):
    array = []
    for trees in lines:
        line = []
        for tree in trees.strip():
            line.append(int(tree))
        array.append(line)
    return array

def scenic_score(parsed, row, col):
    height = parsed[row][col]
    #import pdb
    #pdb.set_trace()
    # check visible range on the top
    top = 0
    for other_row in reversed(range(row)):
        top += 1
        if(parsed[other_row][col] >= height):
            break
    # check visible range on the bottom
    bottom = 0
    for other_row in range(row+1, len(parsed)):
        bottom += 1
        if(parsed[other_row][col] >= height):
            break
    # check visible range on the left
    left = 0
    for other_col in reversed(range(col)):
        left += 1
        if(parsed[row][other_col] >= height):
            break
    # check visible range on the right
    right = 0
    for other_col in range(col+1, len(parsed[0])):
        right += 1
        if(parsed[row][other_col] >= height):
            break
    return bottom * top * left * right


def part1(parsed):
    visible_trees = set()
    # check visible from left
    for row in range(len(parsed[0])):
        tallest = -1
        for col in range(len(parsed)):
            if(parsed[row][col] > tallest):
                tallest = parsed[row][col]
                visible_trees.add((row, col))
    # check visible trees from top
    for col in range(len(parsed)):
        tallest = -1
        for row in range(len(parsed[0])):
            if(parsed[row][col] > tallest):
                tallest = parsed[row][col]
                visible_trees.add((row, col))
    # check visible trees from bottom
    for row in reversed(range(len(parsed[0]))):
        tallest = -1
        for col in reversed(range(len(parsed))):
            if(parsed[row][col] > tallest):
                tallest = parsed[row][col]
                visible_trees.add((row, col))
    # check visible trees from right
    for col in reversed(range(len(parsed))):
        tallest = -1
        for row in reversed(range(len(parsed[0]))):
            if(parsed[row][col] > tallest):
                tallest = parsed[row][col]
                visible_trees.add((row, col))
    return len(visible_trees)

def part2(parsed):
    best = 0
    for row in range(1, len(parsed)-1):
        for col in range(1, len(parsed[0])-1):
            score = scenic_score(parsed, row, col)
            if(score > best):
                best = score
    return best

def main():
    parsed = parse(input_lines)
    print(part1(parsed))
    print(part2(parsed))

if __name__ == '__main__':
    main()
