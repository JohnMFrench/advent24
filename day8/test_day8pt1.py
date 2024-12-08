from day8pt1 import num_antinodes


def test_day8pt1():
    with open("test_input8.txt") as f:
        grid = f.read().splitlines(keepends=False)
        res = num_antinodes(grid=grid)
        assert res == 14
