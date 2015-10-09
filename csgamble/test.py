__author__ = 'Cam-Mac'
"""Test file for Magic 1089"""


import Magic


# creates a list of numbers 100-999
container = range(100, 999)


# runs the test
def test_yes():
    for i in container:
        Magic.calculate(i)
