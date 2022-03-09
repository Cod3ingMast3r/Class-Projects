import os;

class Node:
    def __init__(self, dataVal = None):
        self.dataVal = dataVal;
        self.leftVal = None;
        self.rightVal = None;
        self.prevVal = None;
    
class LinkedList:
    def __init__(self):
        self.headVal = None;
        self.listSize = 0;
        self.reversed = False;

    # O-h
    def InsertOrderUnique(self, newVal):
        if self.headVal == None:
            self.headVal = Node(newVal)
            self.listSize += 1;

        else:
            currentNode = self.headVal
            foundPlacement = False
            while foundPlacement == False:
                if newVal < currentNode.dataVal:
                    if currentNode.leftVal == None:
                        currentNode.leftVal = Node(newVal)
                        currentNode.leftVal.prevVal = currentNode
                        self.listSize += 1;
                        foundPlacement = True
                    else:
                        currentNode = currentNode.leftVal
                elif newVal > currentNode.dataVal:
                    if currentNode.rightVal == None:
                        currentNode.rightVal = Node(newVal)
                        currentNode.rightVal.prevVal = currentNode
                        self.listSize += 1;
                        foundPlacement = True
                    else:
                        currentNode = currentNode.rightVal
                else:
                    print('Duplicate')
                    foundPlacement = True

    # # O-h
    def remove(self, newVal):
        currentNode = self.headVal
        while currentNode.dataVal != newVal:
            if newVal < currentNode.dataVal:
                currentNode = currentNode.leftVal
            elif newVal > currentNode.dataVal:
                currentNode = currentNode.rightVal
            else:
                print("Error Somewhere")
            
            if currentNode == None:
                print("Doesnt Exist")
                return None
        newVal = currentNode
        print(newVal.dataVal)

        if currentNode.leftVal != None:
            currentNode = currentNode.leftVal
            while currentNode.rightVal != None:
                currentNode = currentNode.rightVal
            currentNode.prevVal.rightVal = currentNode.leftVal
            replacementNode = currentNode

        elif currentNode.rightVal != None:
            currentNode = currentNode.rightVal
            while currentNode.leftVal != None:
                currentNode = currentNode.leftVal
            currentNode.prevVal.leftVal = currentNode.rightVal
            replacementNode = currentNode

        else:
            if currentNode != self.headVal:
                replacementNode = None
            else:
                self.headVal = None
                replacementNode = None

        if newVal != self.headVal:
            if newVal.prevVal.leftVal == newVal:
                newVal.prevVal.leftVal.dataVal = replacementNode.dataVal
            elif newVal.prevVal.rightVal == newVal:
                newVal.prevVal.rightVal.dataVal = replacementNode.dataVal
        else:
            self.headVal.dataVal = replacementNode.dataVal
        self.listSize -= 1

    # O-h
    def search(self, newVal):
            currentNode = self.headVal
            distanceFromHead = 0
            while currentNode.dataVal != newVal:
                if newVal < currentNode.dataVal:
                    currentNode = currentNode.leftVal
                elif newVal > currentNode.dataVal:
                    currentNode = currentNode.rightVal
                else:
                    print("Error Somewhere")
                distanceFromHead += 1
                
                if currentNode == None:
                    print("Doesnt Exist")
                    return None
            newVal = currentNode
            print(newVal.dataVal)
            print("Distance From Head: " + str(distanceFromHead))

    #O-n
    ### used to determine if each node follows the next ###
    def displayList(self):
        currentNode = self.headVal
        oldNodes = [currentNode]
        lines = []
        foundAllNodes = False
        while foundAllNodes == False:
            newNodes = []
            newNodesText = []
            for nodeIndx, node in enumerate(oldNodes):
                if node != None:
                    newNodesText.append(node.dataVal)
                    if node.leftVal != None:
                        newNodes.append(node.leftVal)
                    else:
                        newNodes.append(None)
                    if node.rightVal != None:
                        newNodes.append(node.rightVal)
                    else:
                        newNodes.append(None)
                else:
                    newNodes.append(None)
                    newNodes.append(None)
                    newNodesText.append("    ")

            lines.append(newNodesText)
            oldNodes = newNodes
            if [None]*len(newNodes) == newNodes:
                foundAllNodes = True
        
        ## largest is equal to 2 to power of line number
        for lineIndx, line in enumerate(lines):
            spacesNeeded = int(2**(len(lines)-2)) - int(len(line))
            print(spacesNeeded)
            neatLine = ' '*(spacesNeeded-(lineIndx+2)*(len(line)-2))
            for wordIndx, word in enumerate(line):
                if word == (None or "    "):
                    word = '_'
                neatLine = neatLine + " "*(lineIndx+2) + str(word)

            print(neatLine)

    def size(self):
        return self.listSize

    # O-1
    def clear(self):
        self.headVal = Node()
        self.listSize = 0

    # O-n
    def cleanUp(self, stringVal):
        stringVal = stringVal.lower()
        newString = ''
        for letter in stringVal:
            if letter.isalpha():
                newString += letter
        return newString

def split(word):
    return [char for char in word]

list1 = LinkedList()

# list2 = LinkedList()

currentDirectory = os.getcwd() + '\Binary Search Tree\Lists'

file1 = open(currentDirectory + '\List1.txt', 'r');

# file2 = open(currentDirectory + '\List2.txt', 'r');

for line in file1.readlines():
    for word in line.split(' '):
        word = word.replace('\n', '')
        word = list1.cleanUp(word)
        list1.InsertOrderUnique(word)

print('Doubly Linked List1 before removal: ')
list1.displayList()
print()
list1.search('if')
print()
list1.remove('how')
print('Doubly Linked List1 after removal: ')
list1.displayList()
print()
list1.search('if')