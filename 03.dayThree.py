########################
# Advent of Code Day 3 #
#  By Matt Dallman     #
########################

#Initialise Variables
xSanta = 0
ySanta = 0
santaPosition = [xSanta,ySanta]


def movement(direction):
    global xSanta
    global ySanta

    if direction == 'v':
        ySanta -= 1
    elif direction == '^':
        ySanta += 1
    elif direction == '>':
        xSanta += 1
    elif direction == '<':
        xSanta -= 1
