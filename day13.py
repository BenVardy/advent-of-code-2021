from typing import List, Tuple


def printpaper(paper: List[List[bool]]):
    print('\n'.join(''.join(('#' if x else '.' for x in row)) for row in paper))


def foldpaper(paper: List[List[bool]], instructions: List[Tuple[str, int]], part1: bool):
    for _dir, val in instructions:
        if _dir == 'y':
            new_paper = [row[::] for row in paper[:val]]

            coff_rows = len(paper) - val - 1
            coff_cols = len(paper[0])

            for i in range(coff_rows):
                for j in range(coff_cols):
                    new_paper[len(new_paper) - i - 1][j] |= paper[val + 1 + i][j]
        else:  # == 'x'
            new_paper = [row[:val] for row in paper]

            coff_rows = len(paper)
            coff_cols = len(paper[0]) - val - 1

            for i in range(coff_rows):
                for j in range(coff_cols):
                    new_paper[i][len(new_paper[0]) - j - 1] |= paper[i][val + 1 + j]

        paper = new_paper
        if part1:
            break

    if part1:
        print(sum(row.count(True) for row in paper))
    else:
        printpaper(paper)


def part1(paper: List[List[bool]], instructions: List[Tuple[str, int]]):
    foldpaper(paper, instructions, True)


def part2(paper: List[List[bool]], instructions: List[Tuple[str, int]]):
    foldpaper(paper, instructions, False)


def main():
    f = open('inputs/day13.txt')

    txt_coords, txt_instructions = f.read().split('\n\n')

    # x, y
    coords = [tuple(int(x) for x in line.strip().split(',')) for line in txt_coords.splitlines()]

    paper = [[False for _ in range(max(coords, key=lambda x: x[0])[0] + 1)] for _ in range(max(coords, key=lambda x: x[1])[1] + 1)]

    for x, y in coords:
        paper[y][x] = True

    instructions: List[Tuple[str, int]] = []
    for line in txt_instructions.splitlines():
        _dir, val = line.strip().split('=')
        instructions.append((_dir[-1], int(val)))

    part1(paper, instructions)
    part2(paper, instructions)


if __name__ == '__main__':
    main()
