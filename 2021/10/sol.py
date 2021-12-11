#!/usr/bin/env python3

import argparse

# DEFAULT_FILENAME = 'example'
DEFAULT_FILENAME = 'input'

parser = argparse.ArgumentParser(description="AoC day 10")
parser.add_argument('filename', nargs='?', default=DEFAULT_FILENAME)
args = parser.parse_args()

pairs = {
    ')': '(',
    '>': '<',
    '}': '{',
    ']': '[',
}

syntax_score_values = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
    None: 0
}

completion_score_values = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}


def first_illegal_char(line):
    stack = []
    for char in line:
        # if stack empty, add to it
        if not stack:
            stack.append(char)
        # If character is opener, add to stack
        elif char in pairs.values():
            stack.append(char)
        # if we match current top of stack, close it
        elif pairs[char] == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    # Entire stack should be openers. First closer is therefore illegal
    for char in stack:
        if char in pairs.keys():
            return char
    return None


def complete_line(line):
    stack = []
    for char in line:
        # if stack empty, add to it
        if not stack:
            stack.append(char)
        # If character is opener, add to stack
        elif char in pairs.values():
            stack.append(char)
        # if we match current top of stack, close it
        elif pairs[char] == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    return stack


def part1(lines):
    score = 0
    filtered_lines = []
    for line in lines:
        illegal = first_illegal_char(line)
        score += syntax_score_values[illegal]
        if not illegal:
            filtered_lines.append(line)

    return filtered_lines, score


def part2(lines):
    scores = []
    for line in lines:
        completion = complete_line(line)
        completion = completion[::-1]
        current_score = 0
        for char in completion:
            current_score *= 5
            current_score += completion_score_values[char]
        scores.append(current_score)
    scores = sorted(scores)
    mid_idx = len(scores) // 2
    mid_score = scores[mid_idx]

    return mid_score


def parse_data(filename):
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line.strip())

    return lines


lines = parse_data(args.filename)
lines, part1_ans = part1(lines)
print(part1_ans)
print(part2(lines))
