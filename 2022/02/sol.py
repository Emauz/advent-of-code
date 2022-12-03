#!/usr/bin/env python3

filename = "input.txt"
#filename = "1.txt"

with open(filename) as f:
    lines = f.readlines()

# takes a rock(0), paper(1), or scissors(2) from us and an opponent,
# returning the game's result: lose(0), tie(1), win(2)
def duel(them, us) -> int:
    if(us == them - 1 or (us == 2 and them == 0)):
        # we lost
        return 0
    elif(us == them):
        # we tied
        return 1
    elif(us == them + 1 or (us == 0 and them == 2)):
        # we won!
        return 2

# what to play against their move if we want a given result
# moves and results are the same numerical values as above
def what_to_play(them, result):
    if(result == 0):
        # we want to lose
        return (them - 1) % 3
    if(result == 1):
        # we want to tie
        return them
    if(result == 2):
        # we want to win
        return (them + 1) % 3

def parse():
    games = []
    for line in lines:
        line = line.split()
        first = ord(line[0]) - ord('A')
        second = ord(line[1]) - ord('X')
        game = (first, second)
        games.append(game)
    return games

def part1(games):
    total_score = 0
    for (them, us) in games:
        result = duel(them, us)
        total_score += result * 3
        total_score += us + 1
    return total_score

def part2(games):
    total_score = 0
    for them, result in games:
        our_move = what_to_play(them, result)
        total_score += result * 3
        total_score += our_move + 1
    return total_score


games = parse()
print(part1(games))
print(part2(games))
