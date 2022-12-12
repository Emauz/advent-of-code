#!/usr/bin/env python3

import math

filename = "input.txt"
#filename = "1.txt"

class Monkey(object):
    def __init__(self, id, items, operation, test, test_divisor):
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test
        self.test_divisor = test_divisor
        # statistics
        self.inspections_done = 0

    def __repr__(self):
        return f"Monkey {self.id}: {self.items}"

    def give_item(self, item):
        self.items.append(item)

    def take_turn(self, monkeys, divide: bool, lcm=None):
        #print(f"Monkey {self.id}")
        while(self.items):
            self.inspections_done += 1
            current_item = self.items.pop(0)
            #print(f"\t Monkey inspects item with a worry level of {current_item}")
            current_item = self.operation(current_item)
            #print(f"\t\t Monkey inspects item. New worry level: {current_item}")
            if(divide):
                current_item = current_item // 3
            #print(f"\t\t Item not broken. New worry level: {current_item}")
            target_monkey = self.test(current_item)
            #print(f"\t\t Throwing item to monkey: {target_monkey}")
            if lcm:
                monkeys[target_monkey].give_item(current_item % lcm)
            else:
                monkeys[target_monkey].give_item(current_item)

def parse():
    with open(filename) as f:
        raw_input = f.read()
    monkeys = []
    for monkey_block in raw_input.split('\n\n'):
        monkey_block = monkey_block.split('\n')

        # Line 1: Monkey ID
        id = monkey_block[0] \
                .strip() \
                .split()[1][:-1] # extra [:-1] is to strip the ':' off the end
        id = int(id)

        # Line 2: Monkey's items
        items = monkey_block[1] \
                .strip() \
                .replace(',', '') \
                .split()[2:]
        items = [int(x) for x in items] 

        # line 3: Monkey operation
        operation = monkey_block[2] \
                .strip() \
                .split()[4:]
        # NOTE: we're assuming that all operations will be formatted 
        # "operation = old <arithmetic> <value>". This implementation will
        # break if the first token ends up being set to something other than
        # "old"
        arithmetic_op = operation[0]
        value = operation[1]
        # NOTE: in lambda definitions, value=value parameter forces current state
        #of the "value" parameter to be included in the lambda closure.
        if arithmetic_op == '+':
            operation = lambda x, value=value: x + \
                    (x if value == 'old' else int(value))
        else:
            operation = lambda x, value=value: x * \
                    (x if value == 'old' else int(value))

        # Line 4: test
        test_divisor = int(monkey_block[3].strip().split()[-1])
        true_target = int(monkey_block[4].strip().split()[-1])
        false_target = int(monkey_block[5].strip().split()[-1])
        test = lambda x, \
                true_target=true_target, \
                false_target=false_target, \
                test_divisor=test_divisor \
                : true_target if x % test_divisor == 0 else false_target

        monkeys.append(Monkey(id, items, operation, test, test_divisor))
    return monkeys

def part1(monkeys):
    for round in range(20):
        for monkey in monkeys:
            monkey.take_turn(monkeys, True)
    monkey_inspections = [m.inspections_done for m in monkeys]
    monkey_inspections.sort()
    return monkey_inspections[-1] * monkey_inspections[-2]

def part2(monkeys):
    divisors = [m.test_divisor for m in monkeys]
    lcm = math.lcm(*divisors)
    for round in range(10000):
        for monkey in monkeys:
            monkey.take_turn(monkeys, False, lcm)
    monkey_inspections = [m.inspections_done for m in monkeys]
    monkey_inspections.sort()
    return monkey_inspections[-1] * monkey_inspections[-2]
    return res

def main():
    monkeys = parse()
    print(part1(monkeys))
    monkeys = parse()
    print(part2(monkeys))

if __name__ == '__main__':
    main()
