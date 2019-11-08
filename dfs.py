from utils import createAdjacencyList, printMaze

def dfs(maze, start):
    seenSet = set()
    path = {}
    stack = []
    stack.append(start)
    seenSet.add(start)
    adjacencyList = createAdjacencyList(maze, start)
    while len(stack) != 0:
        currNode = stack.pop()
        if maze[currNode[0]][currNode[1]] == "E":
            break
        for neighbor in adjacencyList.get(currNode):
            if not neighbor in seenSet:
                path[neighbor] = currNode
                stack.append(neighbor)
                seenSet.add(neighbor)
    print(currNode)
    print(path)
    while currNode != start:
      maze[currNode[0]][currNode[1]] = "."
      currNode = path.get(currNode)
    printMaze(maze)