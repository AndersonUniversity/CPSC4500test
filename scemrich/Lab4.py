__author__ = 'Connor  Emrich'

'''Write down a three-digit number whose digits are decreasing.
Then reverse the digits to create a new number, and subtract
is number from the original number. With the resulting number,
add it to the reverse of itself. The number you will get is 1089'''


def check_decreasenum(number1):
    numberstring = str(number1)
    if numberstring[0] > numberstring[1] > numberstring[2] \
            and 3 == len(numberstring):
        return True
    else:
        return False
''' This function checks that the numbers are decreasing'''


def do_the_math(number1):
    # This function computes the problem

    flipnum = flip_number(number1)
    newval = number1 - flipnum
    newestval = flip_number(newval) + newval
    return newestval


def flip_number(number1):
    # This function flips the number

    flippednum = str(number1)
    stringflippednum = str(flippednum)
    stringflippednum[::-1]
    intflippednum = int(stringflippednum)
    return intflippednum