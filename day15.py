import itertools
import heapq
from typing import Dict, List, Tuple


DIRS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]


def part1(graph: List[List[int]]):
    rows = len(graph)
    cols = len(graph[0])

    Q, seen = [(0, (0, 0))], set()
    while True:
        cost, u = heapq.heappop(Q)
        if u not in seen:
            seen.add(u)
            if u == (rows - 1, cols - 1):
                print(cost)
                return

            for oi, oj in DIRS:
                ni, nj = u[0] + oi, u[1] + oj
                v = (ni, nj)

                if ni >= 0 and ni < rows and nj >= 0 and nj < cols:
                    heapq.heappush(Q, (cost + graph[ni][nj], v))


def part2(orig: List[List[int]]):
    orig_rows = len(orig)
    orig_cols = len(orig[0])

    final_rows = orig_rows * 5
    final_cols = orig_cols * 5

    output = [[0 for _ in range(final_cols)] for _ in range(final_rows)]

    for i in range(orig_rows):
        for j in range(orig_cols):
            output[i][j] = orig[i][j]

    for c in range(1, 5):
        oi = orig_rows * c

        for i in range(orig_rows):
            for j in range(orig_cols):
                output[i + oi][j] = (output[i + (oi - orig_rows)][j]) % 9 + 1

    for x in range(5):
        for y in range(1, 5):
            oi = orig_rows * x
            oj = orig_cols * y

            for i in range(orig_rows):
                for j in range(orig_cols):
                    output[i + oi][j + oj] = output[i + oi][j + (oj - orig_cols)] % 9 + 1

    part1(output)


def main():
    f = open('inputs/day15.txt')

    graph: List[List[int]] = [[int(x) for x in list(line.strip())] for line in f.readlines()]

    part1(graph)
    part2(graph)


if __name__ == '__main__':
    main()
