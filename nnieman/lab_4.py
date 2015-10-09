"""A program to calculate the `Magic Number` procedure for a number."""


def verify_digits_decreasing(num):
    """Return True if the digits of a number are
       strictly decreasing or False otherwise."""
    last_digit = None

    for digit_str in str(num):
        digit_int = int(digit_str)
        if last_digit is not None and digit_int >= last_digit:
            return False

        last_digit = digit_int

    return True


def reverse_number(num):
    """Reverse a number in base-10 digit for digit."""
    return int(str(num)[::-1])


def math_magic(num):
    """Return the result of the `Magic Number` procedure for a number."""
    if not verify_digits_decreasing(num):
        return None

    reversed_num = reverse_number(num)

    difference = num - reversed_num

    reversed_difference = reverse_number(difference)

    return difference + reversed_difference
