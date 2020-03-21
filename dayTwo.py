########################
# Advent of Code Day 2 #
#  By Matt Dallman     #
########################


#Given a present with sides l, w, h
#Part 1 - Find the amount of wrapping paper needed.

#calculates the amount of wrapping paper per present.
def calculateWrapping(sizes):
    #This function calculates the armount of paper needed for one present.
    #Get the length of the sides from string
    sides = sizes.split('x')
    l = int(sides[0])
    w = int(sides[1])
    h = int(sides[2])

    #Checks that input string has been entered correctly.
    #print('Length =',l,'Width =',w,'Height =',h)

    #Calculate the area of each side.
    lw = l * w
    lh = l * h
    wh = w * h

    #Calculate the smallest side
    smallestSide = lw
    if smallestSide > lh:
        smallestSide = lh
        
    if smallestSide > wh:
        smallestSide = wh

    #Calculates the amount of paper needed
    paperNeeded = (2 * lw) + (2 * lh) + (2 * wh) + smallestSide
    return paperNeeded

totalPaper = 0
f = open('dayTwoInput.txt   ',mode='r')
for x in f.readlines():
    totalPaper += calculateWrapping(x)
    
<<<<<<< HEAD
print(totalPaper)
=======
#takes the list and iterates using calculateWrapping
def allWrapping():
    totalPaper = 0
    #f = open("dayTwoTest.txt", "r") #uses the test file
    f = open("dayTwoInput.txt", "r") #The project input file
    for line in f:
        totalPaper += calculateWrapping(line)

    return totalPaper

print("The total amount of wrapping paper needed is:", allWrapping())
>>>>>>> caf980b28bd6828499e673d7598fca503d104d48
