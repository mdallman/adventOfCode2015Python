#############################
# Advent of Code 2015 Day 1 #
#     By Matt Dallman       #
#############################


#Initialise the string, floor and positional numbers
santasInstructions = input('Please enter the instructions for Sanata: ')
floor = 0
i = 0
basementEntered = False

while i < len(santasInstructions):
    #If ( go up one floor
    if santasInstructions[i] == '(':
        floor += 1
    #elif ) go down one floor
    elif santasInstructions[i] == ')':
        floor -= 1

    #Check to see if santa has entered the basement.
    if basementEntered == False and floor == -1:
        print('Santa has entered the basement for the first time.')
        print('He has followed',i+1,'instructions.')
        basementEntered  = not basementEntered

    #increment position in the string by 1
    i += 1
    

print('Santa is on floor',floor)
