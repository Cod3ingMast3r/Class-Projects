import random;

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

for i in range(0,100): # do this 100 times
    ### create two random numbers ###
    num1 = random.randint(1, 9999999)
    num2 = random.randint(1, 9999999)
    ### create two random numbers ###

    ### create the neat print format for both numbers and the GCD ###
    whitespace = 7 - len(str(num1))
    num1String = " "*whitespace + str(num1)
    whitespace = 7 - len(str(num2))
    num2String = " "*whitespace + str(num2)
    Greatest_Common_Denominator = GCD(num1,num2)
    whitespace = 7 - len(str(GCD))
    GCD_String = " "*whitespace + str(Greatest_Common_Denominator)
    print("     " + num1String + "     " + num2String + "     " + GCD_String)
    ### create the neat print format for both numbers and the GCD ###