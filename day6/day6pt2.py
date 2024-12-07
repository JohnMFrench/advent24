from typing import TypedDict
import copy
from tqdm import tqdm


# state of guard
class GuardDetails(TypedDict):
    mod: tuple[int, int]
    next: str


# location on the puzzle map
class Loc:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        if isinstance(other, Loc):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self) -> int:
        return hash((self.x, self.y))


# map of guard states
g_map: dict[str, GuardDetails] = {
    ">": {"mod": (1, 0), "next": "V"},
    "V": {"mod": (0, 1), "next": "<"},
    "<": {"mod": (-1, 0), "next": "^"},
    "^": {"mod": (0, -1), "next": ">"},
}

with open("input6.txt") as f:
    sgrid: list[str] = f.read().splitlines(keepends=False)

# find starting Location of guard and store as gx, gy
for y in range(len(sgrid)):
    for x in range(len(sgrid[y])):
        if sgrid[y][x] in g_map.keys():
            sx: int
            sy: int
            sx, sy = x, y  # starting location
            sg = sgrid[y][x]  # starting guard direction

# define N possible moves as number of indices in grid
max_moves = len(sgrid) * len(sgrid[0])
obstacle_locs = 0


def times_out(grid, gx, gy, g) -> bool:
    visited: set[Loc] = set()  # counting unique spaces traveled
    moves: list[str] = []  # for debugging move sequence
    # keep moving guard until leaving the map
    while True:
        # find the next index guard moves to
        next_x: int = gx + g_map[g]["mod"][0]
        next_y: int = gy + g_map[g]["mod"][1]

        try:
            # rotate 90 deg if next move is an obstacle
            if grid[next_y][next_x] == "#":
                moves.append(
                    f"{g} turns to {g_map[g]['next']} at ({gx+1},{gy+1})"
                )
                g = g_map[g]["next"]
            else:
                # count the current Location as visited
                visited.add(Loc(x=gx, y=gy))

                # move the guard
                gx = next_x
                gy = next_y
                moves.append(f"{g} moves to ({next_x+1},{next_y+1})")

                # check if the guard has left the map
                if not (0 <= gx < len(grid[0]) and 0 <= gy < len(grid)):
                    return False
                elif len(moves) > max_moves:
                    return True
        except IndexError:
            print(f"index error at {next_x},{next_y}")


num_counted = 0
for y in tqdm(range(len(sgrid)), "counting by row"):
    for x in range(len(sgrid[y])):
        tgrid = copy.deepcopy(sgrid)
        tgrid = [list(row) for row in sgrid]  # Convert rows to lists
        tgrid[y][x] = "#"
        if times_out(tgrid, sx, sy, sg):
            obstacle_locs += 1
            print("found obstacle")
        num_counted += 1
        # print(num_counted)

print(obstacle_locs)
