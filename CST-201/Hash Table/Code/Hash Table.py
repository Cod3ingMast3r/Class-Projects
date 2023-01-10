import os
class Node:
    def __init__(self, dataVal = None):
        self.dataVal = dataVal;
        self.nextVal = None;
    
class LinkedList:
    def __init__(self):
        self.headVal = None;
        self.listSize = 0

    # O-n
    def Insert(self, newVal):
        if self.headVal == None:
            self.headVal = Node(newVal)
            self.listSize += 1;

        else:
            currentNode = self.headVal
            previousNode = currentNode
            foundPlacement = False
            while foundPlacement == False:
                if newVal == currentNode.dataVal:
                    break
                
                elif newVal < currentNode.dataVal:
                    if currentNode == self.headVal:
                        oldNode = self.headVal;
                        newNode = Node(newVal);
                        self.headVal = newNode;
                        self.headVal.nextVal = oldNode;
                        self.listSize += 1;
                    else:
                        oldNode = previousNode.nextVal;
                        newNode = Node(newVal);
                        previousNode.nextVal = newNode;
                        previousNode.nextVal.nextVal = oldNode
                        self.listSize += 1;
                    foundPlacement = True
                else:
                    if currentNode.nextVal == None:
                        currentNode.nextVal = Node(newVal)
                        self.listSize += 1;
                        foundPlacement = True
                    else:
                        previousNode = currentNode
                        currentNode = currentNode.nextVal;

    
    # O-n
    def displayList(self):
        currentNode = self.headVal
        listValues = ''
        while currentNode != None:
            if currentNode.nextVal != None:
                listValues += str(currentNode.dataVal) + ', '
            else:
                listValues += str(currentNode.dataVal)
            currentNode = currentNode.nextVal;
        return listValues
    
    # O-1 front
    def front(self):
        return str(self.headVal.dataVal);

    # O-1 front
    def pop_front(self):
        headVal = self.headVal.dataVal
        self.headVal = self.headVal.nextVal
        self.listSize -= 1
        return str(headVal);

    # O-n
    def back(self):
        currentNode = self.headVal
        while currentNode.nextVal != None:
            currentNode = currentNode.nextVal;
        return str(currentNode.dataVal)

    # O-n
    def pop_back(self):
        currentNode = self.headVal
        while currentNode.nextVal.nextVal != None:
            currentNode = currentNode.nextVal;
        backVal = currentNode.nextVal.dataVal
        currentNode.nextVal = None
        self.listSize -= 1
        return str(backVal)

    # O-1
    def empty(self):
        if self.headVal == None:
            return True
        else:
            return False

    # O-1
    def size(self):
        return self.listSize

    # O-2n
    def reverse(self):
        currentNode = self.headVal
        array = [None]*self.listSize
        i = 0
        while currentNode != None:
            array[i] = currentNode.dataVal
            currentNode = currentNode.nextVal
            i += 1
        array.reverse()
        for link in range(0,self.listSize):
            if link == 0:
                self.headVal = Node(array[link])
                currentVal = self.headVal
            else:
                currentVal.nextVal = Node(array[link])
                if link != self.listSize:
                    currentVal = currentVal.nextVal
        
    # O-1
    def clear(self):
        self.headVal = Node()
        self.listSize = 0





# best case - o(1)
# worst case - o(n)
def Hash(Array, value):
    mod = len(Array)

    totalValue = 0
    for letter in value:
        totalValue += ord(letter)
    
    place = totalValue % mod

    if Array[place] == None:
        Array[place] = LinkedList()
    Array[place].Insert(value)

# best case - o(1)
# worst case - o(n)
def Hash_Search(Array, value):
    mod = len(Array)

    totalValue = 0
    for letter in value:
        totalValue += ord(letter)
    
    place = totalValue % mod
    linkedListPosition = 0
    if Array[place] != None:
        if Array[place].headVal.dataVal != None:
            currentVal = Array[place].headVal
            while currentVal.dataVal != None:
                if currentVal.dataVal == value:
                    return "Array Position: " + str(place) + ", Linked List Position: " + str(linkedListPosition)
                else:
                    linkedListPosition += 1
                    currentVal = currentVal.nextVal
    

currentDirectory = os.getcwd() + '\Hash Table\Lists'

file1 = open(currentDirectory + '\List1.txt', 'r');

const = 53

list1 = [None]*const

for line in file1.readlines():
    for word in line.split(' '):
        word = word.replace('\n', '')
        Hash(list1, word)

for indx, place in enumerate(list1):
    if place != None:
        currentVal = place.headVal
        print(str(indx), end= ". ")
        while currentVal.nextVal != None:
            print('"' + str(currentVal.dataVal) + '"', end= ", ")
            currentVal = currentVal.nextVal
        print('"' + str(currentVal.dataVal) + '"')
    else:
        print(str(indx), end= ". ")
        print("None")

print(Hash_Search(list1, 'today'))