'''09/28/2015 Tyler Jackson  Functions that handle testing for magic numbers.
    Includes a function to test to see if the number
    is in magic number format, meaning decreasing,
    and a function to reverse a number.'''


def decreasing_or_not(pInt):
    '''Checks whether or not the passed in int is
    decreasing or not, returning a bool.'''
    int_array = list(map(int, str(pInt)))
    for i in range(0, len(int_array)-1):
        if int_array[i] <= int_array[i+1]:
            return False
    return True


def reverse_number(pInt):
    '''Reverses a passed in int, returning the reversal.'''
    int_string = str(pInt)
    int_reversed = int(int_string[::-1])
    return int_reversed


def magic_or_not(pInt):
    '''Tests whether or not the passed in int is a "magic"
    number or not. Returns 1089 if it is.'''
    if pInt > 99 and pInt < 1000:
        step_one = pInt - reverse_number(pInt)
        step_two = step_one + reverse_number(step_one)
        return step_two
    return None
