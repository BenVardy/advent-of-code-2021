from typing import List, Tuple

FORWARD = 'forward'
DOWN = 'down'
UP = 'up'


def part1(commands: List[Tuple[str, int]]):
    horizontal = 0
    depth = 0

    for c in commands:
        direction = c[0]

        if direction == FORWARD:
            horizontal += c[1]
        elif direction == DOWN:
            depth += c[1]
        elif direction == UP:
            depth -= c[1]

    print(horizontal * depth)


def part2(commands: List[Tuple[str, int]]):
    horizontal = 0
    depth = 0
    aim = 0

    for c in commands:
        d = c[0]

        if d == FORWARD:
            horizontal += c[1]
            depth += aim * c[1]
        elif d == DOWN:
            aim += c[1]
        elif d == UP:
            aim -= c[1]

    print(horizontal * depth)




def main():
    f = open('inputs/day02.txt')

    commands = [(y[0], int(y[1])) for y in [x.strip().split(' ') for x in f.readlines()]]

    part1(commands)
    part2(commands)


if __name__ == '__main__':
    main()
