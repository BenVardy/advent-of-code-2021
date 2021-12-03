from functools import reduce
from typing import List


def part1(numbers: List[str]):
    _max = len(numbers[0])

    out = ''

    for i in range(_max):
        no1 = 0

        for x in numbers:
            no1 += int(x[i])

        out += '1' if no1 > len(numbers) / 2 else '0'

    print(int(''.join(str(1 - int(x)) for x in out), 2) * int(out, 2))


def part2(numbers: List[str]):
    o2 = [x for x in numbers]
    co2 = [x for x in numbers]

    for i in range(len(numbers[0])):
        o2_no1 = 0
        co2_no1 = 0

        for x in o2:
            o2_no1 += int(x[i])

        for x in co2:
            co2_no1 += int(x[i])

        o2_f = '1' if o2_no1 >= len(o2) / 2 else '0'
        co2_f = '1' if co2_no1 < len(co2) / 2 else '0'

        if len(o2) > 1:
            o2 = [x for x in o2 if x[i] == o2_f]
        if len(co2) > 1:
            co2 = [x for x in co2 if x[i] == co2_f]

    print(int(o2[0], 2) * int(co2[0], 2))


def main():
    f = open('inputs/day03.txt')

    numbers = [x.strip() for x in f.readlines()]

    part1(numbers)
    part2(numbers)


if __name__ == '__main__':
    main()
