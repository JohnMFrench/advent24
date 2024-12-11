from day10pt1 import get_trailhead_idxs, get_valid_trail


def get_trailhead_rating(grid: list[str], th: tuple[int, int]) -> int:
    paths = get_valid_trail(grid=grid, start=th)
    return len(paths)


def get_trailhead_rating_sum(grid: list[str]) -> int:
    n = 0
    idxs = get_trailhead_idxs(grid=grid)
    for idx in idxs:
        n += get_trailhead_rating(grid=grid, th=idx)
    return n


with open("input10.txt") as f:
    grid = f.read().splitlines(keepends=False)
print(get_trailhead_rating_sum(grid=grid))
