__author__ = 'elliotwomack'
""" Test the magic 1089 """


def is_decreasing(foo):
    if(foo[0] > foo[1] > foo[2]):
        return True
    return False


def reverse(foo):
    """reverse a number"""
    numSplit = list(str(foo))
    return numSplit[2] + numSplit[1] + numSplit[0]


def magic1089(foo):
    """test magic 1089"""
    if(is_decreasing(list(str(foo)))):
        num = foo - int(reverse(foo))
        return num + int(reverse(num))
    return "You didnt enter an increasing number."
