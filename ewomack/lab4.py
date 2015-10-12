__author__ = 'elliotwomack'
""" Test the magic 1089 """


def reverse(foo):
    """reverse a number"""
    numSplit = list(str(foo))
    return numSplit[2] + numSplit[1] + numSplit[0]


def magic1089(foo):
    """test magic 1089"""
    num = foo - int(reverse(foo))
    return num + int(reverse(num))
