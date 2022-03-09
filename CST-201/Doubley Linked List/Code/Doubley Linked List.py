# use insert order unique and popule list and use clean up to ensure no letters are passd through
# do this for list 1 and 2 and then merge them and ensure that it returns new list and list 1 and 2 are both wiped clean after
import os;
from copy import copy


class Node:
    def __init__(self, dataVal = None):
        self.dataVal = dataVal;
        self.nextVal = None;
        self.prevVal = None;
    
class LinkedList:
    def __init__(self):
        self.headVal = None;
        self.listSize = 0;
        self.reversed = False;

    # O-n
    def InsertOrder(self, newVal):
        reversedAtStart = False
        if self.reversed == True:
            reversedAtStart = True
            self.reverse()

        if self.headVal == None:
            self.headVal = Node(newVal)
            self.listSize += 1;

        else:
            currentNode = self.headVal
            previousNode = currentNode
            foundPlacement = False
            while foundPlacement == False:
                
                if newVal < currentNode.dataVal:
                    if currentNode == self.headVal:
                        oldNode = self.headVal;
                        newNode = Node(newVal);
                        self.headVal = newNode;
                        self.headVal.prevVal = None
                        self.headVal.nextVal = oldNode;
                        self.headVal.nextVal.prevVal = self.headVal
                        self.listSize += 1;
                    else:
                        oldNode = previousNode.nextVal;
                        newNode = Node(newVal);
                        previousNode.nextVal = newNode;
                        previousNode.nextVal.prevVal = previousNode
                        previousNode.nextVal.nextVal = oldNode
                        previousNode.nextVal.nextVal.prevVal = previousNode.nextVal
                        self.listSize += 1;
                    foundPlacement = True
                else:
                    if currentNode.nextVal == None:
                        currentNode.nextVal = Node(newVal)
                        currentNode.nextVal.prevVal = currentNode.prevVal
                        self.listSize += 1;
                        foundPlacement = True
                    else:
                        previousNode = currentNode
                        currentNode = currentNode.nextVal;
            # currentNode.nextVal = Node(newVal);
            if reversedAtStart == True:
                self.reverse()
    
    # O-n
    def InsertOrderUnique(self, newVal):
        reversedAtStart = False
        if self.reversed == True:
            reversedAtStart = True
            self.reverse()

        if self.headVal == None:
            self.headVal = Node(newVal)
            self.listSize += 1;

        else:
            currentNode = self.headVal
            previousNode = currentNode
            foundPlacement = False
            while foundPlacement == False:
                
                if newVal < currentNode.dataVal:
                    if currentNode == self.headVal:
                        oldNode = self.headVal;
                        newNode = Node(newVal);
                        self.headVal = newNode;
                        self.headVal.prevVal = None
                        self.headVal.nextVal = oldNode;
                        self.headVal.nextVal.prevVal = self.headVal
                        self.listSize += 1;
                    else:
                        oldNode = previousNode.nextVal;
                        newNode = Node(newVal);
                        previousNode.nextVal = newNode;
                        previousNode.nextVal.prevVal = previousNode
                        previousNode.nextVal.nextVal = oldNode
                        previousNode.nextVal.nextVal.prevVal = previousNode.nextVal
                        self.listSize += 1;
                    foundPlacement = True
                elif newVal == currentNode.dataVal:
                    foundPlacement = True;
                else:
                    if currentNode.nextVal == None:
                        currentNode.nextVal = Node(newVal)
                        currentNode.nextVal.prevVal = currentNode.prevVal
                        self.listSize += 1;
                        foundPlacement = True
                    else:
                        previousNode = currentNode
                        currentNode = currentNode.nextVal;
            # currentNode.nextVal = Node(newVal);
            if reversedAtStart == True:
                self.reverse()


    # O-n
    def remove(self, newVal):
        currentNode = self.headVal
        while (currentNode.nextVal.nextVal != None) and (newVal != currentNode.dataVal):
            currentNode = currentNode.nextVal;
        if newVal == currentNode.dataVal:
            if currentNode == self.headVal:
                self.headVal = currentNode.nextVal
            if currentNode.prevVal != None:
                currentNode.prevVal.nextVal = currentNode.nextVal
            if currentNode.nextVal != None:   
                currentNode.nextVal.prevVal = currentNode.prevVal
            self.listSize -= 1


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
        print(self.reversed)
        return listValues

    #O-n
    ### used to determine if each node follows the next ###
    def displayList2(self):
        currentNode = self.headVal
        listValues = ''
        while currentNode != None:
            print()
            if currentNode.prevVal != None:
                print("Previous Value: " + str(currentNode.prevVal.dataVal))
            if currentNode != None:
                print("Curent Value: " + str(currentNode.dataVal))
            if currentNode.nextVal != None:
                print("Next Value: " + str(currentNode.nextVal.dataVal))
            print()
            currentNode = currentNode.nextVal;
    
    # O-1 front
    def front(self):
        return str(self.headVal.dataVal);

    # O-1 front
    def pop_front(self):
        headVal = self.headVal.dataVal
        self.headVal = self.headVal.nextVal
        self.headVal.prevVal = None
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

    # O-n
    def reverse(self):
        if self.reversed == False:
            self.reversed = True
        else:
            self.reversed = False
        currentNode = self.headVal
        for link in range(0,self.listSize):
            if link == 0:
                oldNode = currentNode.nextVal
                newNode = None
                currentNode.prevVal = oldNode
                currentNode.nextVal = newNode
                currentNode = currentNode.prevVal
            else:
                oldNode = currentNode.nextVal
                newNode = currentNode.prevVal
                currentNode.prevVal = oldNode
                currentNode.nextVal = newNode
                if link != self.listSize - 1:
                    currentNode = currentNode.prevVal
                    self.headVal = currentNode

        

    # O-n
    def merge(self, linkedList):
        newList = copy(self)
        currentNode = linkedList.headVal
        while currentNode != None:
            newList.InsertOrderUnique(currentNode.dataVal)
            currentNode = currentNode.nextVal;
        self.clear()
        linkedList.clear()
        return newList

    # O-n
    def cleanUp(self, stringVal):
        stringVal = stringVal.lower()
        newString = ''
        for letter in stringVal:
            if letter.isalpha():
                newString += letter
        return newString
    
    # O-1
    def clear(self):
        self.headVal = Node()
        self.listSize = 0
        
        


list1 = LinkedList()

list2 = LinkedList()

currentDirectory = os.getcwd() + '\Doubley Linked List\Lists'

file1 = open(currentDirectory + '\List1.txt', 'r');

file2 = open(currentDirectory + '\List2.txt', 'r');

for line in file1.readlines():
    for word in line.split(' '):
        word = word.replace('\n', '')
        word = list1.cleanUp(word)
        list1.InsertOrderUnique(word)

for line in file2.readlines():
    for word in line.split(' '):
        word = word.replace('\n', '')
        word = list2.cleanUp(word)
        list2.InsertOrderUnique(word)

print('Doubly Linked List1 all before merge: ' + list1.displayList())
print('Doubly Linked List2 all before merge: ' + list2.displayList())

list3 = list1.merge(list2)

print('Doubly Linked List1 all after merge: ' + list1.displayList())
print('Doubly Linked List2 all after merge: ' + list2.displayList())
print('Doubly Linked List3 all uique combined: ' + list3.displayList())