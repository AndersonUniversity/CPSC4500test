__author__ = 'emilygrismore'
"""checks requirements for and runs the magic 1089"""


def flip(i):
    """reverses the number"""
    return int(str(i)[::-1])


def decrease(i):
    """checks to see if the #s are in descending order"""
    largest = 10
    for new in str(i):
        number = int(new)
        if number >= largest:
            return False
        else:
            largest = number
    return True


def trick(i):
    """shows the magical 1089"""
    difference = i - flip(i)
    final = difference + flip(difference)
    return final
