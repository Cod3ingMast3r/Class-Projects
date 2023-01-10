# Matthew Powers
# This is my own work

import random

# If it returns a 1 then a number is relatively prime (already previously explaine in lab 6)
def GCD(num1, num2):
    if num1 >= num2: # always makes sure that the larger number is being divided by the smaller
        largeNum = num1
        smallNum = num2
    else:
        largeNum = num2
        smallNum = num1
    
    GCD = smallNum # sets the GCD as the smaler number because if it divides evenly then this would be correct, otherwise this is updated in the future
    remainder = largeNum%smallNum # gets the first remainder
    divisor = smallNum #establishes small num as the next divisor

    while remainder != 0:
        GCD = remainder # establishes the GCD as the remainder in case it ends up being the one that divides to 0
        oldremainder = remainder # establishes an old remainder since this will be the new divisor after a new remander is collected
        remainder = divisor%oldremainder # gets a new remainder and if it is not 0 it continues
        divisor = oldremainder #establishes the divisor as the old remander
    return GCD

# linear Diophantine equation
def LDE(a, b):
    # ensures that the GCD is 1 and if it is not it doesnt need to do this
    if GCD(a,b) == 1:
        ### ensures that larger number is being dived by smaller ###
        if a > b:
            largeNum = a
            smallNum = b
            
        else:
            largeNum = b
            smallNum = a
            flipReturn = True
        ### ensures that larger number is being dived by smaller ###

        ### creates a list of numbers from euclidian algorithm (where large is divided by smaller and smaller is dividedby remainder until remainder =0) ###
        remainder = None
        divided = []
        while remainder != 0:
            divided.insert(0, largeNum)
            remainder = largeNum%smallNum
            # the small num divisor is now the next large num to getr divided
            largeNum = smallNum
            # the remeinder isnow the next divisor
            smallNum = remainder
        divided.insert(0, 1)
        ### creates a list of numbers from euclidian algorithm (where large is divided by smaller and smaller is dividedby remainder until remainder =0) ###

        ### Takes list generated above and pices it back togehter using the Diophantine Equation thus working backwardsstarting with GCF (greatest common factor) ###
        #stores numbers that are multiplies to get ax + by = 1 (they are the x and y)
        prevFirstMultiple = 0
        prevSecondMultiple = 0

        # does the diophantine equation discussed in powerpoint for lab 8
        for numIndx in range(0,len(divided)-2):
            secondMultiple = 1
            desiredResult = divided[numIndx]
            result = 0
            while result != desiredResult:
                # combines numbers until their sum is the number before them two in the list i.e [1,4,5] sum of 4 and 5 to get 1
                result = divided[numIndx + 2] - divided[numIndx + 1]*secondMultiple
                if result > desiredResult:
                    secondMultiple += 1
                else:
                    if numIndx%2 != 0:
                        if prevSecondMultiple != 0:
                            prevFirstMultiple += secondMultiple*prevSecondMultiple
                        else:
                            prevFirstMultiple += secondMultiple
                    else:
                        if numIndx == 0:
                            prevFirstMultiple += 1
                            prevSecondMultiple += secondMultiple
                        else:
                            prevSecondMultiple += secondMultiple*prevFirstMultiple
        ### Takes list generated above and pices it back togehter using the Diophantine Equation thus working backwardsstarting with GCF (greatest common factor) ###
        # since the smaller sumber is always subtracted ultimately, making it negative in a ax + by = 1 equation
        prevSecondMultiple = -prevSecondMultiple

        #ensures that each number is getting multiplied by the correct number
        if a*prevFirstMultiple + b*prevSecondMultiple == 1:
            aMultiple = prevFirstMultiple
            bMultiple = prevSecondMultiple
        else:
            aMultiple = prevSecondMultiple
            bMultiple = prevFirstMultiple

        equation = str(a) +"*(" + str(aMultiple) + ")+" + str(b) + "*(" + str(bMultiple) + ")=1"
    else:
        equation = ""
    line =  str(a).rjust(5) + "\t" + str(b).rjust(5) + "     " + str(GCD(a,b)) + "\t" + str(equation).rjust(22)
    print(line)

print()
print()
for i in range(0,10): # do this 100 times
    ### create two random numbers ###
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    ### create two random numbers ###
    LDE(num1, num2)
# LDE(491, 599)
# LDE(501, 896)
# LDE(280, 5)
# LDE(958, 933)
# LDE(467, 652)
# LDE(274, 584)
# LDE(154, 179)
# LDE(501, 562)
# LDE(496, 33)
print()
print()
