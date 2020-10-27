#############################
# Advent of Code 2015 Day 4 #
#     By Matt Dallman       #
#############################

import hashlib

#initialise variables
secretKey = 'yzbqklnj'
testSecretKey = 'abcdef'
testSecretKeyTwo = 'pqrstuv'
leadingNumber = 0
fiveZeros = False
sixZeros = False

def tryHash(key,number):
    #combines the two strings hashes them and returns the hex.
    numString = str(number)
    hashKey = key+numString
    hashedKey = hashlib.md5(hashKey.encode())
    hexKey = hashedKey.hexdigest()
    return hexKey

def checkFiveZeros(md5Hash):
    if md5Hash[0:5] == '00000':
        return True
    else:
        return False

def checkSixZeros(md5Hash):
    if md5Hash[0:6] == '000000':
        return True
    else:
        return False

while fiveZeros == False:
    leadingNumber += 1
    activeKey = tryHash(secretKey,leadingNumber)
    fiveZeros = checkFiveZeros(activeKey)

print('The first positive number that gives 5 leading zeros for',secretKey,'is',leadingNumber)


while sixZeros == False:
    leadingNumber += 1
    activeKey = tryHash(secretKey,leadingNumber)
    sixZeros = checkSixZeros(activeKey)

print('The first positive number that gives 6 leading zeros for',secretKey,'is',leadingNumber)
