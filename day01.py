from typing import List


def part1(values: List[int]):
    total = 0
    for x, y in zip(values[1:], values[:-1]):
        if x > y:
            total += 1

    print(total)


def part2(values: List[int]):
    total = 0
    prev = sum(values[:3])

    for t in zip(values[1:-2], values[2:-1], values[3:]):
        s = sum(t)
        if s > prev:
            total += 1
        prev = s

    print(total)



def main():
    f = open('inputs/day01.txt')
    values = [int(x.strip()) for x in f.readlines()]

    part1(values)
    part2(values)


if __name__ == '__main__':
    main()
