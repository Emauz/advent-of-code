#!/usr/bin/env python3

f = open('input', 'r')


def part1():
    prev = 69420
    count = 0
    for line in f:
        line = int(line)
        if line > prev:
            count += 1
        prev = line
    return count


def part2():
    prev = 69420
    slidey_window = []
    slidey_window.append(int(f.readline()))
    slidey_window.append(int(f.readline()))
    count = 0
    prev = 42069
    for line in f:
        slidey_window.append(int(line))
        if sum(slidey_window) > prev:
            count += 1
        prev = sum(slidey_window)
        slidey_window = slidey_window[1:]
    return count


print(part1())
f.seek(0)
print(part2())
