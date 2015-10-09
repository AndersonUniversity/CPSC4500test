__author__ = 'Cam-Mac'
"""Tests all 3-digit numbers for Magic 1089 test"""


# makes sure the number is descending
def descent(num):
    num2 = str(num)
    if num2[2] < num2[1] < num2[0]:
        return True
    return False


# does calculations to make sure the test works
def calculate(num):
    num2 = str(num)
    # verifies that the number is 3-digits and each is descending
    if len(num2) == 3 and descent(num) is True:
        # creates backward number
        list1 = [num2[2], num2[1], num2[0]]
        num3 = ''
        for i in list1:
            num3 += i
        # subtracts from original number
        new_num = num - int(num3)
        str_num = str(new_num)
        new_num2 = str(new_num)
        list2 = [new_num2[2], new_num2[1], new_num2[0]]
        new_num3 = ''
        # creates back ward number
        for i in list2:
            new_num3 += i
        # adds the newer 2 numbers
        result = new_num + int(new_num3)
        str_result = str(result)
        # verifies that each of these equals 1089
        print(num2 + ' - ' + num3 + ' = ' + str_num + ' + ' +
              new_num3 + ' = ' + str_result)
