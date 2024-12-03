def pt1(input: list[str]):
    left, right = [], []
    for line in input:
        x, y = doLine(line)

        left.append(x)
        right.append(y)

    left.sort()
    right.sort()

    total = 0

    for i, j in zip(left, right):
        distance = abs(i - j)
        total += distance

    return total


def doLine(line: str):
    x, y = line.split()
    return int(x), int(y)
