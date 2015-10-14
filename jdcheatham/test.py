"""J. Cheatham
CPSC4500, Lab4Test"""


from . import Lab4


def verifyDecrease(number):
    """ check number to verify it fits the requirements of
    decreasing in order"""
    numCheck = str(number)

    if len(numCheck) > 3:
        return False

    if numCheck[0] <= numCheck[1]:
        return False

    if numCheck[1] <= numCheck[2]:
        return False

    return True


def test_magic():
    """test function for magic 1098 (lab 4)"""
    for number in range(100, 999):
        if verifyDecrease(number):
            print(Lab4.magic(number))
            assert Lab4.magic(number) == 1089
