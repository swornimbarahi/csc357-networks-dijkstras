#!/usr/bin/python3

from typing import List, Tuple, Dict


"""
    @param: maze    List of List of strings
    @param: cell    Tuple of ints for coordinates

    @returns: freeCellList    The list of free cells around the given coordinates
"""


def findNearbyFreeCells(maze: List[List[str]], cell: Tuple[int]) -> List[Tuple[int]]:
    freeCellList = []
    if cell[0] > 0 and (
        maze[cell[0] - 1][cell[1]] == " " or maze[cell[0] - 1][cell[1]] == "E"
    ):
        freeCellList.append((cell[0] - 1, cell[1]))
    if cell[1] > 0 and (
        maze[cell[0]][cell[1] - 1] == " " or maze[cell[0]][cell[1] - 1] == "E"
    ):
        freeCellList.append((cell[0], cell[1] - 1))
    if cell[0] < len(maze) - 1 and (
        maze[cell[0] + 1][cell[1]] == " " or maze[cell[0] + 1][cell[1]] == "E"
    ):
        freeCellList.append((cell[0] + 1, cell[1]))
    if cell[0] < len(maze[0]) - 1 and (
        maze[cell[0]][cell[1] + 1] == " " or maze[cell[0]][cell[1] + 1] == "E"
    ):
        freeCellList.append((cell[0], cell[1] + 1))
    return freeCellList


"""
    Prints the maze out in the terminal

    @param: maze    List of List of strings
"""


def printMaze(maze: List[List[str]]):
    for line in maze:
        for cell in line:
            print(cell, end="")
        print("")


"""
    Prints the maze in color out in the terminal

    @param: maze    List of List of strings
"""


def printMazeInColor(maze: List[List[str]]):
    for line in maze:
        for cell in line:
            if cell == "#":
                print("\033[93m{}\033[00m".format(cell), end="")
            elif cell == ".":
                print("\033[91m{}\033[00m".format(cell), end="")
            else:
                print(cell, end="")
        print("")


"""
    Cleans the maze of any tracks left behind

    @param: maze    List of List of strings
"""


def cleanMaze(maze: List[List[str]]):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == ".":
                maze[i][j] = " "


"""
    Searches the map for all nodes

    @param: maze    List of List of strings
    @param: start   The tuple coordinate of the starting cell

    @returns: nodeList the List of all nodes
"""


def findAllNodes(maze: List[List[str]], start: Tuple[int]) -> List[Tuple[int]]:
    nodeList = []
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if checkNode(maze, (i, j)):
                nodeList.append((i, j))
    return nodeList


"""
    Checks if any given cell is a Node

    @param: maze    List of List of strings
    @param: start   The tuple coordinate of the starting cell

    @returns: if the cell is a node
"""


def checkNode(maze: List[List[str]], cell: Tuple[int]) -> bool:
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


"""
    Creates an adjacency list from the maze

    @param: maze    List of List of strings
    @param: start   The tuple coordinate of the starting cell

    @returns: the dictionary of anode mapping to its neighbors
"""

"""
 -> Dict[Tuple[int], List[Tuple[int]]]
"""


def createAdjacencyList(maze: List[List[str]], start: Tuple[int]):
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


"""
    Creates an adjacency of nodes in the maze

    @param: maze    List of List of strings
    @param: node    The tuple coordinate of a node
    @param: neighborCell    The tuple coordinate of the neighbor

    @returns: the node as the tuple that is in the general direction of the node
"""


def checkAdjacentNodes(
    maze: List[List[str]], node: Tuple[int], neighborCell: Tuple[int]
) -> Tuple[int]:
    foundAdjacent = False
    dumCell = [neighborCell[0], neighborCell[1]]
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


"""
    The distance between any two cells

    @param: firstNode     the coordinates first node
    @param: secondNode    the coordinates second node

    @returns: the distance between the two nodes
"""


def distanceBetweenTwoNodes(firstNode: Tuple[int], secondNode: Tuple[int]):
    return (
        (firstNode[0] - secondNode[0]) ** 2 + (firstNode[1] - secondNode[1]) ** 2
    ) ** (1 / 2)


"""
   Draw on the maze to connect two neighbor nodes

    @param: maze          the list of list of strings
    @param: currCell      the coordinates first node
    @param: nextCell      the coordinates second node
"""


def connectTwoCells(maze: List[List[str]], currCell: Tuple[int], nextCell: Tuple[int]):
    dumNode = [currCell[0], currCell[1]]
    if currCell[0] < nextCell[0]:
        while dumNode[0] != nextCell[0]:
            maze[dumNode[0]][dumNode[1]] = "."
            dumNode[0] += 1
    if currCell[1] < nextCell[1]:
        while dumNode[1] != nextCell[1]:
            maze[dumNode[0]][dumNode[1]] = "."
            dumNode[1] += 1
    if currCell[0] > nextCell[0]:
        while dumNode[0] != nextCell[0]:
            maze[dumNode[0]][dumNode[1]] = "."
            dumNode[0] -= 1
    if currCell[1] > nextCell[1]:
        while dumNode[1] != nextCell[1]:
            maze[dumNode[0]][dumNode[1]] = "."
            dumNode[1] -= 1

