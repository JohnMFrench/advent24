from day13 import Button, Machine, get_solution_costs


def test_get_solution_costs_easy():
    a_btn = Button(xmod=1, ymod=3)
    b_btn = Button(xmod=2, ymod=3)

    m = Machine(a_btn=a_btn, b_btn=b_btn)
    sols = get_solution_costs(m=m, ploc=[3, 6])
    print(sols)

    assert sols == 4


def test_get_solution_costs():
    a_btn = Button(xmod=94, ymod=34)
    b_btn = Button(xmod=22, ymod=67)

    m = Machine(a_btn=a_btn, b_btn=b_btn)
    sols = get_solution_costs(m=m, ploc=[8400, 5400])
    print(sols)

    assert sols == 280


def test_get_solution_none():
    a_btn = Button(xmod=26, ymod=66)
    b_btn = Button(xmod=67, ymod=21)

    m = Machine(a_btn=a_btn, b_btn=b_btn)
    sols = get_solution_costs(m=m, ploc=[12748, 12176])
    print(sols)

    assert sols is None
