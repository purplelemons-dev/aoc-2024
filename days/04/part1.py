def pt1(input: list[str]):
    matrix: list[list[str]] = []

    for line in input:
        matrix.append([char for char in line])

    MAX_X = len(matrix[0])
    MAX_Y = len(matrix)
    DIRECTIONS = {1 + 0j, 1 + 1j, 0 + 1j, -1 + 1j, -1 + 0j, -1 - 1j, 0 - 1j, 1 - 1j}

    def try_crossword(pos: complex, direction: complex):
        for idx, char in enumerate("XMAS"):
            new = pos + idx * direction
            if 0 <= new.real < MAX_X and 0 <= new.imag < MAX_Y:
                if matrix[int(new.imag)][int(new.real)] != char:
                    return False
            else:
                return False
        return True

    total = 0

    for y in range(MAX_Y):
        for x in range(MAX_X):
            pos = complex(x, y)
            for direction in DIRECTIONS:
                if try_crossword(pos, direction):
                    total += 1

    return total
