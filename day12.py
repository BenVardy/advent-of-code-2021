import itertools
from typing import Dict, List


def traverse_p1(paths: Dict[str, List[str]], c: str, p: List[str]) -> List[str]:
    is_big = c.isupper()
    if not is_big and c in p:
        return []

    if c == 'end':
        # print(p + ['end'])
        # return []

        return [','.join(p + ['end'])]

    output: List[str] = []

    for _next in paths[c]:
        output += traverse_p1(paths, _next, p + [c])

    return output


def part1(paths: Dict[str, List[str]]):
    result = traverse_p1(paths, 'start', [])

    print(len(result))


def canpass(cave: str, path: List[str]) -> bool:
    if cave in ['start', 'end']:
        return bool(1 - path.count(cave))

    if cave.islower():
        if cave not in path:
            return True

        times_passed = {c: len(list(x)) for c, x in itertools.groupby(sorted(path)) if c.islower()}

        return max(times_passed.values()) == 1
    else:
        return True


def traverse_p2(paths: Dict[str, List[str]], c: str, p: List[str]) -> List[str]:
    if not canpass(c, p):
        return []

    if c == 'end':
        return [','.join(p + ['end'])]

    output: List[str] = []

    for _next in paths[c]:
        output += traverse_p2(paths, _next, p + [c])

    return output



def part2(paths: Dict[str, List[str]]):
    result = traverse_p2(paths, 'start', [])

    print(len(result))


def main():
    f = open('inputs/day12.txt')

    paths: Dict[str, List[str]] = {}

    lines = f.readlines()

    # Populate caves.
    for line in lines:
        s, e = line.strip().split('-')

        if s not in paths.keys():
            paths[s] = []
        if e not in paths.keys():
            paths[e] = []

        paths[s].append(e)
        paths[e].append(s)

    # print(caves)
    # print(paths)

    part1(paths)
    part2(paths)


if __name__ == '__main__':
    main()
