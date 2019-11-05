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
    if cell[0] < len(maze) and (
        maze[cell[0] + 1][cell[1]] == " " or maze[cell[0] + 1][cell[1]] == "E"
    ):
        freeCellList.append([cell[0] + 1, cell[1]])
    if cell[0] < len(maze[0]) and (
        maze[cell[0]][cell[1] + 1] == " " or maze[cell[0]][cell[1] + 1] == "E"
    ):
        freeCellList.append([cell[0], cell[1] + 1])
    return freeCellList


def printMaze(maze):
    for line in maze:
        for cell in line:
            print(cell, end="")
        print("")


# def nodeFinder(maze, start):
#   nodeList = []
#   for line in maze:
#     for cell in line:
#       if ()


def nodeChecker(maze, cell):
    if (
        maze[cell[0]][cell[1]] == "S"
        or maze[cell[0]][cell[1]] == "E"
        or (
            maze[cell[0]][cell[1]] == " "
            and (
                len(findNearbyFreeCells(maze, cell)) > 2
                or len(findNearbyFreeCells(maze, cell)) == 1
            )
        )
    ):
        return true

