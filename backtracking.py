def backtracking(maze, start, end):
  stack = []
  stack.append(start)
  while len(stack) != 0:
    currCell = stack.pop()
    if (maze[currCell[0]][currCell[1]] != "E" and maze[currCell[0]][currCell[1]] != "S"):
      maze[currCell[0]][currCell[1]] = "."
    elif (maze[currCell[0]][currCell[1]] == "E"):
      printMaze(maze)
      return True
    stack += findNearbyFreeCells(maze, currCell)
  printMaze(maze)
  return False

def findNearbyFreeCells(maze, cell):
  freeCellList = []
  if(cell[0] > 0 and maze[cell[0] - 1][cell[1]] == " "):
    freeCellList.append([cell[0] - 1, cell[1]])
  if(cell[1] > 0 and maze[cell[0]][cell[1] - 1] == " "):
    freeCellList.append([cell[0], cell[1] - 1])
  if(cell[0] < len(maze) and maze[cell[0] + 1][cell[1]] == " "):
    freeCellList.append([cell[0] + 1, cell[1]])
  if(cell[0] < len(maze[0]) and maze[cell[0]][cell[1] + 1] == " "):
    freeCellList.append([cell[0], cell[1] + 1])
  return freeCellList