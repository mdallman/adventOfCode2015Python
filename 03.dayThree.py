#############################
# Advent of Code 2015 Day 3 #
#     By Matt Dallman       #
#############################

#TODO write santa class for a more streamlined code.

#Initialise Variables
xSanta = 0
ySanta = 0
santaPosition = [xSanta,ySanta]

xRobo = 0
yRobo = 0
roboPosition = [xRobo,yRobo]

santaTurn = 's'

housesVisited = [[0,0]]
santaInstructions = input('Please enter the instructions for Santa to follow: ')

def movement(direction):
    #Declare variables
    global xSanta
    global ySanta
    global santaPosition

    global xRobo
    global yRobo
    global roboPosition

    global santaTurn
    
    #Reads instructions and moves santa based on them
    if santaTurn == 's':
        if direction == 'v':
            ySanta -= 1
        elif direction == '^':
            ySanta += 1
        elif direction == '>':
            xSanta += 1
        elif direction == '<':
            xSanta -= 1
    elif santaTurn == 'r':
        if direction == 'v':
            yRobo -= 1
        elif direction == '^':
            yRobo += 1
        elif direction == '>':
            xRobo += 1
        elif direction == '<':
            xRobo -= 1

    santaPosition = [xSanta,ySanta]
    roboPosition = [xRobo,yRobo]

def checkHouse():
    global santaPosition
    global roboPosition
    global housesVisited
    global santaTurn
    housePreviouslyVisited = False
    
    for house in housesVisited:
    #check if santaPosition exists in housesVisited


        if santaTurn == 's':
            if santaPosition == house:
                housePreviouslyVisited = True

        if santaTurn == 'r':
            if roboPosition == house:
                housePreviouslyVisited = True
            
    if housePreviouslyVisited == False:
        if santaTurn == 's':
            housesVisited.append(santaPosition)

        if santaTurn == 'r':
            housesVisited.append(roboPosition)

def changeSanta():
    global santaTurn
    if santaTurn == 's':
        santaTurn = 'r'
    elif santaTurn == 'r':
        santaTurn = 's'
    
for x in santaInstructions:
    movement(x)
    checkHouse()
    changeSanta()

#prints how many houses Santa has visited.
print('Santa has been to',len(housesVisited),'houses.')
