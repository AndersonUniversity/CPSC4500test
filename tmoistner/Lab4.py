__author__ = 't'


"""does magic tricks"""


def reverse(i):
    """reverses number"""
    return int(str(i)[::-1])


def descending(i):
    """checks that number is descending"""
    largest = 10
    for c in str(i):
        x = int(c)
        if x >= largest:
            return False
        else:
            largest = x
    return True


def magic(i):
    """prints 1089"""
    difference = i - reverse(i)
    result = difference + reverse(difference)
    return result
