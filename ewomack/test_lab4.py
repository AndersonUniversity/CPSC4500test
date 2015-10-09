__author__ = 'elliotwomack'


from . import lab4


def test_magic1089():
    assert lab4.magic1089(532) == 1089


def test_magic1089_failed():
    for i in range(100-899):
        assert lab4.magic1089(i) == "Wrong" or lab4.magic1089(i) == 1089
