# Q7: Transpose Matrix
# Swap rows and columns of matrix

def transpose(matrix):
    """
    Transpose matrix by swapping rows and columns
    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    """
    # Get original dimensions
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create new matrix with swapped dimensions
    # Rows become cols and cols become rows
    res = [[0] * rows for _ in range(cols)]
    
    # Copy elements with swapped indices
    for r in range(rows):
        for c in range(cols):
            # Element at (r,c) goes to (c,r)
            res[c][r] = matrix[r][c]
    
    return res