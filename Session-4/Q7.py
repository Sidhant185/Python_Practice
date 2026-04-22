def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    # Create new matrix with swapped dimensions
    res = [[0] * rows for _ in range(cols)]
    for r in range(rows):
        for c in range(cols):
            res[c][r] = matrix[r][c]
    return res