#!/usr/bin/python3

from typing import List, Tuple, Dict
from utils import findNearbyFreeCells, printMaze, cleanMaze

""" Simple backtracking algorithm checking every path possible
    to find the route.

    The route it provides is in no way optimized.
    
    @param: maze      List of List of strings
    @param: start     The starting Cell

    @returns: path    The Dict mapping the nextNodes to the previous nodes
"""


def backtracking(
    maze: List[List[str]], start: Tuple[int]
) -> Dict[Tuple[int], Tuple[int]]:
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
    return path