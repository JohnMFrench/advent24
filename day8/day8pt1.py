def num_antinodes(grid: list[str]) -> int:
    """calculates the number of antinodes in the map

    Args:
        grid (list[str]): puzzle map. antennae are represented
        by any ascii character or digit

    Returns:
        int: num of unique antinodes on map
    """
    # antinode locations as x, y pairs
    alocs: set[tuple[int]] = set()

    # antennae indices
    aix: dict[str, list[tuple[int]]] = {
        c: list() for c in set("".join(grid).replace(".", ""))
    }

    # iterate through map and find antennae indices
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != ".":
                aix[grid[y][x]].append(tuple([x, y]))

    # calculate any antinode locations that will fall on the map
    # loop through each antenna freq
    for a, locs in aix.items():
        # loop through each location of an antenna
        for i in range(len(locs)):
            # loop through each other antennae of same freq
            for i2 in range(len(locs)):
                if i != i2:
                    # substract distance to find location if one antenna is
                    # twice as far away
                    modx = locs[i][0] + (locs[i][0] - locs[i2][0])
                    mody = locs[i][1] + (locs[i][1] - locs[i2][1])

                    # check if it falls within the map
                    if 0 <= modx < len(grid[0]) and 0 <= mody < len(grid):

                        # add to list of known antinode locs
                        alocs.add(tuple([modx, mody]))
                        # print(f"found {a} 'node at ({modx},{mody})")
    return len(alocs)


with open("input8.txt") as f:
    grid = f.read().splitlines(keepends=False)
    print(num_antinodes(grid=grid))
