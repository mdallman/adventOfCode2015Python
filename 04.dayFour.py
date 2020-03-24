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
hashedKey = ''

def tryHash(key,number):
    numString = str(number)
    str(key,numString)
