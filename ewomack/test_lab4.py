__author__ = 'elliotwomack'


from . import lab4


def is_decreasing(foo):
    if(foo[0] > foo[1] > foo[2]):
        return True
    return False


def test_magic1089():
    assert lab4.magic1089(532) == 1089


def test_magic1089_failed():
    for i in range(100-899):
        if is_decreasing(i):
            assert lab4.magic1089(i) == 1089
