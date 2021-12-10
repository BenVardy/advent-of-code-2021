from typing import List


def part1(fish: List[int]):
    MAX_DAYS = 80

    for _ in range(MAX_DAYS):
        for i in range(len(fish)):
            fish[i] -= 1
            if fish[i] < 0:
                fish.append(8)
                fish[i] = 6

    print(len(fish))


def part2(fish: List[int]):
    lives = [0] * 9
    for i in range(len(lives)):
        lives[i] = fish.count(i)

    for _ in range(256):
        temp = lives[0]
        for i in range(1, len(lives)):
            lives[i - 1] = lives[i]

        lives[6] += temp
        lives[8] = temp

    print(sum(lives))


def main():
    f = open('inputs/day06.txt')

    _input = [int(x.strip()) for x in f.readline().split(',')]

    part1(_input[::])
    part2(_input[::])


if __name__ == '__main__':
    main()
