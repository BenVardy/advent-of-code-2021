from typing import List


def part1(fish: List[int]):
    MAX_DAYS = 77

    for _ in range(MAX_DAYS):
        for i in range(len(fish)):
            fish[i] -= 1
            if fish[i] < 0:
                fish.append(8)
                fish[i] = 6


    print(len(fish))


def part2(fish: List[int]):
    init_len = len(fish)

    groups = [6]

    for _ in range(77):
        for i in range(len(groups)):
            groups[i] -= 1
            if groups[i] < 0:
                groups.append(8)
                groups[i] = 6

    print(len(groups) * init_len)


def main():
    f = open('inputs/day06.txt')

    _input = [int(x.strip()) for x in f.readline().split(',')]

    part1(_input)
    part2(_input)


if __name__ == '__main__':
    main()
