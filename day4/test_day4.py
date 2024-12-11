from day4pt1 import n_in_xword


def test_n_in_xword():
    S = 'XMAS'
    with open('input4.txt') as f:
        grid = f.read().splitlines()
        n = n_in_xword(rows=grid, s=S)

    with open('test_input4.txt') as f:
        grid = f.read().splitlines()
        test_n = n_in_xword(rows=grid, s=S)

        assert test_n == 18 and n == 2370
