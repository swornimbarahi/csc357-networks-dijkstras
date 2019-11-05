from utils import findNearbyFreeCells, printMaze

def backtracking(maze, start):
    stack = []
    stack.append(start)
    while len(stack) != 0:
        currCell = stack.pop()
        if (
            maze[currCell[0]][currCell[1]] != "E"
            and maze[currCell[0]][currCell[1]] != "S"
        ):
            maze[currCell[0]][currCell[1]] = "."
        elif maze[currCell[0]][currCell[1]] == "E":
            printMaze(maze)
            return True
        stack += findNearbyFreeCells(maze, currCell)
    printMaze(maze)
    return False


