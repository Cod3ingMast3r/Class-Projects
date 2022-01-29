import os;

currentDirectory = os.getcwd() + '\Project0'

file = open(currentDirectory + '\Words.txt', 'r');


wordArray = []

for line in file.readlines():
    for word in line.split(' '):
        word = word.replace('\n', '')
        print(word)
        wordArray.append(word)

print('Unsorted List: ' + str(wordArray))
wordArray.append('garbage')

wordIndex = 0
while wordIndex < len(wordArray):
    if wordIndex < len(wordArray)-1:
        wordIndexChanged = False
        if wordArray[wordIndex].lower() > wordArray[wordIndex + 1].lower():
            oldWord = wordArray[wordIndex]
            newWord = wordArray[wordIndex + 1]
            wordArray[wordIndex] = newWord
            wordArray[wordIndex + 1] = oldWord
            if wordIndex !=0:
                wordIndex -= 1
                wordIndexChanged = True
        else:
            wordIndex += 1
            wordIndexChanged = True
    else:
        break
        

print("Sorted List: "+ str(wordArray))
stillSearching = True
foundWord = False
while stillSearching == True:
    name = input("Type a word to search to find Index: ")
    currentSearchIndex = int(len(wordArray)/2)
    while (currentSearchIndex >= 0) and (currentSearchIndex < len(wordArray)):
        if name.lower() == wordArray[currentSearchIndex].lower():
            print('This word was first found at index: ' + str(currentSearchIndex))
            foundWord = True
            break
        else:
            if name.lower() < wordArray[currentSearchIndex+1].lower():
                currentSearchIndex -= 1
            else:
                currentSearchIndex += 1

    if foundWord == False:
        print('Word Not found')        
    print('Want to search Again?')
    Searchinput = input('(y/n)')
    if Searchinput == 'n':
        stillSearching = False




















# words = []


###Great Sort for as array is created###
# for line in file.readlines():
#     for word in line.split(' '):
#         if len(words) != 0:
#             placed = False
#             for wordsIndex in range(0,len(words)):
#                 if placed == False:
#                     for letter in range(0,len(word)):
#                         if letter < len(words[wordsIndex]):
#                             lowerCaseNewLetter = word[letter].lower()
#                             print('lowerCaseNewLetter: ' + lowerCaseNewLetter + ' ' + str(ord(lowerCaseNewLetter)))
#                             lowerCaseOldLetter = words[wordsIndex][letter].lower()
#                             print('lowerCaseOldLetter: ' + lowerCaseOldLetter + ' ' + str(ord(lowerCaseOldLetter)))
#                             print(word[letter])
#                             print(words[wordsIndex][letter])
#                             if ord(lowerCaseNewLetter) < ord(lowerCaseOldLetter):
#                                 print('lower in alphabet')
#                                 print(wordsIndex)
#                                 print(len(words)-1)
#                                 words.insert(wordsIndex, word)
#                                 print(words)
#                                 placed = True
#                                 break
#                             elif ord(lowerCaseNewLetter) > ord(lowerCaseOldLetter):
#                                 print('higher in alpohabet')
#                                 if wordsIndex == len(words)-1:
#                                     words.insert(wordsIndex+1, word)
#                                     print(words)
#                                     placed = True
#                                     break
#                                 else:
#                                     break
#                             else:
#                                 print('matched')
#                                 continue
#                         else:
#                             words = [word] + words
#                             placed = True
#                             break
#                 else:
#                     print('PLACED')
#                     break
#         else:
#             words.append(word)
# print(words)