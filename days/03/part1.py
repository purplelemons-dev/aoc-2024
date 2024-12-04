import re


def pt1(input: list[str]):
    total = 0

    for line in input:
        total += doLine(line)

    return total


def doLine(line: str) -> int:
    found = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)
    total = 0

    for i in found:
        x, y = re.findall(r"\d{1,3}", i)

        subtotal = int(x) * int(y)

        total += subtotal

    return total
