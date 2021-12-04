import re
from typing import List, Tuple


Tile = Tuple[int, bool]
Board = List[List[Tile]]


def boardwon(board: Board) -> bool:
    # Check rows complete
    for row in board:
        if all(x[1] for x in row):
            return True

    # Check cols complete
    for j in range(len(board[0])):
        col_complete = True

        for i in range(len(board)):
            if not board[i][j][1]:
                col_complete = False
                break

        if col_complete:
            return True

    return False


def calcboard(board: Board) -> int:
    return sum(sum(tile[0] for tile in row if not tile[1]) for row in board)


def part1(draws: List[int], boards: List[Board]):
    for d in draws:
        for i, b in enumerate(boards):
            for row in range(len(b)):
                for col in range(len(b[row])):
                    if b[row][col][0] == d:
                        boards[i][row][col] = (b[row][col][0], True)

            if boardwon(b):
                print(calcboard(b) * d)
                return


def part2(draws: List[int], boards: List[Board]):
    for d in draws:
        for i, b in enumerate(boards):
            for row in range(len(b)):
                for col in range(len(b[row])):
                    if b[row][col][0] == d:
                        boards[i][row][col] = (b[row][col][0], True)

        if len(boards) > 1:
            boards = [b for b in boards if not boardwon(b)]
        elif boardwon(boards[0]):
            print(calcboard(boards[0]) * d)
            break


def main():
    f = open('inputs/day04.txt')

    all_lines = f.readlines()

    draws = [int(x.strip()) for x in all_lines[0].split(',')]

    boards: List[Board] = [
        [
            [
                (int(z), False) for z in re.split(r' +', y.strip())
            ] for y in x.splitlines()
        ] for x in ''.join(all_lines[2:]).split('\n\n')
    ]

    part1(draws, boards)
    part2(draws, boards)


if __name__ == '__main__':
    main()
