'''09/28/2015 Tyler Jackson Testing Implementation for magic tests.
    Range of all whole numbers from 100 through 999.'''
from . import lab4


def magic_or_not_test():
    for i in range(100, 1000):
        if lab4.decreasing_or_not(i) is True:
            assert lab4.magic_or_not(i) == 1089
