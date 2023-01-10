import os;

currentDirectory = os.getcwd() + '\Project8 Graph\Lists'

mazeFile = open(currentDirectory + '\Maze.txt', 'r');

row = -1
for line in mazeFile.readlines():
    column = 0
    if row == -1:
        rowByCol = line.split(' ')
        graph = [[None]*int(rowByCol[1]) for _ in range (int(rowByCol[0]))]
    else:
        for value in line.split(' '):
            graph[row][column] = int(value)
            column += 1
    row += 1

for row in graph:
    for col in row:
        print(col, sep = ' ', end = ' ')
    print()
print()

# O(V+E)
def distance(graph, start, end):
    originalEnd = end
    totalWeight = 0
    if graph[start][end] != 0:
        return graph[start][end]
    else:
        if end != (len(graph)-1):
            end +=1
        else:
            end = 0 
        while end != originalEnd:
            end = originalEnd
            while graph[start][end] == 0:
                if end != (len(graph)-1):
                    end +=1
                else:
                    end = 0 
            distance_var = graph[start][end]

            print("Start: " + str(start))
            print("End: " + str(end))
            print("Distance: " + str(distance_var), end='\n\n')
            totalWeight += distance_var
            graph[start][end] = 0
            start = end

        return totalWeight
print("Total Distance: " + str(distance(graph, 0, 9)))
print()