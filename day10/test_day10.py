from day10pt1 import get_trailhead_idxs, get_adjacent_next_steps, get_trailhead_score, get_trailhead_sum

with open("test_input10.txt") as f:
    tgrid = f.read().splitlines(keepends=False)


def test_get_trailhead_idxs():
    idxs = get_trailhead_idxs(grid=tgrid)
    print(idxs)
    assert len(idxs) == 9


def test_get_adjacent_next_steps():
    # assert len(get_adjacent_next_steps(tgrid, 0, 0)) == 2
    assert len(get_adjacent_next_steps(tgrid, 7, 6)) == 2


def test_get_trailhead_score():
    res = get_trailhead_score(grid=tgrid, th=(2, 0,))
    # res2 = get_trailhead_score(grid=tgrid, th=(6, 6,))
    res3 = get_trailhead_score(grid=tgrid, th=(4, 0,))
    assert res3 == 6 and res == 5
    # assert res == 1 and res2 == 2


def test_get_trailhead_sum():
    res = get_trailhead_sum(grid=tgrid)
    assert res == 36
