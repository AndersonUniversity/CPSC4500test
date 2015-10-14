"""J. Cheatham
CPSC4500, lab4"""


def magic(number):
    """run the number through and show the magic"""
    numCheck = str(number)
    revNumber = numCheck[::-1]
    revNum = int(revNumber)
    magicNumber = number - revNum
    magicNum = str(magicNumber)
    revMagic = magicNum[::-1]
    revMag = int(revMagic)
    finalNum = revMag + magicNumber
    return finalNum
