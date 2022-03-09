fTerm = int(input("Enter the first term of your sequence: "))
cDiff = int(input("Enter the common difference between terms: "))
seqLen = int(input("Enter the length of your sequence:"))

# stores sequence
seq = str(fTerm) + ', '

# loops through adding incrimented numbers to arithmatic sequence
for i in range(0,seqLen-1):
    fTerm += cDiff
    if i != seqLen-2:
        seq += str(fTerm) + ', '
    else:
        seq += str(fTerm) 

print("Here is your Arithmatic Sequence: " + seq)