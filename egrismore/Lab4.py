__author__ = 'emilygrismore'
"""checks requirements for and runs the magic 1089"""


def flip(i):
    """reverses the number"""
    int(str(i)[::-1])
    return i


def decrease(i):
    """checks to see if the #'s are in descending order"""
    largest = 10
    for new in str(i):
        number = int(new)
        if number >= largest:
            return False
        else:
            largest = number
    return True


def trick():
    """shows the magical 1089"""
    for i in range(100, 999):
        if decrease(i):
            difference = i - flip(i)
            difference + flip(difference)
            print(i)
