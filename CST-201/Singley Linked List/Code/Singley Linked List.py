from copy import copy;
class Node:
    def __init__(self, dataVal = None):
        self.dataVal = dataVal;
        self.nextVal = None;
    


class LinkedList:
    def __init__(self):
        self.headVal = None;
        self.listSize = 0

    # def Head(self, headVal = None):
    #     self.headVal = headVal;

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
                
                if newVal < currentNode.dataVal:
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
            # currentNode.nextVal = Node(newVal);
    
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

    # O-2n
    def merge(self, linkedList):
        newList = copy(self)
        currentNode = linkedList.headVal
        while currentNode != None:
            newList.Insert(currentNode.dataVal)
            currentNode = currentNode.nextVal;
        self.clear()
        linkedList.clear()
        return newList
        
    # O-1
    def clear(self):
        self.headVal = Node()
        self.listSize = 0





list = LinkedList()

print('Singley Linked List empty(): ' + str(list.empty()))
print('Singley Linked List all: ' + list.displayList())

list.Insert(33)
list.Insert(44)
list.Insert(22)
list.Insert(100)
list.Insert(37)
list.Insert(49)
list.Insert(1)
list.Insert(9)

print('Singley Linked List all: ' + list.displayList())

print('Singley Linked List front(): ' + list.front())

print('Singley Linked List back(): ' + list.back())

print('Singley Linked List pop_back() value: ' + list.pop_back())

print('Singley Linked List all: ' + list.displayList())

print('Singley Linked List pop_front() value: ' + list.pop_front())

print('Singley Linked List all: ' + list.displayList())

print('Singley Linked List size(): ' + str(list.size()))

list2 = LinkedList()

list2.Insert(39)
list2.Insert(17)
list2.Insert(13)
list2.Insert(45)

print('Singley Linked List merge(): ' + 'merged')
list3 = list.merge(list2)
print('Singley Linked List all: ' + list3.displayList())

print('Singley Linked List reverse(): ' + 'reversed')
list3.reverse()

print('Singley Linked List all: ' + list3.displayList())