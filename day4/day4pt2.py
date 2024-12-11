def is_masful(grid, x, y) -> bool:
    if (
        grid[y][x] == 'M' and
        grid[y + 2][x] == 'M' and
        grid[y + 1][x + 1] == 'A' and
        grid[y][x + 2] == 'S' and
        grid[y + 2][x + 2] == 'S'
    ) or (
        grid[y][x] == 'M' and
        grid[y + 2][x] == 'S' and
        grid[y + 1][x + 1] == 'A' and
        grid[y][x + 2] == 'M' and
        grid[y + 2][x + 2] == 'S'
    ) or (
        grid[y][x] == 'S' and
        grid[y + 2][x] == 'S' and
        grid[y + 1][x + 1] == 'A' and
        grid[y][x + 2] == 'M' and
        grid[y + 2][x + 2] == 'M'
    ) or (
        grid[y][x] == 'S' and
        grid[y + 2][x] == 'M' and
        grid[y + 1][x + 1] == 'A' and
        grid[y][x + 2] == 'S' and
        grid[y + 2][x + 2] == 'M'
    ):
        return True
    return False


with open('input4.txt') as f:
    grid = f.read().splitlines()

n = 0
for y in range(len(grid) - 2):
    for x in range(len(grid[y]) - 2):
        if is_masful(grid, x, y):
            n += 1

print(n)