'''09/28/2015 Tyler Jackson Testing Implementation for magic tests. Range of all whole numbers from 100 through 999.
    Not working as intended, throws an AssertionError that I can't seem to figure out. Works if asserted with just one number.'''
import lab4

def magic_or_not_test():
    magic_counter = 0
    for i in range(100, 1000):
        if lab4.decreasing_or_not(i) == True:
            assert lab4.magic_or_not(i) == 1089

