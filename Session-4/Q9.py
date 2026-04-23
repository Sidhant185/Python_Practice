# Q9: Rotate Matrix 90 Degrees Clockwise
# Rotate square matrix in-place

def rotate(matrix):
    """
    Rotate square matrix 90 degrees clockwise
    Uses transpose + reverse approach
    Time Complexity: O(n^2)
    Space Complexity: O(1) - in-place modification
    """
    n = len(matrix)
    
    # Step 1: Transpose the matrix
    # Swap elements along diagonals
    for i in range(n):
        for j in range(i, n):
            # Swap matrix[i][j] with matrix[j][i]
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    # This completes the 90-degree clockwise rotation
    for i in range(n):
        matrix[i].reverse()