from typing import List

MATCHING = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


def part1(chunks: List[str]):
    SCORES = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    total = 0

    for chunk in chunks:
        expected_close: List[str] = []

        for c in chunk:
            if c in dict.keys(MATCHING):
                expected_close.append(MATCHING[c])
            else:
                expect = expected_close.pop()
                if expect != c:
                    total += SCORES[c]
                    break

    print(total)


def part2(chunks: List[str]):
    SCORES = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    incomplete: List[str] = []

    for chunk in chunks:
        expected_close: List[str] = []

        corrupt = False
        for c in chunk:
            if c in dict.keys(MATCHING):
                expected_close.append(MATCHING[c])
            else:
                expect = expected_close.pop()
                if expect != c:
                    corrupt = True
                    break

        if not corrupt:
            incomplete.append(chunk)

    scores: List[int] = []
    for chunk in incomplete:
        expected_close = []

        for c in chunk:
            if c in dict.keys(MATCHING):
                expected_close.append(MATCHING[c])
            else:
                expected_close.pop()

        total = 0
        for x in expected_close[::-1]:
            total *= 5
            total += SCORES[x]

        scores.append(total)

    print(sorted(scores)[len(scores) // 2])


def main():
    f = open('inputs/day10.txt')

    chunks = [x.strip() for x in f.readlines()]

    part1(chunks)
    part2(chunks)


if __name__ == '__main__':
    main()
