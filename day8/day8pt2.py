def num_rep_antinodes(grid: list[str]) -> int:
    """calculates the number of repeating antinodes in the map

    Args:
        grid (list[str]): puzzle map. antenna are represented
        by any ascii character or digit

    Returns:
        int: num of unique antinodes on map
    """
    # antinode locations as x, y pairs
    alocs: set[tuple[int]] = set()

    # antenna indices
    aix: dict[str, list[tuple[int]]] = {
        c: list() for c in set("".join(grid).replace(".", ""))
    }

    # iterate through map and find antenna indices
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != ".":
                aix[grid[y][x]].append(tuple([x, y]))

    # calculate any antinode locations that will fall on the map
    # loop through each antenna freq
    for a, locs in aix.items():
        # loop through each location of an antenna
        for i in range(len(locs)):
            # loop through each other antenna of same freq
            for i2 in range(len(locs)):
                next_aloc = list([locs[i][0], locs[i][1]])
                modx = locs[i][0] - locs[i2][0]
                mody = locs[i][1] - locs[i2][1]
                next_aloc[0] = next_aloc[0] + modx
                next_aloc[1] = next_aloc[1] + mody

                # repeat searching for an antidote the same distance away within the map
                while 0 <= next_aloc[0] < len(grid[0]) and 0 <= next_aloc[1] < len(
                    grid
                ):
                    # add to set of known node locations
                    alocs.add(tuple(next_aloc))
                    # find the next repeated location
                    next_aloc[0] = next_aloc[0] + modx
                    next_aloc[1] = next_aloc[1] + mody
                    # do not keep looping over the same antenna
                    if i == i2:
                        break
    return len(alocs)


with open("input8.txt") as f:
    grid = f.read().splitlines(keepends=False)
    print(num_rep_antinodes(grid=grid))
