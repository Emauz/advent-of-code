#!/usr/bin/env python3

# guess 1: 5286, too low
filename = "input.txt"
#filename = "1.txt"
#filename = "2.txt"

with open(filename) as f:
    input_lines = f.readlines()

def parse(lines):
    parsed = []
    for line in lines:
        line = line.strip().split()
        parsed.append((line[0], int(line[1])))
    return parsed

class Rope(object):
    def __init__(self, num_tails):
        self.head = [0, 0]
        self.tails = []
        for _ in range(num_tails):
            self.tails.append([0, 0])

    def __repr__(self):
        ret = ''
        ret += f'H: x: {self.head[0]}, y: {self.head[1]}\n'
        for tail_idx in range(len(self.tails)):
            ret += f'{tail_idx}: x: {self.tails[tail_idx][0]}, y: {self.tails[tail_idx][1]}'
        return ret

    def move_head(self, direction):
        if direction == 'L':
            self.head[0] -= 1
        elif direction == 'R':
            self.head[0] += 1
        elif direction == 'U':
            self.head[1] += 1
        elif direction == 'D':
            self.head[1] -= 1

    def update_tail(self, tail_idx):
        if(tail_idx == 0):
            parent_segment = self.head
        else:
            parent_segment = self.tails[tail_idx - 1]

        # don't move if tail is adjacent to the head
        if(abs(parent_segment[0] - self.tails[tail_idx][0]) <= 1 and \
           abs(parent_segment[1] - self.tails[tail_idx][1]) <= 1):
            #print('not moving tail')
            return
        elif(parent_segment[0] == self.tails[tail_idx][0]):
            # x is same, move one closer in y
            dy = (parent_segment[1] - self.tails[tail_idx][1])
            dy = dy // abs(dy) # force value to 1
            self.tails[tail_idx][1] += dy
            #print(f"Tail y += {dy}")
        elif(parent_segment[1] == self.tails[tail_idx][1]):
            # y is same, move one closer in x
            dx = (parent_segment[0] - self.tails[tail_idx][0])
            dx = dx // abs(dx) # force value to 1
            self.tails[tail_idx][0] += dx
            #print(f"Tail x += {dx}")
        else:
            # we're at a diagonal. move one closer in both dimensions
            dx = (parent_segment[0] - self.tails[tail_idx][0])
            dx = dx // abs(dx) # force value to 1
            dy = (parent_segment[1] - self.tails[tail_idx][1])
            dy = dy // abs(dy) # force value to 1
            self.tails[tail_idx][0] += dx
            self.tails[tail_idx][1] += dy
            #print(f"Tail x += {dx}, y += {dy}")


def part1(parsed):
    tail_visited = set()
    r = Rope(1) # 1 tail
    for direction, steps in parsed:
        for _ in range(steps):
            #print(direction)
            r.move_head(direction)
            r.update_tail(0)
            tail_visited.add((r.tails[0][0], r.tails[0][1]))
            #print(r)
    return len(tail_visited)

def part2(parsed):
    NUM_TAILS = 9
    tail_end_visited = set()
    r = Rope(NUM_TAILS)
    for direction, steps in parsed:
        for _ in range(steps):
            #print(direction)
            r.move_head(direction)
            for tail_idx in range(NUM_TAILS):
                r.update_tail(tail_idx)
            tail_end_visited.add((r.tails[NUM_TAILS-1][0], r.tails[NUM_TAILS-1][1]))
            #print(r)
    return len(tail_end_visited)

def main():
    parsed = parse(input_lines)
    print(part1(parsed))
    print(part2(parsed))

if __name__ == '__main__':
    main()
