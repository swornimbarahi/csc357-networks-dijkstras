#!/usr/bin/python3

from typing import List, Tuple, Dict
from utils import createAdjacencyList, printMaze


""" Simple depth first search algorithm to find the route.

    The route it provides is in no way optimized.
    
    @param: maze      List of List of strings
    @param: start     The starting Cell

    @returns: path    The Dict mapping the nextNodes to the previous nodes
"""


def dfs(maze: List[List[str]], start: Tuple[int]) -> Dict[Tuple[int], Tuple[int]]:
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
    return path
