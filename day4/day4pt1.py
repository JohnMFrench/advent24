def n_in_xword(rows: list[str], s: str) -> int:
    n: int = 0

    # build descending diagonals
    # moving top to bottom
    diags: list[str] = []
    for i in range(len(rows)):
        x, y = 0, i
        line = ""
        while y < len(rows) and x < len(rows[y]):
            line += rows[y][x]
            x += 1
            y += 1
        diags.append(line)

    # moving left to right
    for i in range(1, len(rows[0])):
        x, y = i, 0
        line = ""
        while y < len(rows) and x < len(rows[y]):
            line += rows[y][x]
            x += 1
            y += 1
        diags.append(line)

    # Build ascending diagonals
    # moving top to bottom
    for i in range(len(rows)):
        x, y = 0, i
        line = ""
        while y >= 0 and x < len(rows[0]):
            line += rows[y][x]
            x += 1
            y -= 1
        diags.append(line)

    # moving left to right
    for i in range(1, len(rows[0])):
        x, y = i, len(rows) - 1
        line = ""
        while y >= 0 and x < len(rows[0]):
            line += rows[y][x]
            x += 1
            y -= 1
        diags.append(line)

    # Build columns
    cols: list[str] = []
    for x in range(len(rows[0])):
        line = "".join(rows[y][x] for y in range(len(rows)))
        cols.append(line)

    # combine all possible sequences of words
    all_lines = rows + cols + diags
    for line in all_lines:
        # count occurences forward and backwards
        n += line.count(s)
        n += line[::-1].count(s)
    return n


S = "XMAS"
with open("input4.txt") as f:
    grid = f.read().splitlines()
    print(n_in_xword(rows=grid, s=S))
