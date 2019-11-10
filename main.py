from backtracking import backtracking
from dfs import dfs
from bfs import bfs
from djikstras import djikstras
from utils import printMaze, checkNode, createAdjacencyList, findNearbyFreeCells
from mazes import mazes

def main():
    maze = mazes(2)
    print(djikstras(maze, (0,1)))

if __name__ == "__main__":
    main()

