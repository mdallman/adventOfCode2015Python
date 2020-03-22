########################
# Advent of Code Day 3 #
#  By Matt Dallman     #
########################

#Initialise Variables
xSanta = 0
ySanta = 0
santaPosition = [xSanta,ySanta]
santaHouse = []
housesVisited = 0

def movement(direction):
    #Declare variables
    global xSanta
    global ySanta
    global santaPosition

    #Reads instructions and moves santa based on them
    if direction == 'v':
        ySanta -= 1
    elif direction == '^':
        ySanta += 1
    elif direction == '>':
        xSanta += 1
    elif direction == '<':
        xSanta -= 1

    santaPosition = [xSanta,ySanta]

def checkHouse(position):
    global santaPosition
    global santaHouse
    global housesVisited

    #check if santaPosition exists in housesVisited
    #How to check, binary search/bubble search? - which one to use
        #if it doesn't exist add it into housesVisited

#prints how many houses Santa has visited.
print('Santa has been to',len(santaHouse),'houses.')
