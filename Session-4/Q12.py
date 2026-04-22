def hourglassSum(matrix):
    max_sum = float('-inf')
    for r in range(len(matrix) - 2):
        for c in range(len(matrix[0]) - 2):
            top = sum(matrix[r][c:c+3])
            mid = matrix[r+1][c+1]
            bot = sum(matrix[r+2][c:c+3])
            max_sum = max(max_sum, top + mid + bot)
    return max_sum