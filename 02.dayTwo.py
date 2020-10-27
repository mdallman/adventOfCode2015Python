#############################
# Advent of Code 2015 Day 2 #
#     By Matt Dallman       #
#############################


#Given a present with sides l, w, h
#Part 1 - Find the amount of wrapping paper needed.

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


def calcRibbon(sizes):
    #Gets the length, height and width.
    sides = sizes.split('x')
    l = int(sides[0])
    w = int(sides[1])
    h = int(sides[2])

    faceLW = 2 * (l+w)
    faceLH = 2 * (l+h)
    faceWH = 2 * (w+h)
    volume = l * w * h

    smallPeri = faceLW
    if smallPeri > faceLH:
        smallPeri = faceLH

    if smallPeri > faceWH:
        smallPeri = faceWH

    ribbonRequired = volume + smallPeri
    return ribbonRequired
    

totalPaper = 0
totalRibbon = 0
f = open('dayTwoInput.txt   ',mode='r')
for x in f.readlines():
    totalPaper += calculateWrapping(x)
    totalRibbon += calcRibbon(x)
    
    
print('Total amount of wrapping paper required:',totalPaper)
print('Total amount of ribbon required:',totalRibbon)
