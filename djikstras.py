#!/usr/bin/python3

import sys
from typing import List, Tuple, Dict
from utils import printMaze, findAllNodes, createAdjacencyList, distanceBetweenTwoNodes

""" 
    Return the shortest path according to djikstras algorithm
    @param: maze      List of List of strings
    @param: start     The starting Cell

    @returns: path    The Dict mapping the nextNodes to the previous nodes
"""


def djikstras(maze: List[List[str]], start: Tuple[int]):
    nodeList = findAllNodes(maze, start)
    adjacencyList = createAdjacencyList(maze, start)
    unvisited = set(nodeList)
    distance = {}
    path = {}
    for node in nodeList:
        distance[node] = sys.maxsize
        path[node] = None
    distance[start] = 0
    while len(unvisited) != 0:
        current = getMin(unvisited, distance)
        unvisited.discard(current)
        for neighbor in adjacencyList[current]:
            if neighbor in unvisited:
                alt = distance[current] + distanceBetweenTwoNodes(current, neighbor)
                if alt < distance[neighbor]:
                    distance[neighbor] = alt
                    path[neighbor] = current
    return path


"""
  Returns the minimum distance node that is present
  in the node set.

  @param: nodeSet       the Set of nodes to choose from
  @param: distanceDict  the dictionary of the tentative distances from the source

  @returns: retNode     the node with the minimum distance
"""


def getMin(nodeSet: set, distanceDict: dict):
    minimum = sys.maxsize
    retNode = None
    for node in nodeSet:
        if node in distanceDict and distanceDict[node] < minimum:
            retNode = node
            minimum = distanceDict[node]
    return retNode
