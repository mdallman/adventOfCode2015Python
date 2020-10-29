#############################
# Advent of Code 2015 Day 5 #
#     By Matt Dallman       #
#############################
#Imports
import csv

# Main Function for the code
def main():
    numberOfNiceStrings = 0
    f = open('dayFive.csv','r')
    reader = csv.reader(f)
    for entry in reader:
        if isNice(entry[0]):
            numberOfNiceStrings += 1
    print(numberOfNiceStrings)        


#Define the Check if Nice String Function

def isNice(aString):
    #Checks the three conditions
    if (threeVowels(aString)):
        if (doubleLetters(aString)):
            if (not containsLetters(aString)):
                return True
                
    return False

#Define check if at least three vowels
def threeVowels(aString):
    vowels = ['a','e','i','o','u']
    vowelCount = 0

    for letter in aString:
        for vowel in vowels:
            if (vowel == letter):
                vowelCount += 1
        
    if (vowelCount >= 3):
        return True
    else:
        return False
            
        

#Define check for at least one set of  double letters
def doubleLetters(aString):
    n = len(aString)
    x = 0
    i = 1

    while i < n:
        if aString[x] == aString[i]:
            return True
        else:
            x += 1
            i += 1
    return False
        

#TODO Define Check for strings 'ab' 'cd' 'pq' 'xy'
def containsLetters(aString):
    letters = ['ab','cd','pq','xy']
    n = len(aString)
    x = 0
    

    while x < n:
        for l in letters:
            if aString[x:x+2] == l:
                return True
        x += 1   
    return False
        
