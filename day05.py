import math
import itertools
from typing import Dict, List, Tuple


Point = Tuple[int, int]


def part1(lines: List[Tuple[Point, Point]]):
    full_lines: List[Point] = []

    for line in lines:
        c_line: List[Point] = []

        start, end = line

        if start[0] == end[0]:
            s = min(start[1], end[1])
            e = max(start[1], end[1])
            for i in range(s, e + 1):
                c_line.append((start[0], i))

        elif start[1] == end[1]:
            s = min(start[0], end[0])
            e = max(start[0], end[0])
            for i in range(s, e + 1):
                c_line.append((i, start[1]))

        full_lines.extend(c_line)

    full_lines.sort()

    print(len([y for y in (len(list(x)) for _, x in itertools.groupby(full_lines)) if y > 1]))


def part2(lines: List[Tuple[Point, Point]]):
    full_lines: List[Point] = []

    for line in lines:
        c_line: List[Point] = []

        start, end = line

        if start[0] == end[0]:
            s = min(start[1], end[1])
            e = max(start[1], end[1])
            for i in range(s, e + 1):
                c_line.append((start[0], i))
        elif start[1] == end[1]:
            s = min(start[0], end[0])
            e = max(start[0], end[0])
            for i in range(s, e + 1):
                c_line.append((i, start[1]))
        else:
            x_dir = 1 if start[0] < end[0] else -1
            y_dir = 1 if start[1] < end[1] else -1

            for p in zip(range(start[0], end[0], x_dir), range(start[1], end[1], y_dir)):
                c_line.append(p)

            c_line.append(end)

        full_lines.extend(c_line)

    full_lines.sort()

    print(len([y for y in (len(list(x)) for _, x in itertools.groupby(full_lines)) if y > 1]))


def main():
    f = open('inputs/day05.txt')

    lines: List[Tuple[Point, Point]] = [
        tuple(
            tuple(int(y) for y in x.split(',')) for x in l.strip().split(' -> ')
        ) for l in f.readlines()
    ]

    part1(lines)
    part2(lines)


if __name__ == '__main__':
    main()
