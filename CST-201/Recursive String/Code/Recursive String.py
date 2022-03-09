slips = ["DFG", "EFG", "DFFFFFG", "DFDFDFDFG", "DFEFFFFFG"]
notSlips = ["DFEFF", "EFAHG", "DEFG", "DG", "EFFFFDG", "DFFFGE"]

slaps = ["AH", "ABAHC", "ABABAHCC", "ADFGC", "ADFFFFGC", "ABAEFGCC", "ADFDFGC"]
notSlaps = ["ABC", "ABAH", "DFGC", "ABABAHC", "SLAP", "ADGC"]

slops =["AHDFG", "ADFGCDFFFFFG", "ABAEFGCCDFEFFFFFG"]
notSlops = ["AHDFGA", "DFGAH", "ABABCC"]

#O(n)
def Slip(word): # can only have letters d e f g
    for letterIndx, letter in enumerate(word):
        F_exists = False
        
        if letter not in "DEFG":
            return "Not A Slip"

        if letter == "D" or letter == "E":
            if letterIndx != len(word)-1:
                nextLetterIndx = letterIndx + 1
            else:
                return "Not A Slip"
            while word[nextLetterIndx] == "F":
                F_exists = True
                if nextLetterIndx == len(word)-1:
                    return "Not A Slip"
                else:
                    nextLetterIndx += 1
            if F_exists == False:
                return "Not A Slip"
            elif (nextLetterIndx == len(word)-1) and (word[len(word)-1] == "G"):
                return "Slip"
            else:
                return Slip(word[nextLetterIndx:])
        elif len(word) < 3:
            return "Not A Slip"
        else:
            return Slip(word[letterIndx+1:])

#O(n)
def Slap(word):
    for letterIndx, letter in enumerate(word):
        if len(word) <= 1:
            return "Not A Slap"
        if letter == 'A':
            nextLetterIndx = letterIndx + 1
            letter = word[nextLetterIndx]
            if len(word) == 2:
                if letter == 'H':
                    return "Slap"
                else:
                    return "Not A Slap"
            
            elif letter in "DEFG":
                if Slip(word[nextLetterIndx:len(word)-1]) == "Slip":
                    if word[len(word)-1:] == 'C':
                        return "Slap"
                    else:
                        return "Not A Slap"
            elif letter == 'B':
                if Slap(word[nextLetterIndx+1:len(word)-1]) == "Slap":
                    if word[len(word)-1:] == "C":
                        return "Slap"
                    else:
                        return "Not A Slap"
            else:
                return "Not A Slap"
        else:
            return "Not A Slap"

#O(n)
def Slop(word):
    for letterIndx, letter in enumerate(word):
        if Slap(word[:letterIndx]) == "Slap":
            if Slip(word[letterIndx:]) == "Slip":
                return "Slop"
            else:
                return "Not A Slop"
        else: continue
    return "Not A Slop"

print()
print('Not Slips:')
for word in notSlips:
    print(word + ": ", end='')
    answer = Slip(word)
    print(answer)
print()
print('Slips:')
for word in slips:
    print(word + ": ", end='')
    answer = Slip(word)
    print(answer)

print()
print('Not Slaps:')
for word in notSlaps:
    print(word + ": ", end='')
    answer = Slap(word)
    print(answer)
print()
print('Slaps:')
for word in slaps:
    print(word + ": ", end='')
    answer = Slap(word)
    print(answer)

print()
print('Not Slops:')
for word in notSlops:
    print(word + ": ", end='')
    answer = Slop(word)
    print(answer)
print()
print('Slops:')
for word in slops:
    print(word + ": ", end='')
    answer = Slop(word)
    print(answer)
print()