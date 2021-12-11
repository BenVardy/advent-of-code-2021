import itertools
from typing import List


def part1(octopod_in: List[List[int]]):
    octopod = [x[::] for x in octopod_in]

    total = 0

    for _ in range(9):
        octopod = [[x + 1 for x in row] for row in octopod]

        while any(any(x > 9 for x in row) for row in octopod):
            for i in range(len(octopod)):
                for j in range(len(octopod[i])):
                    if octopod[i][j] > 9:
                        for oi, oj in itertools.product(range(-1, 2),
                                                        repeat=2):
                            if oi == 0 and oj == 0:
                                continue

                            ni, nj = i + oi, j + oj
                            if (ni < 0 or ni >= len(octopod) or nj < 0
                                    or nj >= len(octopod[i])
                                    or octopod[ni][nj] == 0):
                                continue

                            octopod[ni][nj] += 1

                        octopod[i][j] = 0
                        total += 1

    print(total)


def part2(octopod_in: List[List[int]]):
    octopod = [x[::] for x in octopod_in]

    counter = 0
    while any(any(x != 0 for x in row) for row in octopod):
        counter += 1
        octopod = [[x + 1 for x in row] for row in octopod]

        while any(any(x > 9 for x in row) for row in octopod):
            for i in range(len(octopod)):
                for j in range(len(octopod[i])):
                    if octopod[i][j] > 9:
                        for oi, oj in itertools.product(range(-1, 2),
                                                        repeat=2):
                            if oi == 0 and oj == 0:
                                continue

                            ni, nj = i + oi, j + oj
                            if (ni < 0 or ni >= len(octopod) or nj < 0
                                    or nj >= len(octopod[i])
                                    or octopod[ni][nj] == 0):
                                continue

                            octopod[ni][nj] += 1

                        octopod[i][j] = 0

    print(counter)


def main():
    f = open('inputs/day11.txt')

    octopod = [[int(x) for x in line.strip()] for line in f.readlines()]

    part1(octopod)
    part2(octopod)


if __name__ == '__main__':
    main()
