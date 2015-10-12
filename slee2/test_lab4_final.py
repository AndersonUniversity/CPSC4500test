import lab4_final
__author__ = 'sLee'
''' In unit test (use nosetests), use range() to generate a list that contains all numbers from 100 to 999.'''


def test_generate_num():
    """ unit test that generate nums and execute functions. """
    for x in range(100, 1000):
        if lab4_final.check_valid(x):
            finalnum = lab4_final.magic_n(x)
            print(finalnum)
            assert finalnum == 1089
