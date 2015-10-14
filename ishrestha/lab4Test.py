__author__ = 'Ivaan'
'''Nosetest to ensure that functions written
in lab 4 is wokring as it supposed to
Prof. Coy and Prof. Tarplee'''

from lab4 import numCheck, numConvert


def test_numCheck():

    '''to test numCheck'''
    flag = True
    for i in range(100, 999):
        assert numCheck(i) == flag


def test_numConvert():

    '''to test numConvert'''
    count = 0
    for i in range(100, 999):
        if numConvert(i) == 1089:
            count = count + 1
        else:
            count = count

    return count
