########################
# Advent of Code Day 3 #
#  By Matt Dallman     #
########################

#Initialise Variables
xSanta = 0
ySanta = 0
santaPosition = [xSanta,ySanta]
santaHouse = [[0,0]]
santaInstructions = input('Please enter the instructions for Santa to follow: ')

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
    housePreviouslyVisited = False
    
    for house in santaHouse:
    #check if santaPosition exists in housesVisited
        if santaPosition == house:
            housePreviouslyVisited = True
                
    if housePreviouslyVisited == False:
        santaHouse.append(santaPosition)    
for x in santaInstructions:
    movement(x)
    checkHouse(santaPosition)
    
#prints how many houses Santa has visited.
print('Santa has been to',len(santaHouse),'houses.')
