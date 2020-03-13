########################
# Advent of Code Day 2 #
#  By Matt Dallman     #
########################


#Given a present with sides l, w, h
#Part 1 - Find the amount of wrapping paper needed.

#calculates the amount of wrapping paper per present.
def calculateWrapping(sizes):

    #Get the length of the sides from string
    sides = sizes.split('x')
    l = int(sides[0])
    w = int(sides[1])
    h = int(sides[2])

    #Calculate the area of each side.
    lw = l * w
    lh = l * h
    wh = w * h

    #Calculate the smallest side
    smallestSide = lw
    if smallestSide > lh:
        smallestSide = lh
    elif smallestSide > wh:
        smallestSide = wh

    #Calculates the amount of paper needed
    paperNeeded = (2 * lw) + (2 * lh) + (2 * wh) + smallestSide
    return paperNeeded
    
#takes the list and iterates using calculateWrapping
def allWrapping():
    totalPaper = 0
    #f = open("dayTwoTest.txt", "r") #uses the test file
    f = open("dayTwoInput.txt", "r") #The project input file
    for line in f:
        totalPaper += calculateWrapping(line)

    return totalPaper

print("The total amount of wrapping paper needed is:", allWrapping())
