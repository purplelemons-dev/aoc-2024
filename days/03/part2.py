import re


def pt2(input: list[str]):
    total = 0
    enabled = True

    for line in input:
        subtotal, enabled = doLine(line, enabled)
        total += subtotal

    return total


def doLine(line: str, enabled: bool) -> tuple[int, bool]:
    found = re.findall(r"(mul\(\d{1,3},\d{1,3}\))|(do(n\'t){,1}\(\))", line)
    total = 0

    for i in found:
        if any(j == "do()" for j in i):
            enabled = True
        elif any(j == "don't()" for j in i):
            enabled = False

        elif enabled:
            x, y = re.findall(r"\d{1,3}", i[0])

            subtotal = int(x) * int(y)
            total += subtotal

    return total, enabled
