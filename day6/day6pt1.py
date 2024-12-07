from typing import TypedDict


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
    grid: list[str] = f.read().splitlines(keepends=False)

# find starting Location of guard and store as gx, gy
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] in g_map.keys():
            gx: int
            gy: int
            gx, gy = x, y  # starting location
            g = grid[y][x]  # starting guard direction

visited: set[Loc] = set()  # counting unique spaces traveled
moves: list[str] = []  # for debugging move sequence

# keep moving guard until leaving the map
while True:
    # find the next index guard moves to
    next_x: int = gx + g_map[g]["mod"][0]
    next_y: int = gy + g_map[g]["mod"][1]

    # rotate 90 deg if next move is an obstacle
    if grid[next_y][next_x] == "#":
        moves.append(f"{g} turns to {g_map[g]['next']} at ({gx+1},{gy+1})")
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
            break

print(len(visited))
