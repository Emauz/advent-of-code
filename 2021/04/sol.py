#!/usr/bin/env python3

import argparse
import numpy as np

DEFAULT_FILENAME = 'input'

parser = argparse.ArgumentParser(description="AoC day 04")
parser.add_argument('filename', nargs='?', default=DEFAULT_FILENAME)
args = parser.parse_args()


class BingoBoard(object):
    def __init__(self, board_array):
        self.board = board_array

    # given a number, mark where it exists in the current board
    def mark(self, num):
        loc = np.where(self.board == num)
        if loc[0].size > 0:
            loc = (loc[0][0], loc[1][0])  # coord conversion hack
            self.board[loc[0]][loc[1]] = -1

    def check_win(self) -> bool:
        # brute force solutions for the win
        # check columns
        for col in self.board.T:
            if np.all(col == -1):
                return True
        for row in self.board:
            if np.all(row == -1):
                return True
        return False

    def calculate_unmarked_sum(self) -> int:
        # zero out all marked values (so we can use sum())
        self.board[self.board == -1] = 0
        return self.board.sum()


def part1(numbers, boards):
    for num in numbers:
        for board in boards:
            board.mark(num)
            if board.check_win():
                return board.calculate_unmarked_sum() * num
    return -1


def part2(numbers, boards):
    for num in numbers:
        for board in boards[:]:
            board.mark(num)
            # remove boards from list when they win
            if board.check_win():
                boards.remove(board)
                if not boards:
                    # found the last board to win
                    return board.calculate_unmarked_sum() * num
    return -1


def parse_data(filename):
    # Get data from file and split into fields
    f = open(filename, 'r')
    data = f.read().split('\n\n')

    numbers = np.array(data[0].split(','), dtype=int)
    boards = []
    # Construct board object for each given bingo board
    for board_string in data[1:]:
        board_array = np.array(board_string.split(), dtype=int)
        # convert to 2d array
        board_array.resize((5,5))
        # Create board and add to array
        boards.append(BingoBoard(board_array))

    return numbers, boards


numbers, boards = parse_data(args.filename)
print(part1(numbers, np.copy(boards)))
numbers, boards = parse_data(args.filename)
print(part2(numbers, boards))
