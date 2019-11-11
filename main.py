#!/usr/bin/python3

"""
    Author:   Swornim Barahi
    Date:     11/11/2019
    
    Title:            Final Project for CSC357
    Submitted to:     Dr. Kevin McCullen
    
    Description:    A program that solves mazes using commonly known algorithms
"""

from backtracking import backtracking
from dfs import dfs
from bfs import bfs
from djikstras import djikstras
from utils import (
    printMaze,
    printMazeInColor,
    checkNode,
    createAdjacencyList,
    findNearbyFreeCells,
    connectTwoCells,
)
from mazes import mazes

""" Contains the main code to run all path finding algorithms

    Run this program in the command line.
    The program will prompt you for some options.
"""


def main():
    print("\n\n\nEnter the maze number that you want to solve.")
    mazeNumber = int(input("[1]. maze1.txt \t 2. maze2.txt \t 3. maze3.txt\n"))

    print("\n\nEnter algorithm number you would like to use.")
    algoPref = int(
        input(
            "[1]. Djikstra's \n 2. Breadth First Searh \n 3. Depth First Search \n 4. Backtracking\n"
        )
    )

    print("\n\nDo you want to get the output in color?")
    color = input("[Y]es\t\tNo\n")

    maze, start, end = mazes(mazeNumber)

    if algoPref == 4:
        path = backtracking(maze, start)
    elif algoPref == 3:
        path = dfs(maze, start)
    elif algoPref == 2:
        path = bfs(maze, start)
    else:
        path = djikstras(maze, start)

    # Printing the maze with the solution for the respective path finding algorithm
    currNode = end
    while currNode != (0, 1):
        nextNode = path[currNode]
        connectTwoCells(maze, currNode, nextNode)
        currNode = nextNode
    if color == "Y" or color == "y" or color.capitalize() == "Yes":
        printMazeInColor(maze)
    else:
        printMaze(maze)


if __name__ == "__main__":
    main()

