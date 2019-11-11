#!/usr/bin/python3

"""
    Reads the maze file
    
    @params: n    the maze number to read
    
    Tuple return
    @returns: matrix  the List of list of strings
    @returns: start   The coordinates of the start cell S
    @returns: end     The coordinates of the end cell E
"""


def mazes(n: int):
    mazefile = open("maze" + str(n) + ".txt", "r")
    matrix = []
    for lines in mazefile:
        line = []
        for cell in lines.strip():
            line.append(cell)
        matrix.append(line)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "S":
                start = (i, j)
            elif matrix[i][j] == "E":
                end = (i, j)
    return matrix, start, end

