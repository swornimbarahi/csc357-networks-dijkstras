import sys
from utils import printMaze, findAllNodes, createAdjacencyList, distanceBetweenTwoNodes


def djikstras(maze, start):
    nodeList = findAllNodes(maze, start)
    adjacencyList = createAdjacencyList(maze, start)
    unvisited = set(nodeList)
    distance = {}
    path = {}
    for node in nodeList:
        distance[node] = sys.maxsize
        path[node] = None
    distance[start] = 0
    while len(unvisited) != 0:
        current = getMin(unvisited, distance)
        unvisited.discard(current)
        for neighbor in adjacencyList[current]:
            if neighbor in unvisited:
                alt = distance[current] + distanceBetweenTwoNodes(current, neighbor)
                print(alt, "====>", distance[neighbor])
                if alt < distance[neighbor]:
                    distance[neighbor] = alt
                    path[neighbor] = current
    
    currNode = (19, 2)
    while currNode != start:
      maze[currNode[0]][currNode[1]] = "."
      currNode = path.get(currNode)
    printMaze(maze)
    return path


def getMin(nodeSet, distanceDict):
    minimum = sys.maxsize
    retNode = None
    for node in nodeSet:
        if node in distanceDict and distanceDict[node] < minimum:
            retNode = node
            minimum = distanceDict[node]
    return retNode
