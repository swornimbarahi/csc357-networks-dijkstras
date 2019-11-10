from utils import findNearbyFreeCells, printMaze, cleanMaze

def backtracking(maze, start):
    stack = []
    stack.append(start)
    path = {}
    while len(stack) != 0:
        currCell = stack.pop()
        if (
            maze[currCell[0]][currCell[1]] != "E"
            and maze[currCell[0]][currCell[1]] != "S"
        ):
            maze[currCell[0]][currCell[1]] = "."
        elif maze[currCell[0]][currCell[1]] == "E":
            break
        nearbyCells = findNearbyFreeCells(maze, currCell)
        stack += nearbyCells
        for cell in nearbyCells:
            path[(cell[0], cell[1])] = currCell
    cleanMaze(maze)
    while currCell != start:
        currCell = path.get((currCell[0], currCell[1]))
        maze[currCell[0]][currCell[1]] = "."
    printMaze(maze)

