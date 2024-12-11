def get_trailhead_idxs(grid: list[str]) -> list[tuple[int, int]]:
    idxs: list[tuple[int, int]] = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "0":
                ix: tuple[int, int] = (x, y)
                idxs.append(ix)
    return idxs


def get_adjacent_next_steps(grid: list[str], x: int, y: int) -> list[tuple[int, int]]:
    valid_adjacent: list[tuple[int, int]] = []
    dirs = [(-1, 0,), (1, 0,), (0, -1,), (0, 1,)]
    for d in dirs:
        adj_x, adj_y = x + d[0], y + d[1]
        if 0 <= adj_x < len(grid[0]) and 0 <= adj_y < len(grid):
            if int(grid[y][x]) + 1 == int(grid[adj_y][adj_x]):
                valid_adjacent.append((adj_x, adj_y,))
    return valid_adjacent


def get_valid_trail(grid: list[str], start, visited=None, path=None, all_paths=None) -> list:
    # test if values should be initialized on first run
    if visited is None:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    if path is None:
        path = []
    if all_paths is None:
        all_paths = []

    # check if no valid moves are possible
    x, y = start
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or visited[x][y]:
        return []  # this value will be thrown out

    # check if a valid path has been found
    if grid[y][x] == '9':
        all_paths.append(path + [start])
        return all_paths

    # mark the cell as having been visited
    visited[x][y] = True
    path.append(start)

    # find adjacent moves
    adj = get_adjacent_next_steps(grid=grid, x=start[0], y=start[1])
    for ac in adj:
        # move to adjacent cell and recurse
        get_valid_trail(grid=grid, start=ac, visited=visited, path=path, all_paths=all_paths)

    # backtrack to last move before recursing
    # this is the part I was missing!
    visited[x][y] = False
    path.pop()

    return all_paths


def get_trailhead_score(grid: list[str], th: tuple[int, int]) -> int:
    paths = get_valid_trail(grid=grid, start=th)
    end_p = [list(p[-1]) for p in paths]
    up = []
    for p in end_p:
        if p not in up:
            up.append(list(p))
    # print(up)
    return len(up)


def get_trailhead_sum(grid: list[str]) -> int:
    n = 0
    idxs = get_trailhead_idxs(grid=grid)
    for idx in idxs:
        n += get_trailhead_score(grid=grid, th=idx)
    return n


with open("input10.txt") as f:
    grid = f.read().splitlines(keepends=False)
print(get_trailhead_sum(grid=grid))
