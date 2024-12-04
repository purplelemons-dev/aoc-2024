def pt1(input: list[str]):
    total = 0
    for line in input:
        total += int(doLine(line))

    return total


def doLine(line: str):
    numbers = line.split(" ")
    analyzed = []
    for i in range(len(numbers) - 1):
        analyzed.append(int(numbers[i]) - int(numbers[i + 1]))

    return all([3 >= x >= 1 for x in analyzed]) or all(
        [-3 <= x <= -1 for x in analyzed]
    )
