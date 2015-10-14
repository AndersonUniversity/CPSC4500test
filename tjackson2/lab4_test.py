'''09/28/2015 Tyler Jackson Testing Implementation for magic tests.
    Range of all whole numbers from 100 through 999.'''
from . import lab4


def magic_or_not_test():
    '''Testing of functionality of lab4.py to check to make
    sure that any three digit number will, if decreasing,
    return 1089.'''
    for i in range(100, 1000):
        if (lab4.decreasing_or_not(i)):
            assert lab4.magic_or_not(i) == 1089
