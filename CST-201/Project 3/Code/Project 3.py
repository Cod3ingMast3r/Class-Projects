# use insert order unique and popule list and use clean up to ensure no letters are passd through
# do this for list 1 and 2 and then merge them and ensure that it returns new list and list 1 and 2 are both wiped clean after


class Node:
    def __init__(self, dataVal = None):
        self.dataVal = dataVal;
        self.nextVal = None;
        self.prevVal = None;
    

# class Node_Head:
#     def __init__(self):
#         self.headVal = None;
    

class LinkedList:
    def __init__(self):
        self.headVal = None;
        self.listSize = 0;
        self.reversed = False;

    # def Head(self, headVal = None):
    #     self.headVal = headVal;

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

        

    # O-2n
    def merge(self, linkedList):
        currentNode = linkedList.headVal
        while currentNode != None:
            self.InsertOrder(currentNode.dataVal)
            currentNode = currentNode.nextVal;
    # O-n
    def cleanUp(self, stringVal):
        stringVal = stringVal.lower()
        newString = ''
        for letter in stringVal:
            if letter.isalpha():
                newString += letter
        print(newString)
        
        


list = LinkedList()

print('Doubly Linked List empty(): ' + str(list.empty()))
print('Doubly Linked List all: ' + list.displayList())

list.InsertOrder(33)
list.InsertOrder(44)
list.InsertOrder(22)
list.InsertOrder(100)
list.InsertOrder(37)
list.InsertOrder(49)
list.InsertOrder(1)
list.InsertOrder(9)

print('Doubly Linked List all: ' + list.displayList())

print('Doubly Linked List front(): ' + list.front())

print('Doubly Linked List back(): ' + list.back())

print('Doubly Linked List pop_back() value: ' + list.pop_back())

print('Doubly Linked List all: ' + list.displayList())

print('Doubly Linked List pop_front() value: ' + list.pop_front())

print('Doubly Linked List all: ' + list.displayList())

print('Doubly Linked List size(): ' + str(list.size()))

list2 = LinkedList()

list2.InsertOrder(39)
list2.InsertOrder(17)
list2.InsertOrder(13)
list2.InsertOrder(45)

print('Doubly Linked List merge(): ' + 'merged')
list.merge(list2)
print('Doubly Linked List all: ' + list.displayList())

### used to determine if each node follows the next ###
# print('Doubly Linked List all front and back vals: ')
# list.displayList2()

##### good up to here, order of prev and next and current are all established correctly, look into reverse2 function

print('Doubly Linked List reverse(): ' + 'reversed')
list.reverse()

list.InsertOrder(31)
list.InsertOrderUnique(33)
list.InsertOrderUnique(33)
list.InsertOrderUnique(33)
list.remove(22)

print('Doubly Linked List all: ' + list.displayList())

list.cleanUp('111ap123ple32')

