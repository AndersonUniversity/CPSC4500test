from . import Lab4


def test_lab4():
    for i in range(100, 999):
        if Lab4.descending(i):
            Lab4.magic(i)
