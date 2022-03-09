# Name: Matthew Powers
# This is my own work

def HALF_ADDER(i, j):
    c = 0 # carry in circut logic
    s = 0 # sum in circut logic
    if i and j: # and gate returns true then carry = 1
        c = 1
    if i != j: # exclusive or gate returns true then sum = 1
        s = 1
    return (s, c) # returns carry and sum values

def FULL_ADDER(i, j, k):
    c = 0 # carry in circut logic
    s = 0 # sum in circut logic

    if i != j: # exclusive or Gate returns true
        if k: # if 3rd input is true and so is the exclusive or then carry = 1
            c = 1
        else: # if 3rd input is False and the exclusive or is not then sum = 1
            s = 1 
    else: # exclusive or gate returns false
        if k: #if k is true and exclusive or gate is false then sum = 1
            s = 1
    
    if i and j: # and gate returns true then carry = 1
        c = 1

    return (s, c) # returns carry and sum values

def PARALLEL_ADDER(ABC, DEF):
    WXYZ = [0]*4 # creates empty array to store added binary digits
    addCarry = False # used to adda cary from prevous additon
    c = 0 # carry value
    s = 0 # sum value
    for number in range(-1,-4,-1): # starts at far right of array of binary int and goes left
        if addCarry: # if there was a previous carry then we must now add it to the two binary numbers meaning the full adder is now required, otherwise use half adder
            carrySum = FULL_ADDER(ABC[number], DEF[number], c)
            c = carrySum[1] # carry
            s = carrySum[0] # sum
        else:
            carrySum = HALF_ADDER(ABC[number], DEF[number])
            c = carrySum[1] # carry
            s = carrySum[0] # sum
        WXYZ[number] = s # adds sum value to new binary digit
        if c: # if there is a carry digit meaning when added it was 2 or 3 andnot 1 or 0
            if number == -3: #if at final for loop and thereis a carry it gets added here since there will not be another loop
                WXYZ[number-1] = c
            else:
                addCarry = True # sets addcary variable to true so it knows to add carry to next for loop
        else:
            addCarry = False #if there was no carry then it sets addcary to false so it kknows not to use full adder

    ### takes each number from WXYZ andsets them in wanted format for return ###
    W = WXYZ[0]
    X = WXYZ[1]
    Y = WXYZ[2]
    Z = WXYZ[3]
    ### takes each number from WXYZ andsets them in wanted format for return ###
    return(W, X, Y, Z) # returns an ordered 4-tuple



print("Half-adder")
print("i = 0  j = 0  |  c = " + str(HALF_ADDER(0,0)[1]) + "  s = " + str(HALF_ADDER(0,0)[0]))
print("i = 0  j = 1  |  c = " + str(HALF_ADDER(0,1)[1]) + "  s = " + str(HALF_ADDER(0,1)[0]))
print("i = 1  j = 0  |  c = " + str(HALF_ADDER(1,0)[1]) + "  s = " + str(HALF_ADDER(1,0)[0]))
print("i = 1  j = 1  |  c = " + str(HALF_ADDER(1,1)[1]) + "  s = " + str(HALF_ADDER(1,1)[0]))

print()
print("Full-adder")
print("i = 0  j = 0  k = 0  |  c = " + str(FULL_ADDER(0,0,0)[1]) + "  s = " + str(FULL_ADDER(0,0,0)[0]))
print("i = 0  j = 0  k = 1  |  c = " + str(FULL_ADDER(0,0,1)[1]) + "  s = " + str(FULL_ADDER(0,0,1)[0]))
print("i = 0  j = 1  k = 0  |  c = " + str(FULL_ADDER(0,1,0)[1]) + "  s = " + str(FULL_ADDER(0,1,0)[0]))
print("i = 0  j = 1  k = 1  |  c = " + str(FULL_ADDER(0,1,1)[1]) + "  s = " + str(FULL_ADDER(0,1,1)[0]))
print("i = 1  j = 0  k = 0  |  c = " + str(FULL_ADDER(1,0,0)[1]) + "  s = " + str(FULL_ADDER(1,0,0)[0]))
print("i = 1  j = 0  k = 1  |  c = " + str(FULL_ADDER(1,0,1)[1]) + "  s = " + str(FULL_ADDER(1,0,1)[0]))
print("i = 1  j = 1  k = 0  |  c = " + str(FULL_ADDER(1,1,0)[1]) + "  s = " + str(FULL_ADDER(1,1,0)[0]))
print("i = 1  j = 1  k = 1  |  c = " + str(FULL_ADDER(1,1,1)[1]) + "  s = " + str(FULL_ADDER(1,1,1)[0]))
print()
print("011 + 110 = " + str(PARALLEL_ADDER([0,1,1],[1,1,0])).replace(', ', '').replace('(', '').replace(')', ''))


