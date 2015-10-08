import lab4

__author__ = 'Neal'

"""
testLab4 - file to test the functions in lab4
"""


def test_lab4_functions():
    count = 0
    for i in range(100, 1000):
        if lab4.is_decreasing(i):
            assert lab4.calc(i) == 1089

