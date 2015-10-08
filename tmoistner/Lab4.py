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


def magic():
    """prints 1089"""
    for i in range(100, 999):
        if descending(i):
            difference = i - reverse(i)
            print(difference + reverse(difference))
            print(i)
