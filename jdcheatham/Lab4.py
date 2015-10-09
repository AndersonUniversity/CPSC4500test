"""J. Cheatham
CPSC4500, lab4"""

def verifyDecrease(number):

    if number[0] < number[1]:
        return ("false")
    else:
        if number[0] < number[2]:
            return ("false")
    return "true"

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


