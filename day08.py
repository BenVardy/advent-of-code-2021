import itertools
from typing import List, Tuple

Line = Tuple[List[str], List[str]]

LEN_0 = 6
LEN_1 = 2
LEN_2 = 5
LEN_3 = 5
LEN_4 = 4
LEN_5 = 5
LEN_6 = 6
LEN_7 = 3
LEN_8 = 7
LEN_9 = 6

def part1(lines: List[Line]):
    total = 0

    for _, digits in lines:
        total += len([
            x for x in digits if len(x) == LEN_1 or len(x) == LEN_4
            or len(x) == LEN_7 or len(x) == LEN_8
        ])

    print(total)


def part2(lines: List[Line]):
    total = 0

    for line, digits in lines:
        found = ['' for _ in range(10)]
        for x in line:
            if len(x) == LEN_1:
                found[1] = x
            elif len(x) == LEN_4:
                found[4] = x
            elif len(x) == LEN_7:
                found[7] = x
            elif len(x) == LEN_8:
                found[8] = x

        # Find 3
        fives = [x for x in line if len(x) == 5]
        temp = [(x, y) for x, y in itertools.combinations(fives, 2) if len(set(x).intersection(y)) == 4]
        found[3] = set(temp[0]).intersection(temp[1]).pop()
        fives.remove(found[3])

        # Find 9
        sixes = [x for x in line if len(x) == 6]
        found[9] = [x for x in sixes if len(set(x).intersection(found[3])) == 5][0]
        sixes.remove(found[9])

        # Find 0 and 6
        found[0] = [x for x in sixes if len(set(x).intersection(found[7])) == 3][0]
        sixes.remove(found[0])
        found[6] = sixes[0]

        # Find 2 and 5
        found[2] = [x for x in fives if len(set(x).intersection(found[6])) == 4][0]
        fives.remove(found[2])
        found[5] = fives[0]

        total += int(''.join(str(found.index(x)) for x in digits))

    print(total)


def main():
    f = open('inputs/day08.txt')

    lines: List[Line] = [tuple([''.join(sorted(list(y))) for y in x.split(' ')] for x in l.strip().split(' | ')) for l in f.readlines()]

    part1(lines)
    part2(lines)


if __name__ == '__main__':
    main()
