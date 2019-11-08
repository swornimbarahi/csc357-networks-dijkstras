from utils import createAdjacencyList, printMaze

def bfs(maze, start):
    seenSet = set()
    path = {}
    queue = []
    queue.append(start)
    seenSet.add(start)
    adjacencyList = createAdjacencyList(maze, start)
    while len(queue) != 0:
        currNode = queue.pop(0)
        if maze[currNode[0]][currNode[1]] == "E":
            break
        for neighbor in adjacencyList.get(currNode):
            if not neighbor in seenSet:
                path[neighbor] = currNode
                queue.append(neighbor)
                seenSet.add(neighbor)
    print(currNode)
    print(path)
    while currNode != start:
      maze[currNode[0]][currNode[1]] = "."
      currNode = path.get(currNode)
    printMaze(maze)