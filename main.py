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
  if(cell[0] > 0 and (maze[cell[0] - 1][cell[1]] == " " or maze[cell[0] - 1][cell[1]] == "E")):
    freeCellList.append([cell[0] - 1, cell[1]])
  if(cell[1] > 0 and (maze[cell[0]][cell[1] - 1] == " " or maze[cell[0]][cell[1] - 1] == "E")):
    freeCellList.append([cell[0], cell[1] - 1])
  if(cell[0] < len(maze) and (maze[cell[0] + 1][cell[1]] == " " or maze[cell[0] + 1][cell[1]] == "E")):
    freeCellList.append([cell[0] + 1, cell[1]])
  if(cell[0] < len(maze[0]) and (maze[cell[0]][cell[1] + 1] == " " or maze[cell[0]][cell[1] + 1] == "E")):
    freeCellList.append([cell[0], cell[1] + 1])
  return freeCellList

# ---------------------------------------------------------------------

def printMaze(maze):
  for line in maze:
    for cell in line:
      print(cell, end="")
    print("")

def main():
  maze = [
    ["#", "#", "#", "S", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", " ", " ", "#"],
    ["#", "#", "#", " ", "#", "#", " ", " ", " ", "#", "#", "#", " ", "#", "#"],
    ["#", "#", "#", " ", "#", "#", " ", "#", " ", "#", "#", "#", " ", "#", "#"],
    ["#", "#", " ", " ", " ", "#", " ", "#", " ", " ", " ", " ", " ", "#", "#"],
    ["#", "#", " ", "#", " ", "#", " ", "#", "#", "#", " ", "#", "#", "#", "#"],
    ["#", "#", " ", "#", " ", " ", " ", "#", "#", "#", " ", "#", "#", "#", "#"],
    ["#", "#", " ", "#", "#", " ", "#", "#", "#", "#", " ", "#", "#", "#", "#"],
    ["#", "#", " ", "#", "#", " ", "#", "#", "#", "#", " ", "#", "#", "#", "#"],
    ["#", "#", " ", "#", "#", " ", " ", " ", " ", " ", " ", "#", "#", "#", "#"],
    ["#", "#", " ", "#", "#", " ", "#", "#", " ", "#", " ", "#", "#", "#", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", " ", "#", " ", "#", "#", "#", "#"],
    ["#", " ", "#", "#", "#", " ", "#", "#", "#", "#", " ", "#", "#", "#", "#"],
    ["#", " ", "#", "#", "#", " ", "#", "#", "#", "#", " ", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "E", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
  ]
  printMaze(maze)
  print("\n\n\n")
  print(backtracking(maze, [0, 3], [14, 5]))


if __name__ == "__main__":
  main()