__author__ = 'sLee'
'''
Lab3
Samuel Lee
Sept/28/2015
Goal is to Write a Python module to verify that the Magic 1089 trick
is indeed true.
This program should:
Have a function that takes a number as an argument and verifies that
the digits are in decreasing order,
returning True if they are and False if not.
The digits must be strictly decreasing,
since the Magic 1089 trick does not
work for numbers like 988, where two digits are equal.
# One way to do this is to convert the number to a string using
the str() function, then use a for loop to compare neighboring characters.
Have a function that takes a number as an argument. If the number is
three digits, and the digits are in decreasing order, then the function
should perform the above calculations and return the result
(which should be 1089) as an integer.
'''


def magic_n(n):  # n is a list contain three int
    """ calculating magic number """
    print("numb valid = ", n)
    g = str(n)
    # g list type <list> = <string>.split()
    # g should store each string type number in list separately []
    a = g[0]
    c = g[2]
    fd = str(99*(int(a)-int(c)))
    rfd = ''.join(reversed(fd))
    result = int(fd) + int(rfd)
    # print(fd, rfd, diff)
    # rdiff = ''.join(reversed(str(diff)))
    # result = diff + int(rdiff)
    return result


def check_valid(n):
    """ Check if parameter is valid for magic num fuction.
        Descending order, 3 integers etc. """
    # print("testing numb = ", n)
    if len(str(n)) != 3:
        print("not valid length")
        return False
    g = str(n)
    a, b, c = g
    if int(a) <= int(b):
        # print("first int is less than second int")
        return False
    if int(b) <= int(c):
        # print("second int is less than third int")
        return False

    return True
