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
    print()
    print("Original Deck ...")
    print(deck, end='\n\n')
    firstDraw = randomDraw(deck.copy())
    secondDraw = randomDraw(deck.copy())
    print("After first draw...")
    print(firstDraw, end='\n\n')
    print("After second draw...")
    print(secondDraw, end='\n\n')
    
    fixedpoints = 0
    for i in range(0,n):
        if firstDraw[i] == secondDraw[i]:
            fixedpoints += 1
    print("There are " + str(fixedpoints) + " fixed ponts", end='\n\n')


fixedPoint(16)