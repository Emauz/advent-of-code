#!/usr/bin/env python3

import argparse

# DEFAULT_FILENAME = 'example'
DEFAULT_FILENAME = 'input'

parser = argparse.ArgumentParser(description="AoC day 21")
parser.add_argument('filename', nargs='?', default=DEFAULT_FILENAME)
args = parser.parse_args()


def part1(positions):
    scores = [0, 0]
    die_position = 0
    num_rolls = 0
    player = 1
    while scores[0] < 1000 and scores[1] < 1000:
        # switch player's turn
        player ^= 1
        # play turn
        roll_total = 0
        # roll each die
        for die in range(3):
            num_rolls += 1
            die_position += 1
            roll = die_position
            die_position = (die_position % 100)
            roll_total += roll

        positions[player] += roll_total
        positions[player] = ((positions[player] - 1) % 10) + 1
        scores[player] += positions[player]

    return min(scores) * num_rolls


# global var for part 2
winning_universes = [0, 0]


def part2(positions, scores=[0, 0], universes=1, player=0):
    # how many universes lead to each outcome?
    paths_to_num = {
        3: 1,
        4: 3,
        5: 6,
        6: 7,
        7: 6,
        8: 3,
        9: 1
    }

    # determine if we're at a winning state
    global winning_universes
    if scores[0] >= 21:
        winning_universes[0] += universes
        return
    if scores[1] >= 21:
        winning_universes[1] += universes
        return

    # make every move possible
    for roll_total in range(3, 10):
        new_positions = positions[:]
        new_scores = scores[:]
        new_positions[player] += roll_total
        new_positions[player] = ((new_positions[player] - 1) % 10) + 1
        new_scores[player] += new_positions[player]
        part2(new_positions, new_scores, universes * paths_to_num[roll_total], player ^ 1)


def parse_data(filename):
    with open(filename) as f:
        positions = []
        for line in f:
            line = line.split(' ')
            player_pos = int(line[-1])
            positions.append(player_pos)
    return positions


data = parse_data(args.filename)
print(part1(data[:]))
part2(data[:])
print(max(winning_universes))
