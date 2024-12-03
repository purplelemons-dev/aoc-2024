from part1 import sortLines


def pt2(input: list[str]):
    left, right = sortLines(input)
    total = 0

    for i in left:
        total += i * right.count(i)

    return total
