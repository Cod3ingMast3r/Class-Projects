import random
import math
import itertools

def main():
    ### uses random int set to establish a set of random numbers between a min max as well as the number of random numbers in a set ###
    print()
    set1 = RandomIntSet(0, 100, 3)
    print("Set 1: " + str(set1))
    set2 = RandomIntSet(0, 100, 3)
    print("Set 2: " + str(set2))
    set3 = RandomIntSet(0, 100, 3)
    print("Set 3: " + str(set3))
    print()
    ### uses random int set to establish a set of random numbers between a min max as well as the number of random numbers in a set ###
    
    programedCartesian = set(itertools.product(set1,set2,set3))
    print("Computer calculated Cartesian: " + str(programedCartesian))
    print("Number of sets in calculated cartesian: " + str(len(programedCartesian)) + '\n')

    myCartesian = ConvertSettoCartesian(set1, set2, set3)
    print("My Cartesian: " + str(myCartesian))
    print("Number of sets in my  cartesian: " + str(len(myCartesian)) + '\n')

    if myCartesian == programedCartesian:
        print('They match :)')
    else:
        print('They dont :(')


def ConvertSettoCartesian(set1, set2, set3):
    #loops through changing one number in a set at a time until all possible combinations have been added
    cartesianSet = set()
    for number1 in set1:
        for number2 in set2:
            for number3 in set3:
                cartesianSet.add((number1, number2, number3))
    return cartesianSet


def RandomIntSet(min, max, size):
    # this stops a infinite whule loop of getting a new random int because if you are requesting more random ints than are available it will keep looking for a new one
    if abs((max-min)) >= size-1:
        randomSet = set()
        # loops through to create number of decified random ints in size variable given
        for number in range(0,size):
            #establishes random int
            randomInt = random.randint(min,max)
            #if the random int is inside of the set of random ints then it will get a new random int until it is not
            while randomInt in randomSet:
                #establishes new random int if above condition is met
                randomInt = random.randint(min,max)
            #adds random int
            randomSet.add(randomInt)
        #returns the set of random int
        return randomSet

    else:
        return "Range of max and min was less than size given"

main()