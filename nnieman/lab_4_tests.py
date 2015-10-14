"""Nose tests for lab_4"""

from .lab_4 import math_magic


def test_math_magic():
    for i in range(100, 1000):
        magic_result = math_magic(i)
        print("Checking {}; magic result = {}.".format(i, magic_result))
        assert magic_result is None or magic_result == 1089
