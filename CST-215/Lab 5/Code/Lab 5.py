def getBits(numInput):
    count = 0 # initialization of count of bits
    finalNum = '' # final num as a string
    if numInput == 0:# if given number is 0 then there will be 0 bits so no need to go through while loop
        return (0, '0')
    while numInput !=1: # final number should always be a 1 since it is going to be continuously divided by 2
        end = numInput%2 # gets remainder when divided by two
        if end == 1: # if remainder is 1 then it adds it to the count
            count +=1
        finalNum = str(end) + finalNum #adds remainder to the beginning of the string whether it is a 0 or a 1
        numInput = numInput//2 # gets the new number whendivided by two without the remainder
        if numInput == 1: # if the final number is 1 then there is no more division by two and thus it is added to the count
            count+=1
    finalNum = str(numInput)+finalNum # adds the final digit tothe binary number
    return (count, finalNum) # returns count and binary number

print(getBits(10)) # runs getBits
print(format(10, 'b')) # combars format of getBits binary number to computer calculated one