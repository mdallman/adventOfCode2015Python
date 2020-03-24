########################
# Advent of Code Day 4 #
#  By Matt Dallman     #
########################

import hashlib

#initialise variables
secretKey = 'yzbqklnj'
testSecretKey = 'abcdef'
testSecretKeyTwo = 'pqrstuv'
leadingNumber = 0

def tryHash(key,number):
    #combines the two strings hashes them and returns the hex.
    numString = str(number)
    hashKey = key+numString
    hashedKey = hashlib.md5(hashKey.encode())
    hexKey = hashedKey.hexdigest()
    return hexKey
