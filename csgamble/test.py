__author__ = 'Cam-Mac'
"""Test file for Magic 1089"""


from . import Magic


# runs the test
def test_yes():
    # creates a list of numbers 100-999
    container = range(100, 999)
    for i in container:
        Magic.calculate(i)
