#!/usr/bin/env python3

import sys

from queue import PriorityQueue

filename = "input.txt"
#filename = "1.txt"

class Square(object):
    def __init__(self, \
            height, \
            row, \
            col, \
            cost=sys.maxsize, \
            is_start=False, \
            is_end=False):
        self.height = ord(height)
        self.cost = cost
        self.is_start = is_start
        self.is_end = is_end
        self.prev = None
        self.row = row
        self.col = col
        self.visited = is_start # start node gets visited first by default

    def __repr__(self):
        if(self.is_start):
            return 'S'
        elif(self.is_end):
            return 'E'
        return chr(self.height)

    def __eq__(self, other):
        return self.cost == other.cost

    def __lt__(self, other):
        return self.cost < other.cost


class Map(object):
    def __init__(self, mapfile, is_part1: bool):
        self.potential_starts = []
        self.start = None
        self.end = None
        self.grid = []
        for row, line in enumerate(open(mapfile)):
            squares = []
            for col, ch in enumerate(line.strip()):
                if(ch == 'S'):
                    if(is_part1):
                        self.start = Square('a', row, col, cost=0, is_start=True)
                    else:
                        self.start = Square('a', row, col)
                    self.potential_starts.append(self.start)
                    squares.append(self.start)
                elif(ch == 'E'):
                    self.end = Square('z', row, col, is_end=True)
                    squares.append(self.end)
                elif(ch == 'a'):
                    cur = Square(ch, row, col)
                    self.potential_starts.append(cur)
                    squares.append(cur)
                else:
                    squares.append(Square(ch, row, col))
            self.grid.append(squares)

    def __repr__(self):
        ret = ''
        for row in self.grid:
            for square in row:
                ret += str(square)
            ret += '\n'
        return ret


def calculate_distance(map, start):
    q = PriorityQueue()
    q.put(map.grid[start.row][start.col])
    map.grid[start.row][start.col].cost = 0
    while(not q.empty()):
        current = q.get()
        row = current.row
        col = current.col
        for (row2, col2) in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            try:
                other = map.grid[row2][col2]
                if(not other.visited and \
                        other.height <= current.height + 1):
                    other.visited = True
                    cost_via_current = current.cost + 1
                    if(other.cost > cost_via_current):
                        other.cost = cost_via_current
                        other.prev = current
                    q.put(other)
            except:
                pass
    return map.end.cost

def part1(map):
    return calculate_distance(map, map.start)

def part2(map):
    min_distance = sys.maxsize
    for potential_start in map.potential_starts:
        fresh_map = Map(filename, is_part1=False)
        dist = calculate_distance(fresh_map, potential_start)
        if(dist < min_distance):
            min_distance = dist
    return min_distance

def main():
    map = Map(filename, is_part1=True)
    print(part1(map))
    print(part2(map))

if __name__ == '__main__':
    main()
