def pt1(input: list[str]):
    total = 0

    for i, j in zip(sortLines(input)):
        distance = abs(i - j)
        total += distance

    return total


def doLine(line: str):
    x, y = line.split()
    return int(x), int(y)


def sortLines(input: list[str]) -> tuple[list[int], list[int]]:
    left, right = [], []
    for line in input:
        x, y = doLine(line)

        left.append(x)
        right.append(y)

    left.sort()
    right.sort()

    return left, right
