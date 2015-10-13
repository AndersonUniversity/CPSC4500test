from . import Lab4


def test_Lab4():
    for i in range(100, 999):
        if Lab4.decrease(i):
            assert Lab4.trick(i) == 1089
