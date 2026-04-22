def snakePattern(matrix):
    res = []
    for i in range(len(matrix)):
        if i % 2 == 0:
            for j in range(len(matrix[0])):
                res.append(matrix[i][j])
        else:
            for j in range(len(matrix[0]) - 1, -1, -1):
                res.append(matrix[i][j])
    return res