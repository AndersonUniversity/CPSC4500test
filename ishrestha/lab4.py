__author__ = 'Ivaan'
''' Lab 4:Python module to verify that the Magic 1089 trick is indeed true
Prof. Kyle and Prof. Coy'''


def numCheck(num):

    '''this function takes a number as an argument
    and verifies that the digits are in decreasing order'''
    b = str(num)  # converting the number to string
    a = len(b)  # getting a length of string
    if a != 3:  # making sure there are only 3 digits
        return False
    else:  # if only 3 digits
        if int(b[0]) > int(b[1]) and int(b[1]) > int(b[2]):  # decreasing order
            return True  # returns true
        else:
            return False  # return false if not in decresing order


def numConvert(a):

    '''this function converts the number to 1089 after calculations'''
    b = str(a)  # converts to string
    if numCheck(b):  # checks if it is of 3 length and in decreasing order
        '''some varibale assignments I know we can use slice'''
        f = b[2]
        s = b[1]
        t = b[0]
        newNum = f+s+t  # adding all these together
        newNum = int(newNum)  # convert to int
        newNum1 = a - newNum  # reversed number of original number
        newNum1 = str(newNum1)  # convert to string
        newNum2 = newNum1[::-1]  # reversing the number
        newNum2 = int(newNum2)  # converting to string
        newNum1 = int(newNum1)  # converting to string
        newNum = newNum1 + newNum2  # adding to numbers
        return newNum  # returns value 1089

    else:  # if less or greater
        return None  # just nothing
