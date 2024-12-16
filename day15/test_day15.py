from day15 import Loc, Robot, Map


def test_is_pushable_in_dir():
    with open("test_input15.txt") as f:
        smap, smoves = f.read().split("\n\n")
    map: Map = Map.parse_string(smap)
    print(map.to_str())

    assert not map.is_pushable_in_dir(0, -1, Loc(x=3, y=1))
    assert not map.is_pushable_in_dir(1, 0, Loc(x=8, y=1))
    assert not map.is_pushable_in_dir(0, 1, Loc(x=5, y=8))
    assert not map.is_pushable_in_dir(0, 1, Loc(x=5, y=7))
    assert map.is_pushable_in_dir(-1, 0, Loc(x=4, y=7))


def test_robot_movable_in_dir():
    with open("test_input15.txt") as f:
        smap, smoves = f.read().split("\n\n")
    map: Map = Map.parse_string(smap)
    print(map.to_str())

    assert map.is_robot_movable_in_dir(xmod=-1, ymod=0, loc=Loc(x=3, y=4))
    assert not map.is_robot_movable_in_dir(xmod=-1, ymod=0, loc=Loc(x=2, y=5))
