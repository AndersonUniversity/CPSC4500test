__author__ = 'Neal'

"""
Lab4 - to determine which 3 digit numbers are Magic 1089 numbers
"""


def is_decreasing(foo):
    """
    function to see if the numbers are decreasing
    """
    num = str(foo)  # used for new string being created
    if foo > 999:
        return False
    # loops through the int and see if the numbers are decreasing
    if (num[0] > num[1]) and (num[1] > num[2]):
        return True
    return False


def calc(foo):
    """
    function to calc and see if it is a 1089 number
    """
    num = str(foo)
    reverse1 = num[::-1]
    sub = foo - int(reverse1)
    num2 = str(sub)
    reverse2 = num2[::-1]
    total = sub + int(reverse2)
    return total
