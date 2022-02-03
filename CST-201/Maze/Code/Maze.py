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

    # O-1
    def InsertFront(self, newVal):
        oldNode = self.headVal;
        newNode = Node(newVal);
        self.headVal = newNode;
        self.headVal.nextVal = oldNode;
        self.listSize += 1;

    # O-1 front
    def pop_front(self):
        headVal = self.headVal.dataVal
        self.headVal = self.headVal.nextVal
        self.listSize -= 1
        return str(headVal);

    # O-1
    def empty(self):
        if self.headVal == None:
            return True
        else:
            return False

    # O-1
    def size(self):
        return self.listSize
        
    # O-1
    def clear(self):
        self.headVal = Node()
        self.listSize = 0





list = LinkedList()
