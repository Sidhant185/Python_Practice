# Q6: Snake Pattern Traversal
# Traverse matrix in snake/zigzag pattern (alternate directions per row)

def snakePattern(matrix):
    """
    Traverse matrix left-to-right then right-to-left alternately
    Time Complexity: O(m*n)
    Space Complexity: O(m*n) for result
    """
    res = []
    
    # Iterate through each row
    for i in range(len(matrix)):
        # Check if row index is even
        if i % 2 == 0:
            # Even rows: left to right
            for j in range(len(matrix[0])):
                res.append(matrix[i][j])
        else:
            # Odd rows: right to left
            for j in range(len(matrix[0]) - 1, -1, -1):
                res.append(matrix[i][j])
    
    return res