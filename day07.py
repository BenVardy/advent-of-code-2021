from typing import List


def part1(crabs: List[int]):
    def calcfuel(crabs: List[int], pos: int) -> int:
        return sum(abs(pos - x) for x in crabs)

    res = -1

    for x in set(crabs):
        temp = calcfuel(crabs, x)

        if res == -1 or temp < res:
            res = temp

    print(res)


def part2(crabs: List[int]):
    def calcfuel(crabs: List[int], pos: int) -> int:
        return sum((((pos - x) ** 2) + abs(pos - x)) // 2 for x in crabs)

    res = -1

    for x in [x for x in range(max(crabs))]:
        temp = calcfuel(crabs, x)

        if res == -1 or temp < res:
            res = temp

    print(res)


def main():
    f = open('inputs/day07.txt')

    crabs = [int(x.strip()) for x in f.readline().split(',')]

    part1(crabs)
    part2(crabs)


if __name__ == '__main__':
    main()
