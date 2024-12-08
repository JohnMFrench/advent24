from day8pt2 import num_rep_antinodes


def test_day8pt2():
    with open("test_input8.txt") as f:
        grid = f.read().splitlines(keepends=False)
        res = num_rep_antinodes(grid=grid)
        assert res == 34
