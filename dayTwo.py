########################
# Advent of Code Day 2 #
#  By Matt Dallman     #
########################


#Given a present with sides l, w, h
#Part 1 - Find the amount of wrapping paper needed.

def calculateWrapping(sizes):

    #Get the length of the sides from string
    l = 1
    w = 2
    h = 3

    #Calculate the area of each side.
    lw = l * w
    lh = l * h
    wh = w * h

    #Calculate the smallest side
    smallestSide = lw

    #Calculates the amount of paper needed
    paperNeeded = (2 * lw) + (2 * lh) + (2 * wh) + smallestSide
    
