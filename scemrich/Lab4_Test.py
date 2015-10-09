__author__ = 'Connor  Emrich'

from  . import Lab4


def test_Lab4():
    for i in range(100,999):
       if Lab4.check_decreasenum(i) == True:
           Lab4.do_the_math(i)
    print(i)

#nose test that cycles through all of the three digit numbers