def mazes(n):
    mazefile = open("maze" + str(n) + ".txt", "r")
    matrix = []
    for lines in mazefile:
        line = []
        for cell in lines.strip():
            line.append(cell)
        matrix.append(line)
    return matrix

