def pt2(input: list[str]):
    total = 0
    for line in input:
        total += int(doLine(line))

    return total


def doLine(line: str):
    numbers = line.split(" ")
    analyzed = []
    for i in range(len(numbers) - 1):
        analyzed.append(int(numbers[i]) - int(numbers[i + 1]))

    if not (
        all([3 >= x >= 1 for x in analyzed]) or all([-3 <= x <= -1 for x in analyzed])
    ):
        for idx in range(len(numbers)):
            newNumbers = numbers.copy()
            newNumbers.pop(idx)
            newAnalyzed = []

            for i in range(len(newNumbers) - 1):
                newAnalyzed.append(int(newNumbers[i]) - int(newNumbers[i + 1]))

            if all([3 >= x >= 1 for x in newAnalyzed]) or all(
                [-3 <= x <= -1 for x in newAnalyzed]
            ):
                return True

        return False

    return True
