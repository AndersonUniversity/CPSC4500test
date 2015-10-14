"""J. Cheatham
CPSC4500, Lab4Test"""


import Lab4


"""test function for magic 1098 (lab 4)"""
def test_magic():
    for number in range(100, 999):
        assert Lab4.magic(number) == 1098
