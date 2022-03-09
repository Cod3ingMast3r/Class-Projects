import os;
from copy import copy

class Node:
    def __init__(self, dataVal = None):
        self.dataVal = dataVal;
        self.nextVal = None;



class Stack:
    def __init__(self):
        self.headVal = None;
        self.listSize = 0

    # def Head(self, headVal = None):
    #     self.headVal = headVal;
    
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
    # Insert_front
    def Push(self, newVal):
        oldNode = self.headVal;
        newNode = Node(newVal);
        self.headVal = newNode;
        self.headVal.nextVal = oldNode;
        self.listSize += 1;

    # O-1 front
    # pop_front
    def Pop(self):
        headVal = self.headVal.dataVal
        self.headVal = self.headVal.nextVal
        self.listSize -= 1
        return headVal;

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

mazeStack = Stack()

currentDirectory = os.getcwd() + '\Maze\Lists'

mazeFile = open(currentDirectory + '\Maze.txt', 'r');

row = -1
for line in mazeFile.readlines():
    column = 0
    if row == -1:
        rowByCol = line.split(' ')
        maze = [[None]*int(rowByCol[1]) for _ in range (int(rowByCol[0]))]
    else:
        for value in line.split(' '):
            maze[row][column] = int(value)
            column += 1
    row += 1

class MazeCell:
    def __init__(self, row = -1, col = -1):
        self.row = row;
        self.col = col;
        self.direction = 0;
        self.visited = False

    # O-1
    # Copy Constructor
    def MazeCell(self, rhs):
        self.row = rhs.row
        self.col = rhs.col
        self.direction = rhs.direction
        self.visited = rhs.visited

    # O-1
    def getDirection(self):
        return(self.direction)
    
    # O-1
    def advanceDirection(self):
        self.direction += 1;
        if self.direction == 4:
            self.visited = True;
    
    # O-1
    def setcoordinates(self, r, c):
        self.row = r;
        self.col = c;

    # O-1
    def getRow(self):
        return(self.row);

    # O-1
    def getCol(self):
        return(self.col);

    # O-1
    # set visited status to True
    def visit(self):
        self.visited = True;
    # O-1
    # resets visited status to false
    def resetVisit(self):
        self.visited = False;

    # O-1
    # returns true if cell is unvisited
    def unVisited(self):
        return(not self.visited)

    # O-1
    # return string Val of Cell
    def toString(self):
        return("(" + str(self.row) + "," + str(self.col) + ")")

list = Stack()

for row in maze:
    for col in row:
        print(col, sep = ' ', end = ' ')
    print()

for rowIndx, row in enumerate(maze):
    for colIndx, col in enumerate(row):
        if maze[rowIndx][colIndx] == 0:
            maze[rowIndx][colIndx] = MazeCell(-1,-1)
        if maze[rowIndx][colIndx] == 3:
            start = MazeCell(rowIndx, colIndx)
            maze[rowIndx][colIndx] = start
        if maze[rowIndx][colIndx] == 4:
            end = MazeCell(rowIndx, colIndx)
            maze[rowIndx][colIndx] = end
        if maze[rowIndx][colIndx] == 1:
            maze[rowIndx][colIndx] = MazeCell(rowIndx, colIndx)

def DepthSearchMaze(maze, start, mazeStack):
    rowMax = len(maze)-1
    colMax = len(maze[0])-1
    row = start.getRow()
    col = start.getCol()

    currentCell = maze[row][col]

    row_increase_or_decrease = 1
    col_increase_or_decrease = 0

    # if mazeStack.empty() == False:
    #     print(mazeStack.front())

    row_or_col = None
    row_or_col_Max = None
    increase = 1
    decrease = -1

    directions = ['DOWN', 'RIGHT', 'LEFT', 'UP']

    NotFound = True

    while NotFound:
        potentialCell = None
        for directionIndx, direction in enumerate(directions):
            row_increase_or_decrease = 0
            col_increase_or_decrease = 0
            if direction == 'DOWN':
                row_or_col = row
                row_or_col_Max = rowMax
                row_increase_or_decrease = increase
            elif direction == 'RIGHT':
                row_or_col = col
                row_or_col_Max = colMax
                col_increase_or_decrease = increase
            elif direction == 'LEFT':
                row_or_col = col
                row_or_col_Max = 0
                col_increase_or_decrease = decrease
            elif direction == 'UP':
                row_or_col = row
                row_or_col_Max = 0
                row_increase_or_decrease = decrease
            else:
                print("Error, this direction: " + direction + " is not an accepted value")
                NotFound = False
                print("EXITING")
                break

            if (row_or_col != row_or_col_Max):
                nextCell = maze[row + row_increase_or_decrease][col + col_increase_or_decrease]
                if nextCell.toString() != '(-1,-1)':
                    if nextCell.unVisited():
                        noDirection = False
                        row += row_increase_or_decrease
                        col += col_increase_or_decrease
                        currentCell.visit()
                        mazeStack.Push(currentCell)
                        currentCell = maze[row][col]
                        # print(currentCell.toString())
                        if currentCell.toString() == end.toString():
                            currentCell.visit()
                            mazeStack.Push(currentCell)
                            print("Path from end to start: ")
                            NotFound = False
                            for cell in range(0,mazeStack.size()):
                                print(mazeStack.Pop().toString())
                        else:
                            break
            else:
                next
        if (directionIndx == len(directions)-1) and (noDirection == True):
            if currentCell.toString() == start.toString():
                print("No exit")
                NotFound = False
            else:
                currentCell.visit()
                currentCell = mazeStack.Pop()
                # print(currentCell.toString())
                row = currentCell.getRow()
                col = currentCell.getCol()
        noDirection = True
DepthSearchMaze(maze, start, mazeStack)