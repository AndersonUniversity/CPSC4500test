__author__ = 'Ivaan'
'''Nosetest to ensure that functions written
in lab 4 is wokring as it supposed to
Date: 09/27/2015
Prof. Coy and Prof. Tarplee'''

from lab4 import numCheck  # imports numCheck function from lab4
from lab4 import numConvert  # imports numConvert function from lab 4


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

if __name__ == '__main__':
    print(test_numConvert())  # prints number of results with 1089


