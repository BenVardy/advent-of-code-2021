import itertools
import math
from typing import List, Tuple


DIRS: List[Tuple[int, int]] = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]


def part1(surface: List[List[int]]):
    low_points: List[int] = []

    for i in range(len(surface)):
        for j in range(len(surface[i])):
            lowest = True
            c = surface[i][j]

            for oi, oj in DIRS:
                ni = i + oi
                nj = j + oj

                if ni >= 0 and ni < len(surface) and nj >= 0 and nj < len(surface[i]) and surface[i + oi][j + oj] <= c:
                    lowest = False
                    break

            if lowest:
                low_points.append(c)

    print(sum(1 + x for x in low_points))


def backtrack(surface: List[List[Tuple[int, bool]]], p: Tuple[int, int]) -> int:
    px, py = p
    if surface[px][py][1] or surface[px][py][0] == 9:
        return 0

    surface[px][py] = (surface[px][py][0], True)

    total = 1

    for d in DIRS:
        nx, ny = px + d[0], py + d[1]
        if nx < 0 or nx >= len(surface) or ny < 0 or ny >= len(surface[0]):
            continue

        total += backtrack(surface, (nx, ny))

    return total


def part2(in_surface: List[List[int]]):
    surface = [[(x, x == 9) for x in row] for row in in_surface]

    basin_sizes: List[int] = []

    for i, j in itertools.product(range(len(surface)), range(len(surface[0]))):
        if not surface[i][j][1]:
            basin_sizes.append(backtrack(surface, (i, j)))

    print(math.prod(sorted(basin_sizes, reverse=True)[:3]))


def main():
    f = open('inputs/day09.txt')

    surface = [[int(y) for y in list(x.strip())] for x in f.readlines()]

    part1(surface)
    part2(surface)


if __name__ == '__main__':
    main()
