class InvalidLetterError(Exception):
    def __init__(self, message = 'You entered invalid letter for hex number'):
        super().__init__(message)


class InvalidDecimalBaseError(Exception):
    def __init__(self, message = 'You entered invalid decimal base for hex number'):
        super().__init__(message)


def convertFromHexBaseToDecimalBase(n):
    match n:
        case 'a' | 'A':
            return 10
        case 'b' | 'B':
            return 11
        case 'c' | 'C':
            return 12
        case 'd' | 'D':
            return 13
        case 'e' | 'E':
            return 14
        case 'f' | 'F':
            return 15
        case _:
            raise InvalidLetterError()


def convertFromDecimalBaseToHexBase(n):
    match n:
        case 10:
            return 'a'
        case 11:
            return 'b'
        case 12:
            return 'c'
        case 13:
            return 'd'
        case 14:
            return 'e'
        case 15:
            return 'f'
        case _:
            raise InvalidDecimalBaseError()


def fromHexToBigEndian(num):
    length = len(num)
    reversednum = num[length:1:-1]
    arrayOfDigit = []
    for i in range(len(reversednum)):
        if not reversednum[i].isdigit():
            arrayOfDigit.append(convertFromHexBaseToDecimalBase(reversednum[i]))
        else:
            arrayOfDigit.append(reversednum[i])
    resultnum = 0
    for i in range(len(arrayOfDigit)):
        resultnum += pow(16, i) * int(arrayOfDigit[i])
    return resultnum


def fromHextoLittleEndian(num):
    length = len(num)
    slicednum = num[2:length:1]
    arrayOfReversedPairs = []
    for i in range(1, len(slicednum), 2):
        arrayOfReversedPairs.append(slicednum[i])
        arrayOfReversedPairs.append(slicednum[i-1])
    arrayOfDigit = []
    for i in range(len(arrayOfReversedPairs)):
        if not arrayOfReversedPairs[i].isdigit():
            arrayOfDigit.append(convertFromHexBaseToDecimalBase(arrayOfReversedPairs[i]))
        else:
            arrayOfDigit.append(arrayOfReversedPairs[i])
    resultnum = 0
    for i in range(len(arrayOfDigit)):
        resultnum += pow(16, i) * int(arrayOfDigit[i])
    return resultnum


def fromBigEndianToHex(num):
    copynum = num
    resstr = ''
    while copynum != 0:
        remainder = copynum % 16
        if remainder < 10:
            resstr += str(remainder)
        else:
            resstr += convertFromDecimalBaseToHexBase(remainder)
        copynum = copynum // 16  
    resstr += 'x0'
    resulting = resstr[::-1]
    return resulting


def fromLittleEndianToHex(num):
    copynum = num
    resstr = ''
    while copynum != 0:
        remainder = copynum % 16
        if remainder < 10:
            resstr += str(remainder)
        else:
            resstr += convertFromDecimalBaseToHexBase(remainder)
        copynum = copynum // 16  
    reversedpairs = ''
    for i in range(1, len(resstr), 2):
        reversedpairs += resstr[i]
        reversedpairs += resstr[i-1]
    resulting = '0x' + reversedpairs
    return resulting

