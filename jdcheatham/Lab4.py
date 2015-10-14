"""J. Cheatham
CPSC4500, lab4"""


""" check number to verify it fits the requirements of decreasing in order"""
def verifyDecrease(number):
    if number[0] < number[1]:
        return ("false")
    else:
        if number[0] < number[2]:
            return ("false")
    return "true"


"""run the number through and show the magic"""
def magic(number):
    numCheck = str(number)
    if len(numCheck) > 3:
        return 0
    checkAgain = verifyDecrease(numCheck)
    if checkAgain == "false":
        return 0
    revNumber = numCheck[::-1]
    revNum = int(revNumber)
    magicNumber = number - revNum
    magicNum = str(magicNumber)
    revMagic = magicNum[::-1]
    revMag = int(revMagic)
    finalNum = revMag + magicNumber
    return finalNum
