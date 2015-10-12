from . import Lab4


def test_Lab4():
    '''nose test that cycles through all of the three digit numbers'''
    for i in range(100, 999):
       if Lab4.check_decreasenum(i):
           Lab4.do_the_math(i)
    print(i)
