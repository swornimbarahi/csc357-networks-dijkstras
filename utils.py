def findNearbyFreeCells(maze, cell):
    freeCellList = []
    if cell[0] > 0 and (
        maze[cell[0] - 1][cell[1]] == " " or maze[cell[0] - 1][cell[1]] == "E"
    ):
        freeCellList.append([cell[0] - 1, cell[1]])
    if cell[1] > 0 and (
        maze[cell[0]][cell[1] - 1] == " " or maze[cell[0]][cell[1] - 1] == "E"
    ):
        freeCellList.append([cell[0], cell[1] - 1])
    if cell[0] < len(maze) - 1 and (
        maze[cell[0] + 1][cell[1]] == " " or maze[cell[0] + 1][cell[1]] == "E"
    ):
        freeCellList.append([cell[0] + 1, cell[1]])
    if cell[0] < len(maze[0]) - 1 and (
        maze[cell[0]][cell[1] + 1] == " " or maze[cell[0]][cell[1] + 1] == "E"
    ):
        freeCellList.append([cell[0], cell[1] + 1])
    return freeCellList


def printMaze(maze):
    for line in maze:
        for cell in line:
            print(cell, end="")
        print("")

def cleanMaze(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == ".":
                maze[i][j] = " "


def findAllNodes(maze, start):
    nodeList = []
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if checkNode(maze, (i, j)):
                nodeList.append((i, j))
    return nodeList


def checkNode(maze, cell):
    cellChar = maze[cell[0]][cell[1]]
    if cellChar == "#":
        return False
    if len(findNearbyFreeCells(maze, cell)) == 2:
        if (cell[0] > 0 and cell[0] < len(maze)) and (
            (maze[cell[0] - 1][cell[1]] == "#") and (maze[cell[0] + 1][cell[1]] == "#")
        ):
            return False
        if (cell[1] > 1 and cell[1] < len(maze[0])) and (
            (maze[cell[0]][cell[1] - 1] == "#") and (maze[cell[0]][cell[1] + 1] == "#")
        ):
            return False
    return True


def createAdjacencyList(maze, start):
    nodeList = findAllNodes(maze, start)
    adjacencyList = {}
    while len(nodeList) != 0:
        currNode = nodeList.pop()
        neighborCells = findNearbyFreeCells(maze, currNode)
        for neighborCell in neighborCells:
            if not currNode in adjacencyList:
                adjacencyList[currNode] = [
                    checkAdjacentNodes(maze, currNode, neighborCell)
                ]
            else:
                adjacencyList[currNode].append(
                    checkAdjacentNodes(maze, currNode, neighborCell)
                )
    return adjacencyList


def checkAdjacentNodes(maze, node, neighborCell):
    foundAdjacent = False
    dumCell = neighborCell
    if neighborCell[0] == node[0] - 1:
        while not foundAdjacent:
            if checkNode(maze, dumCell):
                foundAdjacent = True
            else:
                dumCell[0] -= 1
    if neighborCell[1] == node[1] - 1:
        while not foundAdjacent:
            if checkNode(maze, dumCell):
                foundAdjacent = True
            else:
                dumCell[1] -= 1
    if neighborCell[0] == node[0] + 1:
        while not foundAdjacent:
            if checkNode(maze, dumCell):
                foundAdjacent = True
            else:
                dumCell[0] += 1
    if neighborCell[1] == node[1] + 1:
        while not foundAdjacent:
            if checkNode(maze, dumCell):
                foundAdjacent = True
            else:
                dumCell[1] += 1
    return (dumCell[0], dumCell[1])


def distanceBetweenTwoNodes(firstNode, secondNode):
    return (
        (firstNode[0] - secondNode[0]) ** 2 - (firstNode[1] - secondNode[1]) ** 2
    ) ** (1 / 2)

