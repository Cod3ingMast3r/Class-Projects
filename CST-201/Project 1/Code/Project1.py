from copy import copy

class MyString:  
    def __init__(self, string = ''):
        self.string = string

        self.curr_length = self.length(string)

        self.myStringArray = [None]*self.curr_length
    
        for letterIndex in range(0, self.curr_length):
            self.myStringArray[letterIndex] = self.string[letterIndex]

    def length(self, word):
        return len(word)

    def __ensureCapacity(self, length):
        self.myStringArray = [None]*length

    def toString(self, array):
        string = ''
        for i in range(0, self.length(array)):
            string += array[i]
        return string

    def concat(self, newString):
        new_length = self.curr_length + self.length(newString)
        if new_length > self.curr_length:
            self.__ensureCapacity(new_length)
            
            for letterIndex in range(0, self.curr_length):
                self.myStringArray[letterIndex] = self.string[letterIndex]
            for letterIndex in range(self.curr_length, new_length):
                self.myStringArray[letterIndex] = newString[letterIndex-self.length(newString)-1]
            self.curr_length = new_length
            self.string = self.toString(self.myStringArray)
    
    def equals(self, word):
        if self.string == word:
            return True
        else:
            return False

    def compareTo(self, word):
        if self.string == word:
            return 0
        elif self.string > word:
            return -1
        elif self.string < word:
            return 1
    
    def get(self, int):
        if (abs(int) < self.curr_length):
            return self.myStringArray[int]
        else:
            return 'Int greater than size of string'

    def toUpper(self):
        return self.string.upper()


    def toLower(self):
        return self.string.lower()

    def substring(self, n, m = None):
        if m == None:
            return self.string[n:]
        else:
            return self.string[n:m]
    
    def indexOf(self, word):
        foundWord = False;
        while foundWord == False:
            innerLetter = 0
            for outerLetter in range(0, self.length(self.string)):
                if self.length(self.string) - outerLetter >= self.length(word)-innerLetter:
                
                    runAgain = True
                    while runAgain == True:
                        if word[innerLetter] == self.string[outerLetter]:
                            if innerLetter == self.length(word)-1:
                                return outerLetter - self.length(word)+1
                            else:
                                innerLetter += 1
                                runAgain = False
                        else:
                            if innerLetter == 0:
                                runAgain = False
                            else:
                                innerLetter = 0
                                runAgain = True
                else:
                    return -1
            foundWord = True
        return -1
                


    def lastIndexOf(self, word):
        foundWord = False;
        while foundWord == False:
            innerLetter = self.length(word)-1
            for outerLetter in range(self.length(self.string)-1,-1, -1):
                if self.length(self.string) - outerLetter >= self.length(word)-innerLetter:
                
                    runAgain = True
                    while runAgain == True:
                        if word[innerLetter] == self.string[outerLetter]:
                            if innerLetter == 0:
                                return outerLetter
                            else:
                                innerLetter -= 1
                                runAgain = False
                        else:
                            if innerLetter == self.length(word)-1:
                                runAgain = False
                            else:
                                innerLetter = self.length(word)-1
                                runAgain = True
                else:
                    return -1
            foundWord = True
        return -1
                

word = 'Hello '
array = []

FirstString = MyString(word)

#shallow Copy Constructor
SecondString = copy(FirstString)

#deep copy constructor
ThirdString = FirstString

print()
print('FirstString gets length of banana with length():')
print(FirstString.length('banana'))

print()
print('FirstString turns [w,w,w] to string with toString():')
print(FirstString.toString(['w','w','w']))

print()
print('Firstring prints the curr_length:')
print(FirstString.curr_length)

print()
FirstString.concat('Apple')
print('Firststring value after using concat and concatinating Apple to "Hello ":')

print()
print('FirstString .string value and length:')
print(FirstString.string)
print(FirstString.curr_length)

print()
print('SecondString .string value and length:')
print(SecondString.string)
print(SecondString.curr_length)

print()
print('ThirdString .string value and length:')
print(ThirdString.string)
print(ThirdString.curr_length)

print()
print('Comparing Second String "Hello " to "Hello ":')
print(SecondString.compareTo('Hello '))

print()
print('Comparing Second String "Hello " to "H\Aello ":')
print(SecondString.compareTo('Aello '))

print()
print('Getting Second String value at place 0:')
print(SecondString.get(0))

print()
print('Getting Second String value all lowercase:')
print(SecondString.toLower())

print()
print('Getting Second String value all uppercase:')
print(SecondString.toUpper())

print()
print('Getting Second String values starting at index 1 and ending at index 2 ([1:3]):')
print(SecondString.substring(1,3))

print()
print('Getting Second String index value of the first l:')
print(SecondString.indexOf('l'))

print()
print('Getting Second String index value of the last l:')
print(SecondString.lastIndexOf('l'))