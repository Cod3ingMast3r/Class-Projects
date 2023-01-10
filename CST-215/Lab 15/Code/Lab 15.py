import random

def arrayCreation(n):
    array = []
    for i in range(0,n):
        array.append(i+1)
    return array

def randomDraw(array):
    deck_array = array
    newDrawnDeck = []
    while len(deck_array) != 0:
        selection = random.randint(0,len(deck_array)-1)
        newDrawnDeck.append(deck_array[selection])
        deck_array.pop(selection)
    return newDrawnDeck

def fixedPoint(n):
    deck = arrayCreation(n)
    firstDraw = randomDraw(deck.copy())
    secondDraw = randomDraw(deck.copy())

    fixedpoints = 0
    for i in range(0,n):
        if firstDraw[i] == secondDraw[i]:
            fixedpoints += 1
    # print("There are " + str(fixedpoints) + " fixed ponts", end='\n\n')
    return fixedpoints

def massFixedPoints(numOfCards, numOfTimes):
    #creates array of possible fixed points 
    #(is same size as amount of cards since each one would be one plus an additional slot to account for 0 matches)
    fixedPointOccurances = [0]*(numOfCards+1)
    for i in range(0,numOfTimes):
        fixedpoints = fixedPoint(numOfCards)
        fixedPointOccurances[fixedpoints] += 1
    print("Deck of " + str(numOfCards) + " cards..." + str(numOfTimes) + " different card selections")
    print("Fixed Pts    Percentage")
    print("-----------------------")
    for i in range(0,len(fixedPointOccurances)):
        precentage = fixedPointOccurances[i]/numOfTimes
        print(str(i) + "            " + str(precentage))
print()
massFixedPoints(10,1000)
